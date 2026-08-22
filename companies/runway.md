# Runway: system design interview

> How Runway actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Runway runs it.** Questions come straight from the product: multi-gigabyte video assets, GPU workers, and users who sit waiting while a render finishes. The signature shape is a generation job system, where a request enters a queue with a priority, GPU workers produce the video, and the client tracks progress until the result lands in object storage. Expect about an hour of requirements and architecture followed by deep follow ups on cost per generation and on failures mid render, and machine learning candidates may get an ML design round that adds serving and evaluation.

## Signature questions

- Design a video generation service backed by a limited GPU pool
- Design upload, storage, and delivery for multi-gigabyte video projects
- Design progress tracking for jobs that take seconds to minutes
- Design a scheduler that keeps GPU workers busy without starving interactive users
- Design sharing and collaboration on creative projects

## What interviewers probe

- Requirements first: who the user is, how large the files are, and how fast results must arrive
- Async thinking: queues and progress updates, never a minutes-long synchronous request
- Cost awareness: naming GPU utilization as a goal before the interviewer asks
- Failure handling: checkpointing long renders and idempotent submission so a retry cannot double charge

## Prepare

- Patterns to review: [message queues](../patterns/message-queues.md), [idempotency](../patterns/idempotency.md), [backpressure](../patterns/backpressure.md), [cdn](../patterns/cdn.md), [long polling websockets sse](../patterns/long-polling-websockets-sse.md)
- Practice questions: [Design youtube](../questions/design-youtube.md), [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md), [Design gpu cluster scheduler](../questions/design-gpu-cluster-scheduler.md), [Design netflix](../questions/design-netflix.md)
- Full company guide: [Runway system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-runway-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
