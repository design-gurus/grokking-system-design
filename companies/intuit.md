# Intuit: system design interview

> How Intuit actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Intuit runs it.** Money-grade correctness at consumer scale with the industry's most extreme seasonal burst: tax season compresses a year of traffic into weeks. The GenOS era adds AI-assistant prompts where validation and trust machinery are the design.

## Signature questions

- Design the tax-filing pipeline for deadline day: never-lose-work invariants, acceptance decoupled from government transmission
- Design document ingestion and extraction with confidence-routed automation
- Design an AI financial assistant with segment-gated accuracy and hard lines (it drafts, never files)

## What interviewers probe

- Seasonal-burst arithmetic: pre-scaled capacity on a known calendar
- Calculation determinism: same inputs, same tax outcome, versioned by rule-year
- Privacy architecture for the most sensitive consumer documents

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [idempotency](../patterns/idempotency.md), [write ahead log](../patterns/write-ahead-log.md), [consistency models](../patterns/consistency-models.md)
- Practice questions: [Design payment system](../questions/design-payment-system.md), [Design flash sale system](../questions/design-flash-sale-system.md)
- Full company guide: [Intuit system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-intuit-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
