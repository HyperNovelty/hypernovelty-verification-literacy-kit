# Synthetic Example: Claim Drift Harness Card

Status: SYNTHETIC_EXAMPLE / PUBLIC_SAFE

## 1. Artifact path

- Artifact: `examples/synthetic/mock-school-ai-policy-summary.md`
- Version/date: synthetic v1
- Owner: example reviewer
- Intended use: training

## 2. Main claim under test

> The school AI assistant may grade homework automatically if teachers review final grades.

## 3. Source / evidence path

- Primary source: synthetic policy excerpt in the mini-lab worksheet.
- Source ledger / notes: `labs/ai-literacy-failure-mode-mini-lab/worksheet.md`

## 4. Evidence snippet

> It must not assign grades.

## 5. AI or agent transformation

- Source to summary: AI converted policy into a short summary.
- Summary to claim: AI added automatic grading permission.
- Claim to artifact: The false permission appeared in a proposed parent note.

## 6. Executable / checkable output

| Check | Command / method | Result |
|---|---|---|
| Source phrase present | Search worksheet for “must not assign grades” | Present |
| Artifact claim conflicts | Compare “may grade” vs “must not assign grades” | Conflict |

## 7. Drift risk assessment

| Drift type | Risk | Diagnosis |
|---|---|---|
| Semantic drift | High | The claim reverses a restriction in the source. |
| Experimental drift | N/A | No executable test. |
| Mechanistic drift | N/A | No mechanism claimed. |
| Boundary drift | Medium | A training summary could become unsafe if reused as policy copy. |

## 8. Unsupported leap / repair needed

- Unsupported leap: automatic grading permission.
- Repair: replace with “the assistant must not assign grades.”

## 9. Human-only decision

- [ ] Approve corrected parent-facing policy note.

## 10. Final status

`needs_source_recheck`
