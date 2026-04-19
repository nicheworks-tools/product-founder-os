# AGENTS.md

## Mission

This repo is a product-building operating system.

The goal is not to generate random docs.
The goal is not to generate random code.
The goal is to move from user intent -> definition -> plan -> implementation -> change handling -> completion,
while keeping the repository coherent and honest.

## First move rule

If the user has not clearly stated what they want to build, ask first.

Do not start with arbitrary implementation guesses.
Do not fill files with generic filler just to look productive.

## Source of truth order

When determining what the product currently is, use this priority order:

1. latest explicit user instruction
2. `docs/05-execution/change-requests.md`
3. `docs/05-execution/decision-log.md`
4. `docs/02-spec/*`
5. `docs/01-definition/*`
6. `docs/04-planning/*`

If drift exists, repair the docs before pretending the product direction is clear.

## Required baseline before major build work

Before major implementation work, the repo should have usable forms of:

- `docs/00-intake/project-seed.md`
- `docs/01-definition/product-brief.md`
- `docs/02-spec/functional-spec.md`
- `docs/04-planning/roadmap.md`
- `docs/04-planning/task-backlog.md`
- `docs/04-planning/current-sprint.md`
- `docs/06-quality/done-definition.md`

If they are missing or too weak to guide implementation, improve them first.

## Planning rules

- Break work into milestones.
- Keep backlog items specific and scoped.
- Keep `current-sprint.md` small and current.
- A task is not done because code merely exists.
- Use acceptance criteria, not intuition.

## Change handling rules

When the user adds, removes, or changes a requirement:

1. record it in `docs/05-execution/change-requests.md`
2. update the affected source-of-truth docs
3. update roadmap / backlog / sprint as needed
4. only then shift implementation direction

No silent pivots.

## Execution rules

- Keep `docs/05-execution/worklog.md` current enough for later recovery.
- Keep `decision-log.md` honest.
- Write assumptions down.
- Write blockers down.
- Write unverified status as unverified.
- Prefer updating existing source-of-truth docs over creating ad-hoc extras.

## Completion rules

Do not claim “complete” unless:

- the result matches the current spec
- the acceptance criteria are satisfied
- known issues are documented
- remaining next steps are explicit if anything is still open

## Repo hygiene

- Keep headings stable.
- Reduce stale content aggressively.
- Avoid duplicate plans across files.
- Keep docs useful, not decorative.

## When improving this repo itself

If you are editing `product-founder-os` itself:

- keep README, SKILL.md, and AGENTS.md aligned
- preserve the core flow: ask -> define -> plan -> build -> adjust -> ship
- prefer quality of guidance over quantity of files
- do not bloat the repo with low-value placeholders
