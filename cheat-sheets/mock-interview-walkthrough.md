# A mock interview, annotated: two candidates, one question

The same question, played twice: once as a borderline no-hire, once as a strong hire. The margin notes mark where signal was earned or lost. Both transcripts are condensed; a real round is 40 to 45 minutes. The question is [design a rate limiter](../questions/design-rate-limiter.md), and the [interview framework](interview-framework.md) is the structure both candidates should be following.

---

## Round 1: Candidate A (borderline no-hire)

**Interviewer:** Design a rate limiter for our public API.

**Candidate A:** Sure. So I would use a token bucket algorithm. Each user gets a bucket with, say, 100 tokens, and tokens refill at a fixed rate. When a request comes in, we take a token; if the bucket is empty we reject with 429.

> Lost signal: jumped straight to a solution with zero clarification. Whose requests are limited (user, API key, IP)? What scale? Is this one service or a shared platform? The first two minutes decide whether the candidate designs the right system.

**Interviewer:** OK. Where does this run?

**Candidate A:** In the API server. We keep a hash map from user id to bucket, and a background thread refills tokens.

**Interviewer:** We have around 200 API servers behind a load balancer.

**Candidate A:** Ah, right. Then the counters need to be shared. I would use Redis, so all servers check Redis before serving a request.

> Lost signal: the interviewer had to surface the distributed problem, and it is the entire problem. Candidate A designed a single-box system for a fleet, then patched it when caught. Interviewers write this down as "needed steering."

**Interviewer:** What exactly is in Redis?

**Candidate A:** A key per user with the token count, and we decrement it on each request.

**Interviewer:** Two requests for the same user hit two API servers at the same time. What happens?

**Candidate A:** Both read the count, both decrement... there could be a race. We could use a lock per user.

> Lost signal twice. The race condition was found by the interviewer, not the candidate; and the first fix reached for a lock, which puts a lock acquisition on every API request. The atomic answer (INCR, or a Lua script doing check-and-decrement in one step) should be the reflex.

**Interviewer:** A lock on every request is expensive. Alternatives?

**Candidate A:** Maybe Redis atomic increment, INCR. Yes, INCR with an expiry would work: count requests per window and reject over the limit.

**Interviewer:** That changes the algorithm from token bucket to fixed windows. Is that OK?

**Candidate A:** It is mostly the same thing.

> Lost signal: it is not the same thing, and hand-waving a known difference (window-boundary bursts: a client can send 2x the limit straddling the boundary) reads as not knowing it. "Fixed window allows boundary bursts; if that matters I would move to sliding window" would have recovered fully.

**Interviewer:** What happens if Redis goes down?

**Candidate A:** We would have Redis replicas, so it should not go down.

> Lost signal: "it will not fail" is never the answer. The question was fail-open vs fail-closed, a one-sentence trade-off Candidate A never named.

**Interviewer's private scorecard:** Knows the standard algorithms by name, coded a reasonable single-node limiter. Needed prompting for distribution, concurrency, and failure. No numbers at any point. Hire at mid-level maybe; not senior.

---

## Round 2: Candidate B (strong hire)

**Interviewer:** Design a rate limiter for our public API.

**Candidate B:** Before I design, three quick questions. What are we limiting on: user id, API key, IP, or all three? Roughly what scale: requests per second across the fleet? And is this inline on the request path, where added latency matters, or advisory?

> Earned signal: three questions, each one changes the design. Note they are batched and fast; clarification is an efficiency exercise, not a stall.

**Interviewer:** API key mostly. Around 300K requests per second at peak, 200 servers. Inline.

**Candidate B:** Inline at 300K RPS means the limiter budget is about a millisecond, and it must not be a single point of failure. Let me state the plan: pick the algorithm, then make it work across 200 servers, then failure modes, and I will finish with what I would monitor. The interesting part is the distributed counter, so I will spend most time there.

