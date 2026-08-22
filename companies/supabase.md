# Supabase: system design interview

> How Supabase actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Supabase runs it.** Deep Postgres knowledge counts more here than at most companies, because each prompt is a platform piece bolted onto a real database: write ahead log streaming, row level security, and connection pooling. Question types follow the product: multi tenant hosting, a realtime change feed, permissions, and file storage with access rules. Security has to appear in your design before anyone asks for it, and tenant isolation with predictable cost is graded first.

## Signature questions

- Design a realtime change feed on Postgres
- Design a multi tenant database platform with strict isolation
- Design a connection pooling layer for serverless clients
- Design permissions using row level security
- Design file storage with per-object access rules

## What interviewers probe

- Multi tenant thinking: isolation, cost per tenant, and noisy neighbor control
- Authorization applied before delivery rather than after, which is probed hardest
- Recovery through a saved log position, plus buffer limits for subscribers that fall behind
- Early numbers: changes per second, subscribers per project, bytes per message

## Prepare

- Patterns to review: [write ahead log](../patterns/write-ahead-log.md), [replication](../patterns/replication.md), [long polling websockets sse](../patterns/long-polling-websockets-sse.md), [backpressure](../patterns/backpressure.md), [sharding partitioning](../patterns/sharding-partitioning.md)
- Practice questions: [Design live comment streaming](../questions/design-live-comment-streaming.md), [Design dropbox](../questions/design-dropbox.md), [Design collaborative whiteboard](../questions/design-collaborative-whiteboard.md)
- Full company guide: [Supabase system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-supabase-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
