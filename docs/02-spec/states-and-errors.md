# States and Errors

## States

### undefined
The product does not yet have enough definition to guide implementation safely.

### defining
The core docs are being created or clarified.

### planned
The product has usable definition and an actionable current sprint.

### executing
Implementation or implementation-guided work is underway against the current sprint.

### blocked
A blocker prevents safe continuation and should be recorded explicitly.

### reviewing
The current increment exists, but completion still needs to be checked against acceptance criteria.

### release-ready
The current intended milestone meets its defined completion bar.

## Error cases

### definition drift
The code, docs, and user intent no longer match.

### silent scope change
Requirements changed in conversation, but the source-of-truth docs were not updated.

### fake completion
Work is presented as done without satisfying acceptance criteria.

### doc sprawl
New docs are created instead of maintaining the source-of-truth files.

## Recovery rule
When drift or ambiguity is detected, update the core docs before continuing implementation.
