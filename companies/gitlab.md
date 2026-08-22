# GitLab: system design interview

> How GitLab actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How GitLab runs it.** Design often has no room of its own: it surfaces inside the technical and leadership rounds at senior and staff level, as an open discussion rather than one fixed prompt. Topics track the product directly, so repositories, CI/CD job scheduling, webhook delivery, and merge request processing all appear, and candidates report SQL depth on queries and indexes. Proposing the simplest version one first is treated as a strength here, not as a gap.

## Signature questions

- Design a CI pipeline system
- Design a webhook delivery service for slow or dead customer servers
- Design Git repository hosting for millions of repositories
- Design merge request diff and check processing for busy projects
- Design the indexes for a heavy relational workload

## What interviewers probe

- Announced structure: requirements, scale estimate, high-level parts, then depth where asked
- Practicality, meaning the simplest design first with clear iteration after it
- Named costs for every choice: more latency, more money, or more operational work
- Relational database depth, since GitLab leans on SQL and tests it

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [heartbeats](../patterns/heartbeats.md), [idempotency](../patterns/idempotency.md), [database indexing](../patterns/database-indexing.md), [replication](../patterns/replication.md)
- Practice questions: [Design code deployment system](../questions/design-code-deployment-system.md), [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md), [Design notification system](../questions/design-notification-system.md), [Design distributed message queue](../questions/design-distributed-message-queue.md)
- Full company guide: [GitLab system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-gitlab-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
