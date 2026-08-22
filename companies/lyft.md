# Lyft: system design interview

> How Lyft actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Lyft runs it.** Different parts of one design get different guarantees, and saying so is the senior signal: locations may be slightly stale, trip and payment records may never be wrong. The round runs about 60 minutes on real-time marketplace problems taken from the product, matching, location tracking, pricing, payments, and trip history, on a whiteboard or a laptop. Interviewers expect requirements, an API, a data model, then scale and failure, in that order.

## Signature questions

- Design ride matching between riders and nearby drivers
- Design driver location tracking and nearby search
- Design surge pricing that is fair and explainable
- Design payments and driver payouts
- Design trip history storage and state transitions

## What interviewers probe

- Requirements before boxes: who uses the system and how often, asked before anything is drawn
- A named API and data model early, showing the move from idea to concrete plan
- The write load from constant driver location updates, not only rider read paths
- Failure thinking: what breaks mid ride, what the user sees, and how one region's failure stays local

## Prepare

- Patterns to review: [sharding partitioning](../patterns/sharding-partitioning.md), [replication](../patterns/replication.md), [consistency models](../patterns/consistency-models.md), [caching](../patterns/caching.md), [idempotency](../patterns/idempotency.md)
- Practice questions: [Design uber](../questions/design-uber.md), [Design proximity service](../questions/design-proximity-service.md), [Design payment system](../questions/design-payment-system.md)
- Full company guide: [Lyft system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-lyft-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
