# Atlassian: system design interview

> How Atlassian actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Atlassian runs it.** SaaS collaboration at multi-tenant scale: Jira and Confluence shape the prompts, so tenancy, permissions, search over user content, and integrations recur. The craft register favors practical, buildable designs over exotic architecture.

## Signature questions

- Design an issue tracker: workflows, permissions, and search at tenant scale
- Design real-time collaborative editing for documents
- Design a webhooks and integrations platform

## What interviewers probe

- Multi-tenancy and permission models as first constraints
- Search over user-defined content
- Practical evolution: designs that absorb requirement changes

## Prepare

- Patterns to review: [sharding partitioning](../patterns/sharding-partitioning.md), [database indexing](../patterns/database-indexing.md), [message queues](../patterns/message-queues.md), [caching](../patterns/caching.md)
- Practice questions: [Design google docs](../questions/design-google-docs.md), [Design notification system](../questions/design-notification-system.md)
- Full company guide: [Atlassian system design interview](https://www.designgurus.io/answers/detail/what-are-the-top-system-design-interview-questions-for-atlassian-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
