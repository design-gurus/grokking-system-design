# Nubank: system design interview

> How Nubank actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Nubank runs it.** Immutable data and functional programming are public parts of the engineering culture, and they change what a good answer sounds like: append new facts, keep history, and derive read models from them. The round is an architecture discussion on an online whiteboard such as Miro or Excalidraw, covering ledgers, payment flows, fraud detection, and scaling reads, with Kafka often assumed as the transport. Expect the ACID versus BASE question and answer it per flow rather than once for the whole system.

## Signature questions

- Design real time fraud detection for card transactions
- Design the ledger that holds account balances and movements
- Design a payment flow with retries that cannot double pay
- Design read models that serve balances and statements to millions of app users

## What interviewers probe

- Consistency chosen per flow and said out loud: ACID for the ledger, BASE for notifications
- The tradeoff between missed fraud and false blocks, stated before the design choices follow from it
- Feature freshness: the delay from event to feature store, and the alert when it grows
- Idempotent decisions per transaction identifier, an append-only audit log, and an open fallback when the scoring service fails

## Prepare

- Patterns to review: [event sourcing cqrs](../patterns/event-sourcing-cqrs.md), [idempotency](../patterns/idempotency.md), [consistency models](../patterns/consistency-models.md), [message queues](../patterns/message-queues.md), [batch vs stream processing](../patterns/batch-vs-stream-processing.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md), [Design ad click aggregator](../questions/design-ad-click-aggregator.md), [Design model evaluation pipeline](../questions/design-model-evaluation-pipeline.md)
- Full company guide: [Nubank system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-nubank-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
