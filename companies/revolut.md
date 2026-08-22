# Revolut: system design interview

> How Revolut actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Revolut runs it.** Design is graded in two places: an architecture review of your own take-home project, about 45 to 60 minutes, and for senior candidates a separate discussion about money systems. Candidates report a take-home such as a small currency exchange API built in four to eight hours, where the reviewer asks why you chose your design, how it survives ten times the load, and where it fails. The dedicated round draws on multi-currency accounts, card payments, and exchange, where correctness comes before scale.

## Signature questions

- Design a currency exchange system with live rates
- Design a multi-currency ledger as the source of truth
- Design quote locking so the displayed rate matches the executed rate
- Design a transfer that survives partial failure between two accounts
- Defend your take-home architecture at ten times the load

## What interviewers probe

- Whether the ledger is the source of truth, with faster read copies built from it
- Failure modes named before the interviewer asks: rate provider down, ledger write timeout, expired quote, two confirmations for one quote
- Idempotency keys that make a retried confirmation a no-op
- A place in the design for regulatory checks that delay or stop a transaction, plus daily reconciliation

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [caching](../patterns/caching.md), [distributed transactions](../patterns/distributed-transactions.md), [consistency models](../patterns/consistency-models.md), [event sourcing cqrs](../patterns/event-sourcing-cqrs.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md), [Design stock exchange](../questions/design-stock-exchange.md), [Design distributed cache](../questions/design-distributed-cache.md)
- Full company guide: [Revolut system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-revolut-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
