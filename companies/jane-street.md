# Jane Street: system design interview

> How Jane Street actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Jane Street runs it.** There is usually no classic whiteboard design round: systems thinking is evaluated inside long, evolving coding problems (the input no longer fits in memory; updates are now concurrent; the process can crash) and in design-review-style depth conversations for senior candidates.

## Signature questions

- Requirement shocks inside coding rounds: scale, concurrency, and crash-recovery imposed on your working solution
- Senior depth conversations: a design review of the best system you have built
- Domain-adjacent discussion: determinism, replayability, and state-machine replication

## What interviewers probe

- Correctness before scale: invariants and edge semantics first
- Recognizing when a problem wants the deterministic-state-machine-plus-log shape
- Calibrated honesty about your own systems' weaknesses

## Prepare

- Patterns to review: [write ahead log](../patterns/write-ahead-log.md), [consistency models](../patterns/consistency-models.md), [idempotency](../patterns/idempotency.md)
- Practice questions: [Design stock exchange](../questions/design-stock-exchange.md), [Design unique id generator](../questions/design-unique-id-generator.md)
- Full company guide: [Jane Street system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-jane-street-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
