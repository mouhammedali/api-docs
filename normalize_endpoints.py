#!/usr/bin/env python3
"""Clean up endpoint headings: strip the meaningless page-spanning numbers
(vendors were numbered 1-10+ across the whole original document, which
looks broken once split across pages), strip stray bold markers, and pull
the HTTP method + path out into a styled badge line instead of jamming
them into the heading text."""
import glob
import re

METHOD_RE = re.compile(r"\[(GET|POST|PUT|DELETE|PATCH)\]", re.I)
ANCHOR_RE = re.compile(r"(vendor_Base_URL|Auth_Base_URL|Base_URL)", re.I)
NUM_RE = re.compile(r"^\d+\.\s*")
HEADING_RE = re.compile(r"^(#{3,4})\s*(.*?)\s*$")
ENDPOINT_LABEL_RE = re.compile(r"^(\*\*Endpoint:\*\*)\s*(.*)$")


def badge(method, path):
    parts = []
    if method:
        parts.append(f'<span class="api-method api-method--{method.lower()}">{method.upper()}</span>')
    if path:
        parts.append(f"<code>{path}</code>")
    return " ".join(parts)


def extract(text):
    text = text.replace("**", "")
    text = NUM_RE.sub("", text)
    method = None
    m = METHOD_RE.search(text)
    if m:
        method = m.group(1).upper()
        text = METHOD_RE.sub("", text)
    path = None
    a = ANCHOR_RE.search(text)
    if a:
        path = text[a.start():].strip()
        text = text[:a.start()]
    name = re.sub(r"\s+", " ", text).strip()
    return name, method, path


def process(path_):
    lines = open(path_, encoding="utf-8").read().split("\n")
    out = []
    for line in lines:
        hm = HEADING_RE.match(line)
        em = ENDPOINT_LABEL_RE.match(line)
        if hm:
            hashes, raw = hm.groups()
            name, method, path = extract(raw)
            if name:
                out.append(f"{hashes} {name}")
                if method or path:
                    out.append("")
                    out.append(badge(method, path))
            elif method or path:
                out.append(badge(method, path))
            continue
        if em:
            label, rest = em.groups()
            _, method, path = extract(rest)
            out.append(f"{label} {badge(method, path)}")
            continue
        out.append(line)

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    with open(path_, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    for p in glob.glob("docs/vendors/*.md") + glob.glob("docs/logistics/*.md"):
        process(p)
        print("processed", p)
