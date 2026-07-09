# Scale AI: system design interview

> How Scale AI actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Scale AI runs it.** The distinctive dimension is humans as a component in the architecture: slow, expensive, variable, and indispensable. Strong candidates treat annotators as an API with hours of latency, per-person error rates, and real hourly cost, and design quality as a measured output.

## Signature questions

- Design a data annotation pipeline delivering labeled data at a contracted quality SLA
- Design an LLM evaluation system mixing human raters with model-based judges
- Design quality control for a labeling workforce: gold-standard seeding, rater reputation, collusion detection
- Design an RLHF preference-collection system at scale

## What interviewers probe

- Quality as architecture: consensus, gold tasks, tiered review, each with its cost stated
- Human-in-the-loop economics: tasks x minutes x raters x dollars, computed aloud
- Measurement rigor: inter-annotator agreement, drift detection, auditable SLA claims

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [idempotency](../patterns/idempotency.md), [batch vs stream processing](../patterns/batch-vs-stream-processing.md)
- Practice questions: [Design ad click aggregator](../questions/design-ad-click-aggregator.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md)
- Full company guide: [Scale AI system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-scale-ai-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
