#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED = [
    "docs/00-intake/project-seed.md",
    "docs/01-definition/product-brief.md",
    "docs/02-spec/functional-spec.md",
    "docs/04-planning/roadmap.md",
    "docs/04-planning/task-backlog.md",
    "docs/04-planning/current-sprint.md",
    "docs/06-quality/done-definition.md",
]

def main() -> int:
    missing = []
    for rel in REQUIRED:
        path = ROOT / rel
        if not path.exists():
            missing.append(rel)
    if missing:
        print("Missing required docs:")
        for item in missing:
            print(f"- {item}")
        return 1
    print("All required baseline docs exist.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
