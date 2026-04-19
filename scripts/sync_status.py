#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FILES = [
    "docs/00-intake/project-seed.md",
    "docs/01-definition/product-brief.md",
    "docs/02-spec/functional-spec.md",
    "docs/04-planning/roadmap.md",
    "docs/04-planning/task-backlog.md",
    "docs/04-planning/current-sprint.md",
    "docs/06-quality/done-definition.md",
]

def summarize(path: Path) -> str:
    text = path.read_text(encoding="utf-8").strip()
    first_nonempty = next((line for line in text.splitlines() if line.strip()), "(empty)")
    return first_nonempty[:120]

def main() -> int:
    print("product-founder-os status\n")
    for rel in FILES:
        path = ROOT / rel
        if path.exists():
            print(f"[OK] {rel}")
            print(f"     {summarize(path)}")
        else:
            print(f"[MISSING] {rel}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
