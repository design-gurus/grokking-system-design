# Affirm: system design interview

> How Affirm actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Affirm runs it.** For senior roles, candidates report this round carries the most weight in the loop, and every question comes from the lending domain. Prompts cover installment engines, repayment pipelines against partner bank APIs, transaction ledgers, fraud detection, and experimentation platforms. The deepest questioning lands on consistency, auditing, and retry behavior, including a reported question where the bank API only accepts requests during a few hours each day.

## Signature questions

- Design a loan repayment flow when the bank API is open only a few hours a day
- Design an installment engine that schedules and collects payments
- Design a double entry transaction ledger
- Design real time fraud detection on payment streams
- Design an experimentation platform for A/B testing

## What interviewers probe

- Double entry thinking, where every money movement has a matching source and destination
- What a timed out bank call does on retry, and which failures land in a dead letter queue for human review
- The consistency split: strict for balances, bounded and visible delay for analytics
- Reconciliation against partner records, plus metrics such as queue depth, window utilization, and mismatch count

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [message queues](../patterns/message-queues.md), [consistency models](../patterns/consistency-models.md), [distributed transactions](../patterns/distributed-transactions.md), [event sourcing cqrs](../patterns/event-sourcing-cqrs.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md), [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md), [Design distributed message queue](../questions/design-distributed-message-queue.md)
- Full company guide: [Affirm system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-affirm-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
