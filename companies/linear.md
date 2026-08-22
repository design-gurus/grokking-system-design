# Linear: system design interview

> How Linear actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Linear runs it.** The client is offline-first, so the whole round turns on sync: a local copy that answers every read, and a server that decides one global order for incoming changes. The architecture round runs 45 to 60 minutes in the virtual onsite, and candidates report applied design work rather than abstract trivia. Product judgment is graded next to the architecture, so state what you would ship first and what can wait.

## Signature questions

- Design a sync engine for an offline-first issue tracker
- Design real-time collaboration features: presence, live updates, comment threads
- Model the data for issues, projects, and the workflow state machine
- Design fast workspace search that also works offline
- Design the update path to thousands of connected clients

## What interviewers probe

- Whether the design keeps the client fast, since speed is the product's identity
- Whether clients truly converge, including the offline edit cases
- Trade-off quality, such as choosing last writer wins per property and naming where it fails
- A realistic size estimate for the local store, said out loud

## Prepare

- Patterns to review: [long polling websockets sse](../patterns/long-polling-websockets-sse.md), [event sourcing cqrs](../patterns/event-sourcing-cqrs.md), [consistency models](../patterns/consistency-models.md), [logical clocks](../patterns/logical-clocks.md), [caching](../patterns/caching.md)
- Practice questions: [Design google docs](../questions/design-google-docs.md), [Design collaborative whiteboard](../questions/design-collaborative-whiteboard.md), [Design typeahead autocomplete](../questions/design-typeahead-autocomplete.md)
- Full company guide: [Linear system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-linear-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
