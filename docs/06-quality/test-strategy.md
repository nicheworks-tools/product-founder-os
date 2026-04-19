# Test Strategy

## Current strategy
This repo is primarily a markdown-and-structure product, so its first quality layer is repository validation rather than application runtime testing.

## Validation layers

### Foundation existence
Check that baseline operating docs exist.

### Link integrity
Check markdown local links for breakage.

### Public-quality validation
Check for:
- placeholder phrases in core docs
- malformed markdown code fences
- weak or missing baseline files

### Manual review
Before public release, review:
- README clarity
- internal coherence
- example usefulness
- obvious placeholder leakage

## Minimum rule
Never claim a test ran unless it actually ran.
