# Design a rate limiter

> A service that limits how many requests a client can make in a time window, shared across a fleet of servers.

## 1. Requirements

**Functional**
- Allow or reject a request based on a client's recent request count.
- Configurable rules (per user, per API key, per endpoint).
- Return a clear response when limited (HTTP 429).

**Non-functional**
- Low latency (it sits on every request).
- Accurate enough, without being a bottleneck.
- Works across many servers (distributed).

## 2. Algorithm choice

This builds directly on the [rate limiting pattern](../patterns/rate-limiting.md). Token bucket is the common default because it allows short bursts while capping the sustained rate. Sliding window counter is a good choice when you need smoother accuracy.

## 3. Where it runs

- At the API gateway or load balancer for a first line of defense.
- Optionally per service for finer rules.

## 4. The hard part: distributed counters

A single server's in-memory counter does not work across a fleet, because each server sees only its own traffic. Options:

| Approach | How | Trade-off |
|----------|-----|-----------|
| Centralized store (Redis) | All servers read and update shared counters atomically | Accurate, but adds a network round trip and a dependency |
| Local plus sync | Each server limits locally, periodically reconciling | Lower latency, approximate global limit |

Use atomic operations (for example Redis INCR with expiry, or Lua scripts) to avoid race conditions when many servers update the same counter.

## 5. Deep dive

- Storing state: counters keyed by client id and window, with TTLs so old windows expire.
- Failure mode: if the limiter store is down, decide fail-open (allow traffic) or fail-closed (reject), based on whether availability or protection matters more.
- Response: return 429 with a Retry-After header so clients back off.

## 6. Bottlenecks and trade-offs

- Accuracy vs latency: centralized is accurate but slower; local is fast but approximate.
- The counter store can become a hot spot; shard counters by client.

## Go deeper

- Read more (free): [How to Design a Rate Limiter](https://www.designgurus.io/blog/grokking-rate-limiters)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)