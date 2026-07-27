#!/usr/bin/env python3
"""Some Word docs typed each line of a JSON example as its own paragraph
(no table, no manual line-break) instead of a preformatted block. Pandoc
emits these as one Markdown paragraph per line, each escaped for Markdown.
This pass detects runs of paragraphs that form a balanced {...} / [...]
block and merges them into a single fenced ```json code block.
"""
import json
import re
import sys

BOLD_RE = re.compile(r"^\*\*(.*)\*\*$")


def clean(line):
    m = BOLD_RE.match(line.strip())
    text = m.group(1) if m else line.strip()
    text = text.replace('\\"', '"').replace("\\_", "_").replace("\\*", "*")
    text = text.replace("\\[", "[").replace("\\]", "]")
    return text


def is_opener(cleaned):
    return cleaned in ("{", "[")


def process(path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")

    out = []
    i, n = 0, len(lines)
    in_fence = False
    while i < n:
        line = lines[i]
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue
        cleaned = clean(line)
        if not in_fence and is_opener(cleaned):
            depth = cleaned.count("{") + cleaned.count("[") - cleaned.count("}") - cleaned.count("]")
            block = [cleaned]
            j = i + 1
            consumed_ok = False
            while j < n and j - i < 400:
                if lines[j].strip() == "":
                    j += 1
                    continue
                c = clean(lines[j])
                if c.startswith("#"):
                    break
                depth += c.count("{") + c.count("[") - c.count("}") - c.count("]")
                block.append(c)
                j += 1
                if depth <= 0:
                    consumed_ok = True
                    break
            if consumed_ok and len(block) > 1:
                text = "\n".join(block)
                try:
                    obj = json.loads(text)
                    text = json.dumps(obj, indent=2, ensure_ascii=False)
                except (json.JSONDecodeError, ValueError):
                    pass
                out.append("```json")
                out.extend(text.split("\n"))
                out.append("```")
                i = j
                continue
        out.append(line)
        i += 1

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        process(p)
        print("merged json paragraphs in", p)
