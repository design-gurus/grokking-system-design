# Stripe: system design interview

> How Stripe actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Stripe runs it.** API contracts and data models weigh more than boxes and arrows: a rigorous interface with a modest architecture beats the reverse. Money-grade correctness (idempotency, delivery semantics, reconciliation) is probed in nearly every loop.

## Signature questions

- Design a rate limiter with graceful behavior under load
- Design a metrics service: high-throughput ingestion, time-series storage, a clean query API
- Design webhook delivery to millions of flaky external endpoints
- Design a distributed LRU cache or an APM system

## What interviewers probe

- Contract before boxes: endpoints, error semantics, idempotency keys early
- Data-model rigor: schemas whose invariants prevent illegal states
- "At-least-once plus idempotent consumers" said with the reasons attached

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [rate limiting](../patterns/rate-limiting.md), [message queues](../patterns/message-queues.md), [api gateway](../patterns/api-gateway.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md), [Design rate limiter](../questions/design-rate-limiter.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md)
- Full company guide: [Stripe system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-stripe-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
