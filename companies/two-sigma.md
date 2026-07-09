# Two Sigma: system design interview

> How Two Sigma actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Two Sigma runs it.** The signature format is design-and-implementation: architect a small system, then build it as working code within the session, so designs must be buildable in an hour by you. Senior conversations add research-platform territory where point-in-time correctness rules.

## Signature questions

- Design and implement an in-memory time-series store, a scheduler, or a rate limiter, live
- Design a backtesting platform: no future data leaking into the past, deterministic replay, results cached by input tuple
- Design a feature store serving research (point-in-time) and production (low-latency) consistently

## What interviewers probe

- Buildable-design judgment: scope the architecture to the hour
- Point-in-time discipline: as-of semantics, no lookahead, corrections explicit
- Precise, calibrated communication throughout

## Prepare

- Patterns to review: [caching](../patterns/caching.md), [database indexing](../patterns/database-indexing.md), [write ahead log](../patterns/write-ahead-log.md)
- Practice questions: [Design distributed cache](../questions/design-distributed-cache.md), [Design rate limiter](../questions/design-rate-limiter.md)
- Full company guide: [Two Sigma system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-two-sigma-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
