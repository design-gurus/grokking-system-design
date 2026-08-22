# Redis: system design interview

> How Redis actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Redis runs it.** A design that scales but never mentions memory or latency misses what the company actually sells, because the managed business rests on low latency, high availability, and predictable memory use. Candidates report one or two design interviews in the process, sometimes with a senior R&D leader. Questions split three ways: build something on top of the database (rate limiter, leaderboard, session store, cache), design a piece of the database itself (replication, resharding, eviction), or operate it (node failure, upgrading a cluster without downtime).

## Signature questions

- Design a distributed cache with sub-millisecond reads
- Design a rate limiter
- Design a gaming leaderboard
- Design a replication protocol or cluster resharding
- Design an eviction policy for a node that is out of memory

## What interviewers probe

- Requirements first: data size, read and write rates, latency targets, all confirmed aloud
- Trade-offs named without prompting, including that eviction keeps the cache fast but makes it lossy
- Failure thinking across a server, a network link, and a whole zone, with automatic promotion of a replica
- Hot key handling and closing on monitoring: hit rate, memory use, replication delay

## Prepare

- Patterns to review: [consistent hashing](../patterns/consistent-hashing.md), [caching](../patterns/caching.md), [replication](../patterns/replication.md), [leader election](../patterns/leader-election.md), [quorum](../patterns/quorum.md)
- Practice questions: [Design distributed cache](../questions/design-distributed-cache.md), [Design rate limiter](../questions/design-rate-limiter.md), [Design gaming leaderboard](../questions/design-gaming-leaderboard.md)
- Full company guide: [Redis system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-redis-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
