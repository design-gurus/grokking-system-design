# Wise: system design interview

> How Wise actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Wise runs it.** Correctness outranks raw scale, and the problem usually arrives as a business case, mostly for senior roles: a transfer flow, a ledger, or an integration with unreliable bank partners. The format is collaborative, with the interviewer questioning your choices as you make them, so practice designing aloud because a silent five minutes counts against you. Three facts belong in any answer here: operations must not be lost or duplicated, external banks are slow and sometimes unavailable, and regulators require a complete audit trail.

## Signature questions

- Design an international money transfer flow across two currencies
- Design a double entry ledger for money movements
- Design an integration with unreliable bank partners
- Design retries and reconciliation for failed payout steps

## What interviewers probe

- Whether you ask about failure cases before designing the success case
- Correctness tools named without prompting: idempotency, transactions, reconciliation
- The transfer modeled as a state machine (created, funded, converted, paid out, failed) with each change recorded with a time and a reason
- The customer view: what the sender sees while a partner bank is slow, plus monitoring for transfers stuck in one state

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [message queues](../patterns/message-queues.md), [distributed transactions](../patterns/distributed-transactions.md), [event sourcing cqrs](../patterns/event-sourcing-cqrs.md), [circuit breaker](../patterns/circuit-breaker.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md), [Design distributed message queue](../questions/design-distributed-message-queue.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md)
- Full company guide: [Wise system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-wise-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
