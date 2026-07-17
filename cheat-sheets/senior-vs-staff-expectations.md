# Senior vs staff: how the same question is graded differently

The question does not change with level; the grading does. "Design a notification system" is asked at every level from mid to staff+. What changes is who drives, how much ambiguity you are expected to resolve yourself, and how deep the trade-off reasoning goes. Interviewers rarely say this out loud, which is why strong senior candidates get downleveled: they gave a clean mid-level performance.

## The one-line summary per level

| Level | What the interviewer is asking themselves |
|-------|-------------------------------------------|
| Mid (L4 or equivalent) | "Can they design a working system with guidance?" |
| Senior (L5) | "Can they own this system end to end, including its failure modes?" |
| Staff (L6+) | "Would I trust them to make this decision for an org, and to know when not to build it?" |

## What each level looks like on the same question

Take [design a notification system](../questions/design-notification-system.md).

**Mid-level pass**: covers the happy path competently. API, queue, workers, channel providers, a reasonable data model. Answers follow-up questions correctly. The interviewer steers; the candidate executes.

**Senior pass**: everything above, unprompted, plus ownership of failure. Talks about [idempotency](../patterns/idempotency.md) before the interviewer asks ("retries will double-send without a dedup key"). Quantifies ("100M notifications a day is about 1200 per second average, maybe 10x peak"). Names the trade-offs at each fork and picks one with a reason. Drives the agenda: "the interesting part here is delivery guarantees; let me go deep there."

**Staff pass**: everything above, plus judgment about the system's place in the world. Questions the requirement itself ("do all notification types need the same delivery guarantee? Marketing can drop; security alerts cannot; that split changes the design"). Reasons about evolution ("v1 ships with one queue and one worker pool; here is the seam where channels split into services when scale demands it"). Talks about cost, team boundaries, and operational load as design inputs, not afterthoughts. Knows what not to build ("SMS delivery is a vendor problem; we buy it").

## The behaviors that mark each level

**What moves you from mid to senior**
- You drive; the interviewer observes. You propose the agenda and the deep-dive topic.
- Numbers appear without being requested ([estimation](estimation.md)), and they change your design.
- Every component you draw, you can fail: "what happens when this dies" has an answer before it is asked.
- Trade-offs are stated as decisions, not catalogs: "I chose X, accepting Y" beats listing options.

**What moves you from senior to staff**
- You negotiate the problem before solving it. Requirements are inputs to challenge, not gospel.
- You design for the second year, not the demo: migrations, versioning, the part that gets deleted.
- You bring the organization in: which team owns which component, what the on-call burden is, where the vendor line sits.
- You are calibrated about uncertainty: "I do not know the exact Kafka limit here; I would benchmark, but the design holds either way" is a staff sentence.

## Common downleveling mistakes

- Waiting to be asked. At senior+, silence from the interviewer is the test, not a sign you are done.
- Encyclopedia mode: naming five options for every decision without choosing. Breadth reads as mid-level; commitment reads as senior.
- Depth in only one corner: staff candidates who only want to talk about their specialty (say, Kafka internals) fail the breadth check going the other way.
- Ignoring the boring parts: auth, observability, rollout, and cost are exactly where staff signal lives, because that is what the job is.
- Over-engineering the demo: proposing cells and multi-region active-active for 1000 QPS signals you scale designs by prestige, not by numbers. Right-sizing is the staff move.

## How to prepare differently

- Senior: rehearse failure narration. For every question in the [catalog](../questions/README.md), practice answering "what breaks first and what do you do about it" for your own design ([common mistakes](common-mistakes.md) lists the usual suspects).
- Staff: rehearse requirement negotiation. For each practice question, find the requirement you would push back on, the thing you would buy instead of build, and the one-sentence v1/v2 split.
- Both: watch the clock and own it. Leading the [framework](interview-framework.md) yourself, with timings, is itself level signal.

## Go deeper

- Company-by-company expectations: [company-specific interviews](../companies/README.md)
- Practice against a human bar: [mock interviews with ex-FAANG engineers](https://www.designgurus.io/mock-interviews)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)