# Samsara: system design interview

> How Samsara actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Samsara runs it.** Sensor streams set the agenda: hundreds of thousands of devices reporting every few seconds, data arriving late and out of order, and gateways that drop off the network in a tunnel. Public reports of exact questions are limited, so prepare shapes that match the product: telemetry ingestion, time-series storage, alerting, offline sync, and video clip retrieval. The round is typically 45 to 60 minutes on a virtual whiteboard for mid-level and senior candidates, and the interviewer will push on write-per-second arithmetic, replay after a consumer crash, and freshness versus cost.

## Signature questions

- Design a fleet tracking system for hundreds of thousands of vehicles
- Design an alerting pipeline for events such as harsh braking or a temperature limit
- Design time-series storage for device telemetry
- Design sync for devices that go offline and upload late
- Design video clip retrieval from dash cameras without uploading everything

## What interviewers probe

- Scale arithmetic done out loud, since writes per second drive every storage and queue choice
- Failure thinking: a crashed consumer or a downed region, answered with the queue plus replay
- Device reality most candidates skip: network loss, duplicate messages, clock differences, battery limits
- Trade-off honesty, such as stating that dashboards may lag a few seconds and why that is acceptable

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [batch vs stream processing](../patterns/batch-vs-stream-processing.md), [sharding partitioning](../patterns/sharding-partitioning.md), [caching](../patterns/caching.md), [rate limiting](../patterns/rate-limiting.md)
- Practice questions: [Design uber](../questions/design-uber.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md), [Design ad click aggregator](../questions/design-ad-click-aggregator.md), [Design notification system](../questions/design-notification-system.md)
- Full company guide: [Samsara system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-samsara-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
