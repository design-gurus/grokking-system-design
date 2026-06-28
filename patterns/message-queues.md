# Message queues

> Put a buffer between producers and consumers so work can be processed asynchronously and the two sides scale independently.

## What it is

A message queue (or broker) accepts messages from producers and delivers them to consumers later. It decouples the two sides: producers do not wait for consumers, and a burst of work is absorbed by the queue instead of overwhelming downstream services.

## When to use it

- Slow or spiky work that should not block the request path (sending email, encoding video, generating thumbnails).
- Smoothing traffic bursts (the queue absorbs the spike, consumers drain it at a steady rate).
- Fan-out, where one event triggers many independent actions.
- Decoupling services so they can fail and scale independently.

## Queue vs publish-subscribe

- Queue (work distribution): each message is processed by one consumer. Good for task processing.
- Publish-subscribe (fan-out): each message goes to all subscribers. Good for broadcasting events.

## Delivery guarantees

| Guarantee | Meaning |
|-----------|---------|
| At most once | May lose messages, never duplicates |
| At least once | Never loses, may duplicate (consumers must be idempotent) |
| Exactly once | No loss, no duplicates; hardest and most expensive |

At least once plus idempotent consumers is the common, practical default.

## Things to mention in an interview

- Idempotency: design consumers so reprocessing a message is safe.
- Ordering: most queues only guarantee order within a partition, not globally.
- Dead letter queues: where messages go after repeated failures.
- Backpressure: what happens when the queue grows faster than consumers drain it.

## Go deeper

- Practice live: [Mock interviews](https://www.designgurus.io/mock-interviews)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)