# Setup and Run

## Basic use
1. Connect GPT and/or Codex to the repo.
2. Ask it to read AGENTS.md and the current docs.
3. If the project is still undefined, have it ask what should be built.
4. Have it update the source-of-truth docs before major implementation.

## Foundation checks
Run:

```bash
python3 scripts/create_project_docs.py
python3 scripts/check_doc_links.py
python3 scripts/validate_foundation.py
```
