# Miro: system design interview

> How Miro actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Miro runs it.** The round happens on a Miro board, so the diagram is graded as communication: labeled arrows and a readable layout count, because the product is the drawing tool. Questions stay inside the collaboration domain, including whiteboard edit sync, live cursors for very large numbers of users, and convergence when two people change the same object. Generic scaling talk does not pass here, and the answer has to engage ordering, conflict handling, and catch-up for clients on poor networks.

## Signature questions

- Design real-time sync for a shared whiteboard with thousands of simultaneous edits
- Design presence and live cursors at large scale
- Design consistent handling when two users resize the same shape at once
- Design event broadcast per board over publish-subscribe
- Design for a sudden jump to hundreds of editors on one board

## What interviewers probe

- Whether updates stay fast at realistic scale, against a target near 100 milliseconds
- Whether all clients converge to identical board state after concurrent edits
- Trade-off reasoning such as CRDTs or OT against per-property last-writer-wins, plus when the simple rule fails
- Persistence and catch-up: an event log with periodic snapshots so a reconnecting client recovers cleanly

## Prepare

- Patterns to review: [long polling websockets sse](../patterns/long-polling-websockets-sse.md), [sharding partitioning](../patterns/sharding-partitioning.md), [leader election](../patterns/leader-election.md), [event sourcing cqrs](../patterns/event-sourcing-cqrs.md), [message queues](../patterns/message-queues.md)
- Practice questions: [Design collaborative whiteboard](../questions/design-collaborative-whiteboard.md), [Design google docs](../questions/design-google-docs.md), [Design live comment streaming](../questions/design-live-comment-streaming.md)
- Full company guide: [Miro system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-miro-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
