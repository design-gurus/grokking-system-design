# Epic Games: system design interview

> How Epic Games actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Epic Games runs it.** Game constraints govern the hour: players notice delay above roughly 100 milliseconds and state updates arrive many times per second, so a design that works for a web shop can fail for a shooter. The round sits inside a final loop of four to six interviews, about an hour with one or two interviewers at a whiteboard or shared document, covering leaderboards, multiplayer sessions, matchmaking, and live events. Object-oriented design also appears, sometimes tied to Unreal Engine concepts, so be ready to sketch classes for a small game system and explain each choice.

## Signature questions

- Design a global top-K leaderboard
- Design the multiplayer session service that assigns players to servers
- Design skill-based matchmaking with low wait times
- Design a live in-game event pushed to millions of connected clients
- Design a game telemetry pipeline for designers to query

## What interviewers probe

- Requirement gathering and scale numbers in the opening five minutes, since that section sets the tone of the round
- Separating write ingestion from read ranking, with an in-memory ranking store over a durable history
- Sharding by region or league, plus caching the first page of ranks that absorbs most reads
- The failure ending, graded heavily: a shard dies, and you rebuild memory from durable storage

## Prepare

- Patterns to review: [sharding partitioning](../patterns/sharding-partitioning.md), [caching](../patterns/caching.md), [message queues](../patterns/message-queues.md), [heartbeats](../patterns/heartbeats.md), [long polling websockets sse](../patterns/long-polling-websockets-sse.md)
- Practice questions: [Design gaming leaderboard](../questions/design-gaming-leaderboard.md), [Design live comment streaming](../questions/design-live-comment-streaming.md), [Design notification system](../questions/design-notification-system.md)
- Full company guide: [Epic Games system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-epic-games-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
