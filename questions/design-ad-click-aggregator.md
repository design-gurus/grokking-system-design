# Design an ad click aggregator

> Ingest a massive stream of ad click events and produce accurate, near real-time aggregated counts.

## Requirements

- Ingest a very high volume of click events.
- Aggregate counts by ad, campaign, and time window.
- Near real-time dashboards plus accurate totals for billing.
- Handle duplicate and late events.

## Key ideas

- Events flow into a durable log (a [Kafka](../deep-dives/kafka-distributed-messaging.md) style stream), then a stream processor aggregates them in time windows.
- Two paths: a fast approximate path for live dashboards, and a slower exact path for billing-grade totals (a lambda-architecture idea).
- Deduplication: clicks carry an id so retries and duplicates are not double-counted (idempotency).
- Late events: windows allow a grace period before they are finalized.

## Go deeper

- Quick, focused prep: [System Design Interview Crash Course](https://www.designgurus.io/course/system-design-interview-crash-course)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)