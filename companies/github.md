# GitHub: system design interview

> How GitHub actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How GitHub runs it.** Notably domain-specific: developer infrastructure rather than generic social prompts, with the platform's traffic shape (extreme read dominance punctuated by webhook, CI, and notification storms when a repo goes viral) driving the probes.

## Signature questions

- Design GitHub Actions as a CI/CD platform: ephemeral runners, fair scheduling, live log streaming, abuse containment
- Design a notification system across repos, issues, and PRs with digesting and preferences
- Design webhook delivery to millions of flaky external endpoints
- Design a rate limiter for a public API developers program against

## What interviewers probe

- Fan-out explosions tamed: queues as shock absorbers, per-tenant isolation
- API design for developers: pagination under concurrent writes, idempotent mutations, honest headers
- Fairness and abuse: one tenant queuing 50k jobs, crypto-mining on free runners

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [rate limiting](../patterns/rate-limiting.md), [idempotency](../patterns/idempotency.md), [api gateway](../patterns/api-gateway.md)
- Practice questions: [Design code deployment system](../questions/design-code-deployment-system.md), [Design notification system](../questions/design-notification-system.md), [Design rate limiter](../questions/design-rate-limiter.md)
- Full company guide: [GitHub system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-github-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
