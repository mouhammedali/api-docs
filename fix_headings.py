#!/usr/bin/env python3
"""Normalize heading hierarchy left messy by inconsistent Word heading styles.

- Deletes empty headings (Word manual-break artifacts with no text).
- Turns heading-wrapped images into plain (non-heading) image paragraphs.
- Demotes small field-label headings (Payload, Response, Header, Status: 200, ...)
  to H4 regardless of their original level, since they're always a sub-part of
  whatever endpoint/section precedes them.
- Optionally demotes any remaining top-level (H1) heading that isn't a real
  top-level section to H2, for documents where H1 was misused as a mid-level style.
"""
import re
import sys

LABELS = {
    "payload", "response", "header", "headers", "request", "request body",
    "request payload", "response body", "response example", "response examples",
    "expected response", "query params", "query parameters", "note", "notes",
}

HEADING_RE = re.compile(r"^(#{1,6})\s*(.*?)\s*$")
STRIP_MD_RE = re.compile(r"[\*_]")
STATUS_RE = re.compile(r"^(success\s+)?(response\s+)?status\s*:?\s*\d+", re.I)
IMAGE_ONLY_RE = re.compile(r"^!\[[^\]]*\]\([^)]*\)(\{[^}]*\})?$")


def is_label(text):
    plain = STRIP_MD_RE.sub("", text).strip().lower()
    if plain in LABELS:
        return True
    if STATUS_RE.match(plain):
        return True
    return False


def process(path, demote_h1):
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")

    out = []
    for line in lines:
        m = HEADING_RE.match(line)
        if not m:
            out.append(line)
            continue
        hashes, text = m.groups()

        if IMAGE_ONLY_RE.match(text.strip()):
            out.append(text)
            continue

        plain = STRIP_MD_RE.sub("", text).strip()

        if plain == "":
            if "![" in text:
                out.append(text)  # keep image, drop heading marker
            # else: drop the empty heading entirely
            continue

        if is_label(text):
            out.append(f"#### {text}")
            continue

        if demote_h1 and len(hashes) == 1:
            out.append(f"## {text}")
            continue

        out.append(line)

    # collapse 3+ blank lines left behind by deletions
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    process("docs/vendors-api.md", demote_h1=True)
    process("docs/logistics-api.md", demote_h1=False)
    print("headings normalized")
