# Expedia: system design interview

> How Expedia actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Expedia runs it.** Reported difficulty is easy to medium next to other large tech companies, so clean decomposition and steady narration carry the round more than exotic techniques. It is one interview in the final loop, about 45 minutes, usually on flight or hotel booking, a pricing and availability service, or payments; some candidates report non-travel prompts such as a delivery app, graded the same way. The detail that separates answers is the fare moving between search and booking, and saying plainly that you re-verify it at checkout and show the user the difference.

## Signature questions

- Design a real-time flight booking system
- Design a pricing and availability service under heavy read traffic
- Design a payment processing flow
- Design a delivery app (reported as a non-travel variant)

## What interviewers probe

- Decomposition: can you name the services and their boundaries in the first ten minutes
- Consistency boundaries: strong for seats and payments, eventual for search and reviews
- Caching judgment: where you cache, for how long, and what happens when it is stale
- Failure plans described from the user's side, including serving cached fares marked as estimates

## Prepare

- Patterns to review: [caching](../patterns/caching.md), [idempotency](../patterns/idempotency.md), [distributed locking](../patterns/distributed-locking.md), [consistency models](../patterns/consistency-models.md), [sharding partitioning](../patterns/sharding-partitioning.md)
- Practice questions: [Design hotel reservation](../questions/design-hotel-reservation.md), [Design payment system](../questions/design-payment-system.md), [Design ticketmaster](../questions/design-ticketmaster.md), [Design food delivery](../questions/design-food-delivery.md)
- Full company guide: [Expedia system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-expedia-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
