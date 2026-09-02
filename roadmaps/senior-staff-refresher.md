# Senior and staff refresher

For experienced engineers who have not interviewed in years. You have built and operated real systems. Your problem is not learning what a cache is. Your problem is that the interview is a 45-minute performance with its own rules, your mental model of the default stack is a few years stale, and the bar for your level moved while you were shipping.

This plan is organized by gap, not by day. Diagnose first, then fix only what is broken. Most people here need 6 to 10 hours total, not six weeks.

## Who this is not for

If you have never taken a system design interview, or you cannot yet explain sharding and replication without notes, start with the [6-week study plan](6-week-plan.md) instead. This plan assumes the knowledge is there and only the performance is rusty.

## Step 1: the diagnostic, before you read anything

Do this cold. Reading first will hide the gaps you need to find.

Set a timer for 45 minutes. Pick a question outside your specialty, so a backend engineer should avoid the obvious backend answer. Good choices: [design Ticketmaster](../questions/design-ticketmaster.md), [design a proximity service](../questions/design-proximity-service.md), or [design Zoom](../questions/design-zoom.md). Answer out loud, standing at a whiteboard or a blank document. Record yourself.

Then watch the recording. It will be uncomfortable and it is the highest-value hour in this plan.

## Step 2: score yourself

Mark each row honestly. Any "no" is a track in step 4.

| Check | What a pass looks like |
|-------|------------------------|
| Structure | You led with requirements and scope, and you managed the clock without being told |
| Estimation | Numbers appeared in the first ten minutes and changed a decision |
| Narration | You said why you chose each option, not just what you chose |
| Failure | Every component you drew, you failed out loud before being asked |
| Breadth | You were equally fluent outside your specialty |
| Right-sizing | Your design matched the stated scale, with no unrequested multi-region |
| Negotiation | You pushed back on at least one requirement |
| Recency | You did not reach for a stack you last used at a previous job |

Fewer than six passes means the [interview framework](../cheat-sheets/interview-framework.md) is your first fix, because structure carries the rest.

## Step 3: what changed since you last interviewed

This is the section most experienced candidates skip, and it is where stale answers come from.

- **The bar moved down a level.** What earned a senior offer a few years ago now reads as mid. The interviewer expects you to drive the session, not to answer questions well. See [senior vs staff expectations](../cheat-sheets/senior-vs-staff-expectations.md).
- **Cost is graded as a design input.** Interviewers now ask what a design costs to run, and "cheapest thing that meets the requirement" is a real answer. Right-sizing beats prestige architecture.
- **Managed services changed the default answer, but not the questions.** You would not build a queue at work, so interviewers now ask you to build one on purpose. See [design a distributed message queue](../questions/design-distributed-message-queue.md).
- **AI and LLM questions are a real category**, not just at AI labs. Retrieval, inference serving, and cost per request now appear in ordinary product loops. Skim [design a RAG pipeline](../questions/design-rag-pipeline.md) and [design an LLM gateway](../questions/design-llm-gateway.md) even if you never touch models.
- **Vector search joined the standard toolkit.** Embeddings and approximate nearest-neighbor search sit next to the inverted index now, and hybrid retrieval is the expected answer. See [design semantic search](../questions/design-semantic-search.md), and [HNSW and vector databases](../deep-dives/hnsw-vector-search.md) next to [Elasticsearch and Lucene](../deep-dives/elasticsearch-lucene.md) for the two halves of retrieval.
- **Real-time is the default expectation**, not a bonus feature. Know when to pick server-sent events over WebSockets: [WebSockets vs SSE vs long polling](../cheat-sheets/websockets-vs-sse-vs-long-polling.md).
- **The boring parts are now the signal.** Rollout, observability, on-call load, and team boundaries are where staff evidence lives, because that is what the job is.
- **Newer patterns get named directly.** If your vocabulary predates them, read [distributed transactions](../patterns/distributed-transactions.md), the [outbox pattern](../patterns/outbox-pattern.md), [event sourcing and CQRS](../patterns/event-sourcing-cqrs.md), and [backpressure](../patterns/backpressure.md).

## Step 4: fill only your gaps

**Recall is slow (breadth).** You know the material but retrieval is sluggish under pressure. Run the [flashcards](../cheat-sheets/flashcards.md) until every card takes under 30 seconds. This is the fastest fix in the plan and usually the only one breadth needs.

**Structure is weak.** Rehearse the [framework](../cheat-sheets/interview-framework.md) with timings until the shape is automatic. Then redo the diagnostic question and watch only the first ten minutes.

**Numbers are missing.** Reread [estimation](../cheat-sheets/estimation.md) and [latency numbers](../cheat-sheets/latency-numbers.md). Then take three questions and produce only the numbers, no architecture, in ten minutes each.

**Failure narration is thin.** Take your own diagnostic design and kill every box in turn. Say what breaks, what the user sees, and what you do. Senior candidates are graded on this more than on the happy path.

**Depth is lopsided.** Pick the two areas furthest from your daily work and read those [patterns](../patterns/) plus one [deep dive](../deep-dives/) each. Staff candidates fail the breadth check as often as the depth one. If your gaps are on the infrastructure side, [Borg and Kubernetes](../deep-dives/borg-kubernetes.md), [Flink](../deep-dives/flink-stream-processing.md), and [Redis internals](../deep-dives/redis-internals.md) cover the layers most often taken for granted.

**You do not negotiate requirements.** For each practice question, write down one requirement you would challenge, one thing you would buy instead of build, and a one-sentence split between the first version and the second. This is the clearest staff signal available to you.

## Step 5: rehearse the performance

Knowledge is not the constraint here, so spend your remaining time on delivery.

1. Two more timed questions, out loud, recorded, at least one outside your specialty. Use the [question catalog](../questions/README.md).
2. Read the [annotated mock interview](../cheat-sheets/mock-interview-walkthrough.md) and compare it against your own recording. Find the sentences the stronger candidate says that you do not.
3. Reread [common mistakes](../cheat-sheets/common-mistakes.md) and [communication tips](../cheat-sheets/communication-tips.md) the day before.
4. If the role is at a specific company, read its page in the [company index](../companies/README.md). The same question is graded differently at Stripe, Bloomberg, and Palantir.
5. Book one [mock interview with an ex-FAANG engineer](https://www.designgurus.io/mock-interviews?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=roadmaps-senior-staff-refresher). An experienced engineer's blind spots are hard to see alone, which is the whole reason this plan starts with a recording.

## The failure modes specific to experienced candidates

These do not appear in the general advice, because they only happen to people who have real production scars.

- **Answering from your production system.** "We solved this with Kafka at my last company" is context the interviewer does not have, and the question's constraints may be different. Derive it here.
- **Skipping estimation because you know the scale.** You are not graded on knowing, you are graded on showing the method.
- **Silent competence.** You make a good decision instantly because it is obvious to you, and never say why. Unnarrated judgment scores as no judgment.
- **Scars as over-engineering.** You got paged for this once, so you design for it always. If the requirement does not justify it, it reads as poor judgment rather than experience.
- **Specialty gravity.** You steer every question toward the thing you know best. Interviewers notice, and it reads as narrow.
- **Treating the requirements as fixed.** At staff level, accepting the problem as stated is itself a miss.

## Go deeper

- Level calibration: [senior vs staff expectations](../cheat-sheets/senior-vs-staff-expectations.md)
- Practice against a human bar: [mock interviews with ex-FAANG engineers](https://www.designgurus.io/mock-interviews?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=roadmaps-senior-staff-refresher)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=roadmaps-senior-staff-refresher)
