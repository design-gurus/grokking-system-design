# Chime: system design interview

> How Chime actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Chime runs it.** Mobile check deposit is the reported signature question, and it is not a photo upload problem: the hard part is clearing that takes days, the state machine around it, and money correctness. The round runs about an hour inside the virtual onsite and also covers money movement, buy now pay later, notifications, and fraud checks. Interviewers listen for a ledger mindset, pending states with clear member communication, and honest answers about what the member sees during each failure.

## Signature questions

- Design mobile check deposit where clearing takes days and can fail
- Design money movement between accounts that happens exactly once
- Design a buy now, pay later installment service
- Design deposit, low balance, and suspicious activity alerts
- Design fraud scoring that does not slow normal transactions

## What interviewers probe

- Balances derived from an append-only ledger instead of one balance column that concurrent updates corrupt
- A deposit record with explicit states (submitted, under review, pending, cleared, rejected) that every later step moves forward
- Duplicate detection when the same check is photographed twice, possibly from different devices
- The pending experience: what the member sees while waiting, and what support can answer about where the money is

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [event sourcing cqrs](../patterns/event-sourcing-cqrs.md), [message queues](../patterns/message-queues.md), [consistency models](../patterns/consistency-models.md), [distributed transactions](../patterns/distributed-transactions.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md), [Design notification system](../questions/design-notification-system.md), [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md)
- Full company guide: [Chime system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-chime-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
