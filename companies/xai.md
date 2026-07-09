# xAI: system design interview

> How xAI actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How xAI runs it.** Nearly every round except the hiring manager conversation involves coding, design, or practical infrastructure, and the boundary blurs: a design conversation can turn into "now implement that component." First-principles derivation beats recited reference architectures.

## Signature questions

- Design a multi-level API rate limiter (per-user, per-key, global): the most-reported prompt, often crossing into implementation
- Design a follower push-notification system with celebrity hot spots
- Design recoverable iterators or stateful components that checkpoint and resume after failure
- Infrastructure with a training flavor: job scheduling and health-checking across large GPU fleets

## What interviewers probe

- Implementation credibility: every box on the diagram should have a code-level sketch behind it
- Failure handling as a first-class concern: checkpointing, retries, idempotency before being asked
- Speed: a working end-to-end design in about 15 minutes, then depth

## Prepare

- Patterns to review: [rate limiting](../patterns/rate-limiting.md), [idempotency](../patterns/idempotency.md), [heartbeats](../patterns/heartbeats.md), [write ahead log](../patterns/write-ahead-log.md)
- Practice questions: [Design rate limiter](../questions/design-rate-limiter.md), [Design notification system](../questions/design-notification-system.md)
- Full company guide: [xAI system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-xai-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
