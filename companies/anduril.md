# Anduril: system design interview

> How Anduril actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Anduril runs it.** The cloud playbook partially inverts: the network is the least reliable component, so designs run edge-first with store-and-forward sync, legible degradation, and different delivery guarantees for telemetry versus commands. Prompts arrive deliberately vague; requirements-extraction is graded.

## Signature questions

- Design a sensor fusion pipeline that survives a ten-minute link drop
- Design fleet coordination for autonomous assets with intermittent connectivity
- Design command-and-control with exactly-once semantics over unreliable links

## What interviewers probe

- Degraded-operation design as the default, stated first
- Delivery semantics with judgment: telemetry tolerates loss, commands tolerate neither loss nor duplication
- The operator's view: confident-but-stale is the worst possible output

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [idempotency](../patterns/idempotency.md), [heartbeats](../patterns/heartbeats.md), [consistency models](../patterns/consistency-models.md)
- Practice questions: [Design metrics monitoring](../questions/design-metrics-monitoring.md), [Design reminder alert system](../questions/design-reminder-alert-system.md)
- Full company guide: [Anduril system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-anduril-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
