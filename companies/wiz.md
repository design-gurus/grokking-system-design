# Wiz: system design interview

> How Wiz actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Wiz runs it.** Cloud-security platform design: agentless ingestion living inside cloud providers' API rate limits, the Security Graph (hundreds of millions of nodes per tenant), and toxic-combination detection as incremental multi-hop pattern queries. The stakes inversion: customer data is a map of their weaknesses.

## Signature questions

- Design the cloud inventory pipeline: snapshot plus event planes, rate-limit budgets spent like money
- Design the Security Graph with interactive attack-path queries
- Design risk prioritization that beats alert fatigue

## What interviewers probe

- API-constrained ingestion realism
- Graph thinking at scale: precompute versus traversal, incremental updates
- Security-of-the-security-platform instincts: credentials, isolation, the platform as target

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [rate limiting](../patterns/rate-limiting.md), [sharding partitioning](../patterns/sharding-partitioning.md), [database indexing](../patterns/database-indexing.md)
- Practice questions: [Design web crawler](../questions/design-web-crawler.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md)
- Full company guide: [Wiz system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-wiz-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
