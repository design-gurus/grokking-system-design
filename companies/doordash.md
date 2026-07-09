# DoorDash: system design interview

> How DoorDash actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How DoorDash runs it.** Three-sided logistics at street level: consumers, Dashers, and merchants, with dispatch, ETAs, and pay systems as the native territory. Rounds run 60 to 75 minutes with domain deep-dives for senior candidates, and product intuition for delivery problems is explicitly evaluated.

## Signature questions

- Design order assignment and dispatch: which Dasher gets which order, weighing distance, batching, and earnings
- Design real-time ETA computation through the physical pipeline (restaurant prep, travel, handoff)
- Design Dasher pay: layered rules turned into a correct, auditable calculation

## What interviewers probe

- Three-sided tradeoffs: consumer latency versus Dasher efficiency versus merchant success
- Messy real-world rules translated into clean, testable logic
- Marketplace health metrics: completion rate, lateness, acceptance

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [sharding partitioning](../patterns/sharding-partitioning.md), [idempotency](../patterns/idempotency.md)
- Practice questions: [Design uber](../questions/design-uber.md), [Design flash sale system](../questions/design-flash-sale-system.md)
- Full company guide: [DoorDash system design interview](https://www.designgurus.io/answers/detail/what-are-the-top-system-design-interview-questions-for-doordash-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
