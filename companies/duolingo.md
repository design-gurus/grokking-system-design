# Duolingo: system design interview

> How Duolingo actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Duolingo runs it.** Prompts come straight from the product's own machinery: streaks, reminder timing, the experimentation platform, and the models that pick each exercise. The round is product-aware on purpose, so what a learner experiences during failure is treated as part of the answer, not an afterthought. Candidates who anchor capacity in consumer rhythms (the global evening wave, the midnight boundary) and end designs at the learner rather than at a system metric read as consumer-experienced.

## Signature questions

- Design the streak system
- Design the reminder and notification timing platform
- Design the experimentation platform
- Design lesson delivery and cross-device progress sync
- Design personalization serving for exercise difficulty

## What interviewers probe

- Idempotent, timezone-safe activity recording, with the stated asymmetry that a wrongly broken streak costs more than a wrongly preserved one
- Consumer write patterns anchored in real rhythms (evening peak, per-timezone midnight evaluation) instead of uniform averages
- Clean experiment surfaces built into the design, since notification timing and streak mechanics both exist to be tested
- Offline-first mobile reality: local progress, sync reconciliation, and a no-lost-work invariant

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [message queues](../patterns/message-queues.md), [sharding partitioning](../patterns/sharding-partitioning.md), [batch vs stream processing](../patterns/batch-vs-stream-processing.md), [caching](../patterns/caching.md)
- Practice questions: [Design notification system](../questions/design-notification-system.md), [Design reminder alert system](../questions/design-reminder-alert-system.md), [Design recommendation system](../questions/design-recommendation-system.md), [Design ad click aggregator](../questions/design-ad-click-aggregator.md)
- Full company guide: [Duolingo system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-duolingo-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
