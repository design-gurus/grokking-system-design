# AMD: system design interview

> How AMD actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How AMD runs it.** Questions sit at the hardware-software boundary, and many rounds end with you implementing one component in real C or C++. Reported prompts include a memory allocator, a CPU-to-GPU ring buffer, a caching layer for a graphics driver, and the layering of a new GPU feature across user-space library, kernel driver, and firmware; senior scope adds GPU context switching and virtual memory. Web-scale questions about feeds and messaging are rare, and the flavor follows the team, so ask whether driver, compiler, or AI software people run your loop.

## Signature questions

- Design a memory allocator with fixed-size pools and alignment rules
- Design a ring buffer between a CPU and a device
- Design a caching layer for a graphics driver
- Design the driver architecture for a new GPU feature
- Design GPU context switching or a virtual memory system

## What interviewers probe

- A correct hardware model: cache lines, the cost of memory bandwidth, why copies are expensive
- Interfaces before internals, which also makes the coding portion faster
- Concurrency and failure handling: device resets, racing threads, full buffers, memory ordering
- Arithmetic on your own design (buffer size against command rate) and how you would test for wrap-around and ordering bugs

## Prepare

- Patterns to review: [backpressure](../patterns/backpressure.md), [message queues](../patterns/message-queues.md), [caching](../patterns/caching.md), [consistency models](../patterns/consistency-models.md)
- Practice questions: [Design distributed message queue](../questions/design-distributed-message-queue.md), [Design distributed cache](../questions/design-distributed-cache.md), [Design gpu cluster scheduler](../questions/design-gpu-cluster-scheduler.md)
- Full company guide: [AMD system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-amd-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
