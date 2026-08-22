# Snyk: system design interview

> How Snyk actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Snyk runs it.** Interviewers listen for one specific insight: a reverse index from package version to the projects that use it, instead of rescanning every project each time a new vulnerability record arrives. Design discussion sits inside senior loops and candidates report it sometimes mixed into the pair programming stage, so it can arrive without a clear round boundary. The problems stay close to the product: scanning pipelines, dependency graphs including transitive packages, and integrations built on APIs and webhooks.

## Signature questions

- Design a dependency vulnerability alert system
- Design a scanning pipeline that runs on every code change and returns results quickly
- Design storage and queries for dependency graphs at scale
- Design the APIs and webhooks for editor and build pipeline integrations

## What interviewers probe

- Whether the design actually matches the scale you stated
- The reverse index insight, or an equivalent that avoids a full rescan
- Failure thinking: retries, duplicate notifications, partial data, and a paused feed catching up
- Naming idempotency before being asked, and explaining trade-offs clearly while drawing

## Prepare

- Patterns to review: [database indexing](../patterns/database-indexing.md), [idempotency](../patterns/idempotency.md), [sharding partitioning](../patterns/sharding-partitioning.md), [message queues](../patterns/message-queues.md), [caching](../patterns/caching.md)
- Practice questions: [Design notification system](../questions/design-notification-system.md), [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md), [Design linkedin connections](../questions/design-linkedin-connections.md)
- Full company guide: [Snyk system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-snyk-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
