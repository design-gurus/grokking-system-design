# JPMorgan Chase: system design interview

> How JPMorgan Chase actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How JPMorgan Chase runs it.** Losing a record or paying a customer twice counts as a failed round, so consistency and auditability outrank scale numbers in the grading. Design appears mainly at senior levels as one Superday session of about 45 to 60 minutes, with shorter design and data modeling questions inside technical screens. Legacy systems are a fair topic: designing clean interfaces around old parts reads as experience, while assuming a rewrite does not.

## Signature questions

- Design a payment transfer system between accounts
- Design the transaction ledger that serves as the store of record
- Design a fraud and risk service that scores transactions in real time
- Design the backend for a mobile banking feature used by millions

## What interviewers probe

- Idempotency keys on every transfer, and returning the original result when a retry reuses a key
- Modeling money as debit and credit entries rather than storing a balance directly
- Behavior when the service dies mid-transfer or an external system never responds, including pending states and reconciliation
- Whether you justify a consistency choice instead of saying eventual consistency is fine

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [distributed transactions](../patterns/distributed-transactions.md), [event sourcing cqrs](../patterns/event-sourcing-cqrs.md), [outbox pattern](../patterns/outbox-pattern.md), [consistency models](../patterns/consistency-models.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md), [Design api gateway](../questions/design-api-gateway.md), [Design rate limiter](../questions/design-rate-limiter.md)
- Full company guide: [JPMorgan Chase system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-jpmorgan-chase-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