> Earned signal: restated constraints as numbers with a derived latency budget, and proposed an agenda. The candidate is now driving; the interviewer is observing.

**Candidate B:** Algorithm: token bucket per API key. It allows short bursts, which public APIs want, and it is two numbers per key: token count and last-refill time. Fixed window counters are cheaper but allow 2x bursts at window boundaries; sliding window log is exact but memory-heavy. Token bucket is the right middle. Default 100 requests per second with burst of 200, configurable per key, because enterprise customers will need custom limits.

> Earned signal: options were named in one breath each, then one was chosen with a reason tied to the product. Compare Candidate A, who named one algorithm and never justified it.

**Candidate B:** Distribution: local counters on each server cannot work alone, since 200 servers each allowing 100 RPS per key is a 200x overshoot. So shared state in Redis: bucket state per key, and the check-and-decrement must be atomic, a Lua script so refill-plus-take is one round trip. Redis at 300K RPS: a single instance handles maybe 100K ops per second, so I shard by API key hash across, say, 4 to 8 instances. Sharding by key keeps each key's state on one shard, so no cross-shard coordination.

> Earned signal: the race condition never happened, because the design was atomic from the first sentence. The shard count came from arithmetic (300K RPS against ~100K ops per instance), not from vibes. This is what [estimation](estimation.md) driving design looks like.

**Interviewer:** What about the extra hop to Redis on every request?

**Candidate B:** Round trip inside a datacenter is a few hundred microseconds, so it fits the budget, but I can cut most calls with a local optimization: each server keeps a small local token allowance per hot key, synced to Redis in the background. That trades accuracy for latency, limits become approximate within a few percent. For a public API that is usually acceptable; for billing-grade enforcement it is not, and I would stay synchronous.

> Earned signal: quantified the cost before optimizing it, and the optimization came with its own trade-off and a rule for when not to use it.

**Interviewer:** Redis shard dies?

**Candidate B:** Decision point: fail-open or fail-closed. For a public API I fail open, serving traffic unprotected briefly beats a self-inflicted outage for every key on that shard, and I would page on it. The exception is if this limiter also protects a fragile downstream, then failing open can melt it, so I would fail open with a conservative local fallback limit. Replicas per shard shrink the window either way.

> Earned signal: the failure question was answered as a trade-off with a recommendation and an exception. That sentence shape ("I chose X, accepting Y, unless Z") is the single most senior-sounding structure in the interview. See [senior vs staff expectations](senior-vs-staff-expectations.md).

**Candidate B:** To close: I would return 429 with Retry-After and rate-limit headers so well-behaved clients back off, and monitor rejection rate per key, Redis latency, and shard hot spots, a celebrity key can hot-spot one shard, and per-key sub-sharding is the escape hatch.

**Interviewer's private scorecard:** Drove the whole session. Numbers at every decision. Concurrency and failure handled before being asked. Knew the local-allowance optimization and, more importantly, when not to use it. Strong senior; would not fight a staff argument.

---

## The difference, in one table

| Moment | Candidate A | Candidate B |
|--------|-------------|-------------|
| First 2 minutes | Named an algorithm | Asked 3 questions, derived a latency budget |
| Distribution | Interviewer raised it | Core of the answer, with shard math |
| Race condition | Found by interviewer; first fix was a lock | Never existed; atomic by construction |
| Failure | "It should not go down" | Fail-open vs fail-closed, with a recommendation |
| Numbers | None | At every decision point |
| Who drove | Interviewer | Candidate |

The knowledge gap between the two candidates is small; both knew token bucket and Redis. The behavior gap is the hire/no-hire line: clarify first, drive the agenda, make decisions atomic and failures explicit, and attach a number to every choice.

## Practice this

- Run the same drill on any question in the [catalog](../questions/README.md): play Candidate B out loud, unprompted, against a timer.
- Get graded by a human: [mock interviews with ex-FAANG engineers](https://www.designgurus.io/mock-interviews)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)