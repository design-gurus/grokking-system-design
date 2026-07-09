# PayPal: system design interview

> How PayPal actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How PayPal runs it.** Classic distributed-systems prompts steered by follow-ups into money-grade territory: idempotent payment processing, ledger consistency, reconciliation, and fraud-check placement in the transaction path.

## Signature questions

- Design a payment processing pipeline with exactly-once effects on a ledger
- Design fraud screening inside the authorization window
- Design reconciliation against external processors

## What interviewers probe

- Idempotency and retry semantics everywhere money moves
- Audit trails as first-class outputs
- Communication and reasoning weighted over algorithmic difficulty

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [message queues](../patterns/message-queues.md), [consistency models](../patterns/consistency-models.md), [write ahead log](../patterns/write-ahead-log.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md)
- Full company guide: [PayPal system design interview](https://www.designgurus.io/answers/detail/what-are-the-top-system-design-interview-questions-for-paypal-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
