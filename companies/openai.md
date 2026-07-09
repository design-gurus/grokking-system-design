# OpenAI: system design interview

> How OpenAI actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How OpenAI runs it.** You may face system design twice: a practical screen and a deeper onsite round. For product-flavored prompts, stopping at a backend diagram is explicitly not enough: interviewers expect wireframes, an API contract, and a storage schema, and they probe depth aggressively on whatever you draw.

## Signature questions

- Design the OpenAI Playground (front-end flows, API layer, and schema for thread and message history)
- Design an LLM-powered enterprise search system (a frequent senior-loop prompt)
- Design a notification system, Slack-style messaging, or a distributed job scheduler
- Design a streaming platform at scale

## What interviewers probe

- Depth on demand: every component gets "why this, what breaks at 10x, how do you know"
- Full-stack thinking on product prompts: UI, API shapes, and data model together
- Scoping judgment: what you build first, defer, and stub, with sane back-of-envelope math

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [caching](../patterns/caching.md), [sharding partitioning](../patterns/sharding-partitioning.md), [api gateway](../patterns/api-gateway.md)
- Practice questions: [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md), [Design notification system](../questions/design-notification-system.md), [Design google search](../questions/design-google-search.md)
- Full company guide: [OpenAI system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-openai-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
