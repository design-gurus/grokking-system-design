# Dropbox: system design interview

> How Dropbox actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Dropbox runs it.** Simplicity is graded directly, so adding queues, caches, and shards without a stated reason counts against you in this one hour round. Questions come from the product space: sync, cheap storage, sharing and permissions, metadata for billions of files, and deduplication, and candidates report a senior bar close to staff level elsewhere. Candidates also report a steady rhythm of about five minutes on requirements, ten on the high-level design, twenty-five on deep dives, and ten on failure cases, with the clock managed by you rather than the interviewer.

## Signature questions

- Design a file sync service
- Design storage for very large amounts of data at low cost
- Design folder sharing and permissions that stay correct everywhere
- Design a metadata store for billions of files, versions, and folder structures
- Design deduplication so identical content is stored only once

## What interviewers probe

- Structure: requirements, scale estimates, high-level design, then depth on one or two parts
- The simplest design that meets the requirements, with each added component justified
- Conflict handling for offline edits, never a claim that conflicts cannot happen
- Failure modes named first, such as hot metadata partitions, huge shared folders, and notification storms after an outage

## Prepare

- Patterns to review: [checksums](../patterns/checksums.md), [sharding partitioning](../patterns/sharding-partitioning.md), [consistency models](../patterns/consistency-models.md), [replication](../patterns/replication.md), [long polling websockets sse](../patterns/long-polling-websockets-sse.md)
- Practice questions: [Design dropbox](../questions/design-dropbox.md), [Design amazon s3](../questions/design-amazon-s3.md), [Design notification system](../questions/design-notification-system.md)
- Full company guide: [Dropbox system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-dropbox-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
