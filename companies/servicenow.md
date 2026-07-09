# ServiceNow: system design interview

> How ServiceNow actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How ServiceNow runs it.** Enterprise platform design almost nobody practices: thousands of customers configure everything, workflows run for months, and every design must survive customer customization and platform upgrades simultaneously.

## Signature questions

- Design an approval workflow engine: durable state machines, idempotent steps, definitions changing mid-flight
- Design a multi-tenant SaaS service: isolation strategy, noisy neighbors, per-tenant limits
- Design notification or audit systems for a configurable platform

## What interviewers probe

- Multi-tenancy as the first constraint, not a closing note
- Configurability through constrained extension points rather than arbitrary code
- Upgrade safety: versioned contracts, backward compatibility as discipline

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [write ahead log](../patterns/write-ahead-log.md), [idempotency](../patterns/idempotency.md), [sharding partitioning](../patterns/sharding-partitioning.md)
- Practice questions: [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md), [Design notification system](../questions/design-notification-system.md)
- Full company guide: [ServiceNow system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-servicenow-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
