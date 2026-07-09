# Notion: system design interview

> How Notion actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Notion runs it.** Grounded in its real architecture: everything is a block, users define their own schemas, and offline-first sync must never lose a user's writing. One of the few loops where OT/CRDT literacy is explicitly rewarded, at a practical level.

## Signature questions

- Design a collaborative block-based editor with conflict resolution and offline support
- Design Notion-style databases: user-defined schemas, views, relations and rollups, kept fast
- Design hierarchical permissions with inheritance at read scale

## What interviewers probe

- Data-model-first thinking: blocks as the foundation everything derives from
- The flexibility-performance tension: what degrades and how you bound it
- Offline-first semantics with the never-lose-writing invariant

## Prepare

- Patterns to review: [consistency models](../patterns/consistency-models.md), [database indexing](../patterns/database-indexing.md), [caching](../patterns/caching.md), [sharding partitioning](../patterns/sharding-partitioning.md)
- Practice questions: [Design google docs](../questions/design-google-docs.md), [Design collaborative whiteboard](../questions/design-collaborative-whiteboard.md)
- Full company guide: [Notion system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-notion-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
