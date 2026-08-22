# Grafana Labs: system design interview

> How Grafana Labs actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Grafana Labs runs it.** Every box in your diagram needs a number attached to it: the company calls the exercise non abstract system design, and an estimate that is wrong but reasoned scores while a design with no arithmetic does not. Expect one design interview and expect the problem to come from observability: metrics storage, log aggregation and search, alerting, or the query and dashboard layer. High cardinality is where naive designs fail, so per tenant series limits, dropping expensive labels, and pre aggregation should come from you rather than from a hint.

## Signature questions

- Design a metrics storage system ingesting ten million samples per second
- Design log aggregation and search at large scale
- Design an alerting pipeline that evaluates rules for many tenants
- Design the query and dashboard layer, including fan out and caching

## What interviewers probe

- Whether your numbers are reasonable and you can defend each one with simple arithmetic
- Trade offs stated plainly: memory against cost, freshness against query speed, index size against query time
- Designing for failure from the start, including replica placement across zones
- Cardinality control: per tenant limits enforced at ingest and reported back to the customer

## Prepare

- Patterns to review: [sharding partitioning](../patterns/sharding-partitioning.md), [replication](../patterns/replication.md), [caching](../patterns/caching.md), [rate limiting](../patterns/rate-limiting.md), [database indexing](../patterns/database-indexing.md)
- Practice questions: [Design metrics monitoring](../questions/design-metrics-monitoring.md), [Design ad click aggregator](../questions/design-ad-click-aggregator.md), [Design distributed cache](../questions/design-distributed-cache.md), [Design notification system](../questions/design-notification-system.md)
- Full company guide: [Grafana Labs system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-grafana-labs-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
