# Klarna: system design interview

> How Klarna actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Klarna runs it.** The recurring test is a checkout that never double charges, at millions of purchases a day. One live discussion inside the onsite covers checkout payment flows, fraud and risk scoring that fits the checkout time budget, ledger consistency, and observability across many microservices. Candidates report deep questions on idempotency, reconciliation, retries, regional failure, security, and auditability, so mention encryption of stored card data and access controls before being asked.

## Signature questions

- Design a checkout payment flow that charges exactly once
- Design duplicate charge prevention under network timeouts
- Design a real time fraud and risk scoring system
- Design a ledger and reporting pipeline
- Design observability across many payment microservices

## What interviewers probe

- Handling an unknown state: query the provider before retrying when the answer arrives late
- Strong consistency for money and bounded delay for dashboards, stated as a deliberate tradeoff
- Fraud checks that score risk without slowing honest checkouts
- Region failure: the alert that fires, and how another region takes the traffic

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [consistency models](../patterns/consistency-models.md), [message queues](../patterns/message-queues.md), [replication](../patterns/replication.md), [event sourcing cqrs](../patterns/event-sourcing-cqrs.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md), [Design amazon shopping cart](../questions/design-amazon-shopping-cart.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md)
- Full company guide: [Klarna system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-klarna-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
