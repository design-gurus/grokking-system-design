# Brex: system design interview

> How Brex actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Brex runs it.** A stated company value, complexity is the enemy, shows up in the grading: a simple design defended with reasons scores better than extra services added to look impressive. Questions come from spend management: card authorization at low latency, transaction ledgers, fraud pipelines, and rate limited payment APIs. Candidates report heavy attention to consistency, exactly once behavior, and what happens when a dependency dies, so close with metrics and alerts.

## Signature questions

- Design a card authorization system that approves or declines in about a second
- Design a transaction ledger with full auditability
- Design a fraud detection pipeline over transaction streams
- Design a payment API with rate limits and safe retries
- Design a rewards or pay later service

## What interviewers probe

- A strongly consistent balance check while analytics is allowed to update later, stated as a deliberate choice
- Idempotency keys so a retried authorization cannot approve twice
- Fallback behavior when the fraud scorer is slow: a simple rule instead of a timeout
- Operational detail: decision latency, decline rate, and the alert that fires when the fraud service fails

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [consistency models](../patterns/consistency-models.md), [rate limiting](../patterns/rate-limiting.md), [event sourcing cqrs](../patterns/event-sourcing-cqrs.md), [circuit breaker](../patterns/circuit-breaker.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md), [Design rate limiter](../questions/design-rate-limiter.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md)
- Full company guide: [Brex system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-brex-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
