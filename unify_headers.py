#!/usr/bin/env python3
"""Unify formatting of raw HTTP header / protocol snippets across the site.
Some pages already wrap these in fenced code blocks, others left them as
bare or bold-wrapped paragraph lines. Normalize everything to a single
fenced code block per group, stripping stray bold markers."""
import glob
import re

HEADER_LINE_RE = re.compile(
    r"^\*{0,3}(Authorization|Accept|Content-Type|lang|Client-Secret|Vendor)\s*:",
    re.I,
)
FENCE_RE = re.compile(r"^\s*```")


def clean(line):
    return line.replace("*", "").strip()


def process(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    out = []
    in_fence = False
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue
        if not in_fence and HEADER_LINE_RE.match(line.strip()):
            group = []
            while i < n:
                cur = lines[i]
                if HEADER_LINE_RE.match(cur.strip()):
                    group.append(clean(cur))
                    i += 1
                elif cur.strip() == "" and i + 1 < n and HEADER_LINE_RE.match(lines[i + 1].strip()):
                    i += 1  # skip blank line between header lines
                else:
                    break
            out.append("```")
            out.extend(group)
            out.append("```")
            continue
        out.append(line)
        i += 1

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    for p in glob.glob("docs/vendors/*.md") + glob.glob("docs/logistics/*.md"):
        before = open(p, encoding="utf-8").read()
        process(p)
        after = open(p, encoding="utf-8").read()
        if before != after:
            print("changed", p)
