# Toast: system design interview

> How Toast actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Toast runs it.** Restaurant internet failing during dinner service is the constraint the whole round is built on, so terminals must keep taking orders offline and sync later without losing or doubling anything. One reported follow-up captures the round: what happens when two terminals edit the same open check while offline, where last-write-wins fails and item-level merging is the answer. It runs about 60 minutes on a virtual whiteboard inside a five-interview onsite, and candidates report interviewers who know and probe CRDTs and vector clocks by name.

## Signature questions

- Design an offline-capable point of sale system
- Design payment processing for restaurants under card industry security rules
- Design online ordering with menu synchronization
- Design a kitchen display pipeline that stays ordered during a rush

## What interviewers probe

- Constraint-first thinking: failure conditions named before any boxes are drawn
- Money exactness: an exactly-once story on every payment path, with idempotency keys said early
- Conflict resolution between terminals, including why last-write-wins loses items
- Reconciliation across terminal, cloud, and processor records as the proof nothing was lost

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [event sourcing cqrs](../patterns/event-sourcing-cqrs.md), [logical clocks](../patterns/logical-clocks.md), [message queues](../patterns/message-queues.md), [consistency models](../patterns/consistency-models.md)
- Practice questions: [Design dropbox](../questions/design-dropbox.md), [Design google docs](../questions/design-google-docs.md), [Design payment system](../questions/design-payment-system.md), [Design food delivery](../questions/design-food-delivery.md)
- Full company guide: [Toast system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-toast-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
