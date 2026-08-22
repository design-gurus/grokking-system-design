# Intel: system design interview

> How Intel actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Intel runs it.** Which team you face decides the whole round, so ask the recruiter first: cloud and services teams ask standard scalable design, while embedded, driver, and platform teams go low level. The session runs 45 to 60 minutes and splits into requirements, a high-level design, one deep dive, and a trade-off wrap-up. Resource awareness is scored heavily, so state memory, bandwidth, and power budgets unprompted, and say the mapping out loud when a classic idea appears in hardware form (caching as a memory hierarchy, queues between interrupt handlers and worker threads, sharding as work split across cores).

## Signature questions

- Design a memory manager for an embedded system
- Design a driver interface or a firmware update system
- Design a telemetry pipeline collecting from millions of devices
- Design a build and test system for a huge codebase
- Design a URL shortener, job scheduler, or metrics dashboard

## What interviewers probe

- Structure: requirements before boxes, every time
- Resource awareness: memory, bandwidth, and power budgets named without being asked
- Depth: taking one part down to data structures, free lists, and thread safety
- Trade-off honesty, where every choice names its cost

## Prepare

- Patterns to review: [caching](../patterns/caching.md), [message queues](../patterns/message-queues.md), [sharding partitioning](../patterns/sharding-partitioning.md), [batch vs stream processing](../patterns/batch-vs-stream-processing.md), [backpressure](../patterns/backpressure.md)
- Practice questions: [Design tinyurl](../questions/design-tinyurl.md), [Design distributed job scheduler](../questions/design-distributed-job-scheduler.md), [Design metrics monitoring](../questions/design-metrics-monitoring.md), [Design distributed cache](../questions/design-distributed-cache.md)
- Full company guide: [Intel system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-intel-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
