# Apple: system design interview

> How Apple actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Apple runs it.** Loops are team-designed rather than centrally standardized, so design rounds vary widely: consumer-scale services, on-device and privacy-conscious architectures, and media delivery all appear. Craft and precise tradeoff reasoning carry weight everywhere.

## Signature questions

- Design a photo or media sync service across devices
- Design a messaging or notification system at consumer scale
- Design services where privacy and on-device processing shape the architecture

## What interviewers probe

- Privacy as a design input, not a disclaimer
- Detail-level correctness: sync conflicts, offline behavior, battery and bandwidth budgets
- Clean, defensible tradeoffs over encyclopedic coverage

## Prepare

- Patterns to review: [consistency models](../patterns/consistency-models.md), [caching](../patterns/caching.md), [cdn](../patterns/cdn.md)
- Practice questions: [Design dropbox](../questions/design-dropbox.md), [Design whatsapp](../questions/design-whatsapp.md)
- Full company guide: [Apple system design interview](https://www.designgurus.io/answers/detail/what-are-the-top-system-design-interview-questions-for-apple-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
