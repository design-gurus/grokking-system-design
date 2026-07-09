# SpaceX: system design interview

> How SpaceX actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How SpaceX runs it.** Consequence-driven reliability across an unusual range: telemetry pipelines where bandwidth is set by physics, command paths where wrong is unrecoverable, and constellation-scale infrastructure (Starlink is plausibly the largest distributed system with physics in the loop ever built).

## Signature questions

- Design a launch telemetry pipeline: priority under shrinking bandwidth, store-and-forward through blackouts, dual real-time/archival paths
- Design command-and-control with exactly-once semantics over unreliable links
- Design constellation management: update rollouts that cannot brick assets, autonomous out-of-contact behavior

## What interviewers probe

- Bandwidth and physics budgeting: what fits in an eight-minute pass
- Loss-intolerance where it matters: every frame around an anomaly, always recoverable
- Time discipline: source timestamps, clock sync limits, ordering

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [write ahead log](../patterns/write-ahead-log.md), [checksums](../patterns/checksums.md), [heartbeats](../patterns/heartbeats.md)
- Practice questions: [Design metrics monitoring](../questions/design-metrics-monitoring.md), [Design code deployment system](../questions/design-code-deployment-system.md)
- Full company guide: [SpaceX system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-spacex-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
