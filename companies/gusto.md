# Gusto: system design interview

> How Gusto actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Gusto runs it.** Every reported question is a money-correctness question: a payroll calculation engine with tax rules that differ by state, a direct deposit flow where bank transfers come back days later, and an audit log that cannot be altered. The round runs about 45 to 60 minutes on a virtual whiteboard, and senior and staff candidates report a second, deeper architecture round. Scale is not the target here, since the customer base is hundreds of thousands of businesses, so spend the minutes on data integrity, retries, and recovery.

## Signature questions

- Design a payroll calculation engine with per-state tax rules
- Design a direct deposit system that handles bank returns and reversals
- Design an immutable audit log for financial transactions
- Design the API for a multi-step onboarding flow that saves progress across sessions

## What interviewers probe

- Correctness under failure: a server dying mid-run must never lose or double a payment
- Idempotency keys on every payment operation, reported as the single most important point
- The ledger as source of truth rather than the job queue, plus daily reconciliation against bank records
- Trade-off reasoning said out loud, and a collaborative style that invites the interviewer in

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [write ahead log](../patterns/write-ahead-log.md), [event sourcing cqrs](../patterns/event-sourcing-cqrs.md), [message queues](../patterns/message-queues.md), [distributed transactions](../patterns/distributed-transactions.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md), [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md), [Design notification system](../questions/design-notification-system.md)
- Full company guide: [Gusto system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-gusto-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
