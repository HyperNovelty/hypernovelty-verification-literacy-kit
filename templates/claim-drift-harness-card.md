# Claim Drift Harness Card

Status: TEMPLATE / LOCAL_ONLY / REVIEW_GATE_REQUIRED

Use when a content or review artifact may no longer be supported by its source, evidence, implementation, or validation record.

## 1. Artifact path

- Artifact:
- Version/date:
- Owner:
- Intended use: internal / review / public draft / published / other.

## 2. Main claim under test

Write one claim the artifact appears to make.

> Claim:

## 3. Source / evidence path

- Primary source(s):
- Source ledger / notes:
- Implementation / output file:
- Prior QA receipt:

## 4. Evidence snippet

Paste the smallest source quote or file excerpt that should support the claim.

> Evidence:

## 5. AI or agent transformation

What changed between the source and the artifact?

- Source to summary:
- Summary to claim:
- Claim to artifact:
- Artifact to public/review surface:

## 6. Executable / checkable output

| Check | Command / method | Result |
|---|---|---|
| File exists |  |  |
| Source link works |  |  |
| Required phrase present |  |  |
| Forbidden/internal marker absent |  |  |
| Syntax/render check |  |  |

## 7. Drift risk assessment

| Drift type | Risk | Diagnosis |
|---|---|---|
| Semantic drift | Low/Med/High | Does the artifact preserve the source meaning? |
| Experimental drift | Low/Med/High | Does the executable/checkable work still test the stated intervention? |
| Mechanistic drift | Low/Med/High | Does the evidence show why the result happened, not just that it happened? |
| Boundary drift | Low/Med/High | Did private/gated/internal material leak into public-use claims? |

## 8. Unsupported leap / repair needed

- Unsupported leap:
- Repair:
- Source recheck needed:
- Voice/public gate needed:

## 9. Human-only decision

What only a human reviewer can approve:

- [ ] Public use.
- [ ] Expert/private material use.
- [ ] Forecast or result resolution.
- [ ] Product/launch claim.

## 10. Final status

- `safe_local`
- `needs_source_recheck`
- `needs_voice_gate`
- `needs_browser_review`
- `not_public`
- `discard`

## Explicit non-actions

This card does not publish, deploy, send, spend, trade, upload, or approve itself.
