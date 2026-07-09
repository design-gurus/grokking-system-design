# Waymo: system design interview

> How Waymo actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Waymo runs it.** Two altitudes: on-vehicle low-level design (traffic-signal state machines, in-vehicle pub-sub, sensor scene graphs) where unknown-state honesty is graded, and fleet-scale infrastructure where the simulation platform (billions of tested miles) is the company's safety case in executable form.

## Signature questions

- LLD: an in-vehicle pub-sub broker with bounded latency and priority lanes
- LLD: a sensor scene graph tracking objects with explicit unknown states
- Design the scenario simulation platform: deterministic replay, results cached by input tuple, regression gates
- Design fleet telemetry with incident-reconstruction completeness

## What interviewers probe

- Determinism and replay instincts: versioned everything, seeded randomness
- Hard-edged latency: cycle deadlines, not p99 targets, on-vehicle
- Validation as architecture: "how do you know it works" answered structurally

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [write ahead log](../patterns/write-ahead-log.md), [consistency models](../patterns/consistency-models.md), [heartbeats](../patterns/heartbeats.md)
- Practice questions: [Design metrics monitoring](../questions/design-metrics-monitoring.md), [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md)
- Full company guide: [Waymo system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-waymo-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
