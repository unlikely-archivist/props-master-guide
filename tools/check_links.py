#!/usr/bin/env python3
"""Check every internal Markdown link and #anchor in the repo.

Usage (from the repo root):  python3 tools/check_links.py
Exit status is 1 if any link points to a missing file or heading.
Anchors follow GitHub's rules: lowercase, punctuation dropped, spaces -> hyphens,
and duplicate headings get -1, -2, ...
"""
import glob
import os
import re
import sys


def slug(heading):
    h = heading.strip().lower()
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")


def main():
    files = glob.glob("**/*.md", recursive=True)
    anchors = {}
    for f in files:
        seen, found = {}, set()
        for line in open(f, encoding="utf-8"):
            m = re.match(r"^(#+)\s+(.*)", line)
            if m:
                s = slug(m.group(2))
                n = seen.get(s, 0)
                found.add(s if n == 0 else f"{s}-{n}")
                seen[s] = n + 1
        anchors[os.path.normpath(f)] = found

    bad = 0
    for f in files:
        text = open(f, encoding="utf-8").read()
        for m in re.finditer(r"\]\(([^)\s]+)\)", text):
            target = m.group(1)
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            path, _, anchor = target.partition("#")
            dest = os.path.normpath(os.path.join(os.path.dirname(f), path)) if path else os.path.normpath(f)
            if dest not in anchors:
                print(f"MISSING FILE  {f}: {target}")
                bad += 1
            elif anchor and anchor not in anchors[dest]:
                print(f"BAD ANCHOR    {f}: {target}")
                bad += 1
    print(f"{bad} broken link(s)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
