# Capital One: system design interview

> How Capital One actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Capital One runs it.** Bank-grade constraints on cloud-native architecture: security, compliance, consistency, and fault tolerance are explicit evaluation criteria, and the business dimension surfaces even in design rounds (this is the company that gives engineers case interviews).

## Signature questions

- Design real-time fraud scoring inside the authorization window, with model governance (shadow scoring, staged ramp)
- Design a credit decisioning system where adverse-action explainability constrains the architecture
- Design payment processing with regulator-walkable audit trails

## What interviewers probe

- Security and compliance as design inputs: encryption, tokenization, retention, stated in a structured pass
- Consistency partitioned deliberately: strong where money lives, relaxed where it does not
- The business dial: thresholds and tradeoffs priced in dollars

## Prepare

- Patterns to review: [idempotency](../patterns/idempotency.md), [message queues](../patterns/message-queues.md), [consistency models](../patterns/consistency-models.md), [database indexing](../patterns/database-indexing.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md), [Design ad click aggregator](../questions/design-ad-click-aggregator.md)
- Full company guide: [Capital One system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-capital-one-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
