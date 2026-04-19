#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD_FILES = list(ROOT.rglob("*.md"))
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

def is_external(link: str) -> bool:
    return link.startswith("http://") or link.startswith("https://") or link.startswith("mailto:")

def main() -> int:
    errors = []
    for md in MD_FILES:
      text = md.read_text(encoding="utf-8")
      for _, link in LINK_RE.findall(text):
        if is_external(link) or link.startswith("#"):
          continue
        target = (md.parent / link).resolve()
        if not target.exists():
          errors.append(f"{md.relative_to(ROOT)} -> {link}")
    if errors:
      print("Broken local markdown links:")
      for err in errors:
        print(f"- {err}")
      return 1
    print("No broken local markdown links found.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
