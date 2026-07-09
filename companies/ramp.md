# Ramp: system design interview

> How Ramp actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Ramp runs it.** Pragmatic fintech: card authorization under a hard latency budget, receipt matching as confidence-tiered automation, and integration-heavy systems where banks and accounting APIs are treated as unreliable dependencies. The build-order close ("what ships first with two engineers?") is effectively guaranteed.

## Signature questions

- Design the card authorization flow: precomputed controls, time-boxed risk scoring, fail-open/closed per check type
- Design receipt matching: fuzzy matching with confidence routing between auto-match and human review
- Design the accounting-sync layer that never double-books

## What interviewers probe

- Latency-critical money decisions with explicit budgets
- Confidence-tiered automation as the house pattern
- Reconciliation as where correctness actually lives

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [caching](../patterns/caching.md), [message queues](../patterns/message-queues.md), [circuit breaker](../patterns/circuit-breaker.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md)
- Full company guide: [Ramp system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-ramp-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
