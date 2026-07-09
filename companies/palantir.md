# Palantir: system design interview

> How Palantir actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Palantir runs it.** The Decomposition round is the centerpiece: a vague real-world problem (a chess game, a parking garage, infection tracking) that you must turn into buildable structure: requirements interrogated, domain modeled, components carved with interfaces, and a build order defended, with mid-session constraint twists.

## Signature questions

- Decomposition prompts: design a parking garage system, a social graph with recommendations, an infection tracker
- Senior SD variant: data pipelines with lineage, fine-grained access control, heterogeneous ingestion
- Re-engineering: understand and extend an existing codebase quickly

## What interviewers probe

- Question quality in the first ten minutes: does entropy go down
- Structure that survives the twist: modules whose interfaces localize change
- Prioritization honesty: build order with reasons

## Prepare

- Patterns to review: [api gateway](../patterns/api-gateway.md), [database indexing](../patterns/database-indexing.md), [message queues](../patterns/message-queues.md)
- Practice questions: [Design google calendar](../questions/design-google-calendar.md), [Design people you may know](../questions/design-people-you-may-know.md)
- Full company guide: [Palantir system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-palantir-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
