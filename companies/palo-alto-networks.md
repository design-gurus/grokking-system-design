# Palo Alto Networks: system design interview

> How Palo Alto Networks actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Palo Alto Networks runs it.** Networking is tested harder here than at most product companies, so TCP, TLS, and load balancing follow-ups arrive inside whatever design you are drawing. The hour long round takes its themes from security products: receiving millions of events per second, processing them as a stream, and delivering alerts without duplicates. There is no published question list, and candidates report design rounds for mid-level and senior roles inside the technical interview stage.

## Signature questions

- Design a log ingestion pipeline for millions of security events per second
- Design an alerting system that turns raw events into a small number of useful alerts
- Design a rate limiter
- Design a service that keeps working when a machine or a region fails

## What interviewers probe

- Clarifying volume and delay budgets before proposing any components
- Rough math on events per second and stored bytes
- Queues, retries, and duplicate handling placed where they belong, with at-least-once delivery justified
- Transport and encryption follow-ups answered fluently

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [batch vs stream processing](../patterns/batch-vs-stream-processing.md), [idempotency](../patterns/idempotency.md), [rate limiting](../patterns/rate-limiting.md), [sharding partitioning](../patterns/sharding-partitioning.md)
- Practice questions: [Design metrics monitoring](../questions/design-metrics-monitoring.md), [Design notification system](../questions/design-notification-system.md), [Design distributed message queue](../questions/design-distributed-message-queue.md), [Design rate limiter](../questions/design-rate-limiter.md)
- Full company guide: [Palo Alto Networks system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-palo-alto-networks-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
