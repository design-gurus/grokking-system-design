# Deel: system design interview

> How Deel actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Deel runs it.** Design is folded into the technical interview alongside live coding, not run as a separate whiteboard round for every candidate. The problems follow the product: paying contractors and running payroll across more than 150 countries, through many banks and payment providers, so per-country configuration and partner failure are assumed rather than optional. A design built on one currency, one rule set, and reliable providers gets found out in the follow-ups, and senior candidates report more design depth and more probing.

## Signature questions

- Design a payout system that pays thousands of contractors in different currencies
- Design a monthly payroll run that executes across many countries
- Design an integration platform that syncs with providers through APIs and webhooks
- Design contract and payment history storage so every change is traceable

## What interviewers probe

- A double-entry ledger as the source of truth, with balances computed rather than stored and edited
- The payout modeled as a state machine, with an idempotency key on every provider call
- Reconciliation against provider reports, and the words audit trail given a place in the diagram
- Structured, time-boxed answers with version-one cuts named early, since coding shares the session

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [outbox pattern](../patterns/outbox-pattern.md), [event sourcing cqrs](../patterns/event-sourcing-cqrs.md), [distributed transactions](../patterns/distributed-transactions.md), [circuit breaker](../patterns/circuit-breaker.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md), [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md), [Design api gateway](../questions/design-api-gateway.md)
- Full company guide: [Deel system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-deel-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
