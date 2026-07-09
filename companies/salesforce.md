# Salesforce: system design interview

> How Salesforce actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Salesforce runs it.** Enterprise CRM scale: multi-tenant data platforms, configurable objects and workflows, and integration surfaces, with trust (the company's first value) shaping how data-handling questions are probed.

## Signature questions

- Design a multi-tenant object platform with customer-defined fields
- Design an integration/API layer with per-tenant limits
- Design reporting over large tenant datasets without hurting transactional paths

## What interviewers probe

- Tenant isolation and fairness
- Flexible-schema performance tradeoffs
- Trust and data stewardship raised unprompted

## Prepare

- Patterns to review: [sharding partitioning](../patterns/sharding-partitioning.md), [database indexing](../patterns/database-indexing.md), [rate limiting](../patterns/rate-limiting.md), [caching](../patterns/caching.md)
- Practice questions: [Design api gateway](../questions/design-api-gateway.md), [Design ad click aggregator](../questions/design-ad-click-aggregator.md)
- Full company guide: [Salesforce system design interview](https://www.designgurus.io/answers/detail/what-are-the-top-system-design-interview-questions-for-salesforce-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
