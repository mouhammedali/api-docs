#!/usr/bin/env python3
"""Clean up pandoc-generated markdown: unescape stray markdown escapes outside
fenced code blocks, tidy pandoc span/mark artifacts, and pretty-print valid
JSON inside ```json fences for consistent formatting."""
import json
import re
import sys

ESCAPE_MAP = {
    r"\[": "[",
    r"\]": "]",
    r"\_": "_",
    r"\*": "*",
    r"\-": "-",
    r"\.": ".",
    r"\'": "'",
    r"\$": "$",
}

SPAN_RTL = re.compile(r'\[([^\[\]]*)\]\{dir="rtl"\}')
SPAN_MARK = re.compile(r"\[([^\[\]]*)\]\{\.mark\}")
SPAN_UNDERLINE = re.compile(r"\[([^\[\]]*)\]\{\.underline\}")


def clean_prose_line(line):
    line = SPAN_RTL.sub(r"\1", line)
    line = SPAN_MARK.sub(r"\1", line)
    line = SPAN_UNDERLINE.sub(r"\1", line)
    for esc, plain in ESCAPE_MAP.items():
        line = line.replace(esc, plain)
    line = line.replace("(docs/assets/", "(assets/")
    return line


def prettify_json_block(lines):
    text = "\n".join(lines)
    try:
        obj = json.loads(text)
    except (json.JSONDecodeError, ValueError):
        return lines
    pretty = json.dumps(obj, indent=2, ensure_ascii=False)
    return pretty.split("\n")


DIVIDER_RE = re.compile(r"^\s*-{5,}\s*$")


def process(path):
    with open(path, encoding="utf-8") as f:
        raw_lines = f.read().split("\n")

    out = []
    i = 0
    n = len(raw_lines)
    while i < n:
        line = raw_lines[i]
        fence_match = re.match(r"^(\s*)```\s*(\w*)\s*$", line)
        if fence_match:
            indent, lang = fence_match.groups()
            block = []
            i += 1
            while i < n and raw_lines[i].strip() != "```":
                block.append(raw_lines[i])
                i += 1
            if lang == "json":
                block = prettify_json_block(block)
            out.append(f"{indent}```{lang}")
            out.extend(block)
            out.append(f"{indent}```")
            i += 1
            continue
        if DIVIDER_RE.match(line):
            i += 1
            continue
        out.append(clean_prose_line(line))
        i += 1

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    for p in sys.argv[1:]:
        process(p)
        print("processed", p)
