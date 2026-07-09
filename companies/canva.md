# Canva: system design interview

> How Canva actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Canva runs it.** Consumer-scale creative infrastructure: real-time collaboration, media processing pipelines, template search for hundreds of millions of users, and export rendering, with async-work-plus-waiting-human as the recurring shape.

## Signature questions

- Design the export/render service: deterministic rendering, queue fairness, the Monday-morning burst
- Design the media processing pipeline: transcode fleets, progress surfacing, AI enhancements
- Design template search and recommendation with seasonal surges

## What interviewers probe

- Async pipelines with honest progress for the watching user
- One-renderer determinism: exports must match the editor exactly
- Cacheable-versus-personalized layers in consumer search

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [cdn](../patterns/cdn.md), [caching](../patterns/caching.md), [idempotency](../patterns/idempotency.md)
- Practice questions: [Design youtube](../questions/design-youtube.md), [Design typeahead autocomplete](../questions/design-typeahead-autocomplete.md)
- Full company guide: [Canva system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-canva-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
