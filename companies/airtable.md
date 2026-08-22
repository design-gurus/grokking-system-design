# Airtable: system design interview

> How Airtable actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Airtable runs it.** Expect a requirement to be added partway through, because candidates report the mid-design change as a deliberate pattern, and adapting without restarting is part of the grade. Design can appear in several onsite rounds of 45 to 60 minutes, tailored to your domain: backend candidates get storage and sync problems, frontend candidates get rendering and state problems. The unusual core is that the schema is user data, so fields cannot be hardcoded as database columns and structure changes must not require migrations.

## Signature questions

- Design a collaborative spreadsheet-database
- Design real-time sync for many editors of the same table
- Make a 100,000 row table fast in the browser
- Design a formula engine that recomputes only the affected cells
- Design permissions and sharing across bases, workspaces, and collaborator roles

## What interviewers probe

- Whether the data model supports user-defined fields, types, and views as data
- Whether every editor converges to the same final state, including ordering a field deletion against edits to that field
- Whether the design stays fast at large row counts, with clients loading a window of rows instead of everything
- How you react to the added constraint: what changes, what survives, and which option you rejected

## Prepare

- Patterns to review: [long polling websockets sse](../patterns/long-polling-websockets-sse.md), [consistency models](../patterns/consistency-models.md), [database indexing](../patterns/database-indexing.md), [caching](../patterns/caching.md), [sharding partitioning](../patterns/sharding-partitioning.md)
- Practice questions: [Design google docs](../questions/design-google-docs.md), [Design collaborative whiteboard](../questions/design-collaborative-whiteboard.md)
- Full company guide: [Airtable system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-airtable-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
