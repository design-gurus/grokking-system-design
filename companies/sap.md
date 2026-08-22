# SAP: system design interview

> How SAP actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How SAP runs it.** Multi-tenancy is the lens on almost every follow-up question, and interviewers push on each shared cache and shared queue to find where one customer's data could leak into another's. Candidates report design questions mainly in senior interviews and project discussions rather than as a fixed round at every level, so the same preparation also carries the project deep dive. Correctness beats speed here: a slow invoice is annoying, a wrong invoice is a disaster, and saying that trade-off out loud is part of the answer.

## Signature questions

- Design a multi-tenant SaaS service used by thousands of customer companies
- Design an integration between a cloud service and an on-premise system
- Design a reporting and analytics pipeline over business transactions
- Design a multi-step approval workflow with humans in the middle
- Design an order flow where a record can never be left half written

## What interviewers probe

- Data separation thinking, including the tenant filter applied automatically at the data layer
- Noisy neighbor control through per-tenant rate limits, quotas, and pool placement
- Privacy and audit awareness, such as deletion requirements and a record of administrative actions
- Clean interfaces and versioning, since these systems must change without breaking their callers

## Prepare

- Patterns to review: [sharding partitioning](../patterns/sharding-partitioning.md), [rate limiting](../patterns/rate-limiting.md), [distributed transactions](../patterns/distributed-transactions.md), [consistency models](../patterns/consistency-models.md), [outbox pattern](../patterns/outbox-pattern.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md), [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md), [Design api gateway](../questions/design-api-gateway.md)
- Full company guide: [SAP system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-sap-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
