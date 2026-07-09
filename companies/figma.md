# Figma: system design interview

> How Figma actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Figma runs it.** Classic infrastructure with a real-time multiplayer tilt: WebSocket scaling, presence, and state recovery on disconnect. Practical conflict-resolution literacy matters more than CRDT derivations: knowing why per-property last-writer-wins is often enough is the fluency signal.

## Signature questions

- Design multiplayer document sync: optimistic local edits, server-ordered operations, reconnect recovery
- Design presence and live cursors for thousands of concurrent files
- Scale a WebSocket layer: connection affinity, deploys without dropping everyone, reconnect storms

## What interviewers probe

- Requirements through the user's eyes: what latency is felt, what loss is acceptable
- The stateful-connection problem: sessions pinned to servers and what happens when one dies
- Degradation as product design: what the user sees when sync struggles

## Prepare

- Patterns to review: [long polling websockets sse](../patterns/long-polling-websockets-sse.md), [consistency models](../patterns/consistency-models.md), [message queues](../patterns/message-queues.md)
- Practice questions: [Design collaborative whiteboard](../questions/design-collaborative-whiteboard.md), [Design google docs](../questions/design-google-docs.md)
- Full company guide: [Figma system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-figma-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
