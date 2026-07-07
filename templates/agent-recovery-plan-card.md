# Agent Recovery Plan Card

Status: TEMPLATE / LOCAL_ONLY / REVIEW_GATE_REQUIRED

Use when an agent, automation, workflow, or content pipeline can touch money, content, records, source claims, accounts, public surfaces, or user trust.

## 1. Agent / workflow name

- Name:
- Owner / reviewer:
- Date opened:
- Related source/post/project:

## 2. What the agent is allowed to do

- Allowed actions:
- Allowed tools/surfaces:
- Allowed data/source folders:
- Allowed spending/account/public-action scope: `none` unless separately approved.

## 3. What the agent must not do

- Public posting/deploy:
- Email/outreach/social:
- Account/DNS/payment/credential changes:
- Wallet/broker/trading actions:
- Private-source export:
- Other protected resources:

## 4. Stop / slow-down triggers

| Trigger | Severity | Required response | Human reviewer |
|---|---|---|---|
| Unauthorized tool/resource requested | P0 | Stop; write incident note |  |
| Source claim unsupported | P1 | Mark needs_source_recheck |  |
| Public-copy gate missing | P1 | Mark draft only |  |
| Cost/spend/account surface appears | P0 | Stop before action |  |

## 5. Recovery path

- Safe rollback/revert command or file restore path:
- Last known-good artifact:
- Logs/receipts location:
- How to reconstruct the run:
- How to notify the reviewer:

## 6. Evidence that recovery works

- Dry-run/test performed:
- File existence/link checks:
- Browser/API smoke if applicable:
- Known gap:

## 7. Human-only decision

- [ ] Publish/deploy/send.
- [ ] Account/payment/DNS/credential change.
- [ ] Use private/expert material publicly.
- [ ] Treat the workflow as approved for repeat use.

## 8. Final disposition

- `safe_local`
- `needs_repair`
- `needs_source_recheck`
- `needs_voice_gate`
- `needs_browser_review`
- `blocked_on_human_approval`
- `discard`

## Explicit non-actions

This card does not publish, deploy, send, spend, trade, change accounts, change credentials, or approve itself.
