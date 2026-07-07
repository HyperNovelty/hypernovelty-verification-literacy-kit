# Hypernovelty Verification Literacy Kit

Practical mini-labs and lightweight templates for learning how to verify AI outputs, agent claims, source trails, and recovery boundaries.

This repository is intentionally small, synthetic, and public-safe. It is for education and workflow design, not legal, financial, medical, cybersecurity, or procurement advice.

## What is in this kit?

- A 20-minute **AI Literacy Failure-Mode Mini-Lab** with synthetic examples.
- Templates for checking whether an AI-made artifact is still supported by its evidence.
- A lite harness-audit card for reviewing agent/tool runs without exposing private traces.
- Recovery and calibration templates for teams that want inspectable workflows before automation touches public, paid, or sensitive surfaces.

## Why this exists

AI literacy is not just prompt-writing. People need practice distinguishing:

1. accurate answers,
2. plausible but wrong answers,
3. incomplete answers,
4. unsupported claims,
5. tool runs that completed a task but crossed a boundary.

The goal is to make verification practical enough to teach, repeat, and improve.

## Start here

1. Open `labs/ai-literacy-failure-mode-mini-lab/README.md`.
2. Run the 20-minute lab with a learner or team.
3. Use the answer key to discuss what changed in confidence after checking evidence.
4. Try one template from `templates/` on a harmless synthetic example.

## Repository map

```text
labs/
  ai-literacy-failure-mode-mini-lab/
    README.md
    worksheet.md
    answer-key.md
templates/
  claim-drift-harness-card.md
  harness-audit-lite-card.md
  agent-recovery-plan-card.md
  forecast-calibration-receipt.md
examples/
  synthetic/
    claim-drift-example.md
    harness-audit-lite-example.md
```

## Validation

Run the local validator and smoke test before public review:

```bash
python3 scripts/validate_kit.py
python3 -m unittest discover -s tests
```

## Public-safety boundary

This repo should not contain:

- private source material,
- expert/source relationship records,
- account workflows,
- credentials or secrets,
- automode logs,
- private dashboards,
- client or publication operations,
- public-action approvals,
- real legal/financial/medical/trading recommendations.

Use synthetic examples unless you have explicit rights and a strong reason to publish a real one.

## Suggested use

- Schools and adult-learning workshops.
- Team onboarding for AI-assisted research/writing.
- Source-backed publishing workflows.
- Lightweight agent/tool-run retrospectives.
- Public-interest AI literacy exercises.

## License

MIT. See `LICENSE`.
