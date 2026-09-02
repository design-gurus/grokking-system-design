# Distributed locking

> Mutual exclusion across machines: make sure at most one process in the whole system does a thing at a time.

## What it is

A mutex protects a resource within one process; a distributed lock protects it across a fleet. Typical uses: stop two workers from processing the same job, prevent double-booking of a seat or a room, guard a migration so it runs once. The lock lives in a shared store that all contenders can see.

## How it works

Acquire by atomically creating a record that expires:

```
SET lock:room-42 owner=worker-7 NX PX 30000   -- only if not exists, TTL 30s
  OK      -> you hold the lock, do the work, then DEL (only if still owner)
  nil     -> someone else holds it, back off and retry
```

The TTL is the crucial part: without it, a crashed lock holder deadlocks the system forever. With it, you get the opposite hazard, which is the whole difficulty of the topic.

## The safety problem

If the holder pauses (GC, slow I/O) past the TTL, the lock expires and a second worker acquires it: now two workers believe they hold the lock. Defenses, in increasing strength:

- **Check ownership on release** so you never delete someone else's lock.
- **Fencing tokens**: the lock service issues an increasing number with each grant; the protected resource rejects operations with a stale token. This is the only defense that actually prevents corruption.
- **Consensus-backed locks** (ZooKeeper, etcd, Chubby): the lock is replicated via a [quorum](quorum.md), with sessions kept alive by [heartbeats](heartbeats.md), rather than depending on a single Redis node's clock.

## Choosing an implementation

| Option | Character |
|--------|-----------|
| Redis `SET NX` + TTL | Simple and fast; fine when the lock is an efficiency optimization, not a correctness guarantee |
| ZooKeeper / etcd ephemeral nodes | Stronger: quorum-replicated, session-based, ordered; use when correctness depends on the lock |
| Database row lock or unique constraint | Often the simplest correct answer if all contenders already share the database |

Before reaching for a lock, ask whether [idempotency](idempotency.md) or a unique constraint solves the problem without one. Locks are a last resort, not a default.

## How to talk about it in an interview

Give the Redis one-liner for the simple case, then immediately name its weakness (expiry during a pause means two holders) and the fix (fencing tokens, or a consensus-backed store when correctness is at stake). That progression, simple tool then its failure mode then the hardened version, is exactly the senior signal.

## Go deeper

- Related deep dive: [Chubby, Google's distributed lock service](../deep-dives/chubby-distributed-locking.md)
- Every pattern, in depth: [System Design Patterns](https://www.designgurus.io/course/system-design-patterns?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=patterns-distributed-locking)
- For harder, distributed-systems depth: [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=patterns-distributed-locking)