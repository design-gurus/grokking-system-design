# Cursor (Anysphere): system design interview

> How Cursor (Anysphere) actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Cursor (Anysphere) runs it.** Design conversations live where ML serving meets editor experience: latency budgets are perceptual (keystroke-visible), costs are per-keystroke, and cancellation is a first-class primitive because the user's next keypress invalidates in-flight work constantly.

## Signature questions

- Design the context retrieval system: select what the model sees from a million-line repo, inside a token budget, in tens of milliseconds
- Design Tab-prediction serving: sub-100ms budgets, speculative execution, aggressive caching, small-model economics
- Design streaming completion into a live document (user edits mid-stream; cancel or rebase)
- Design codebase indexing with incremental updates on every edit and privacy boundaries

## What interviewers probe

- Perceptually anchored latency budgets, spent stage by stage
- Cost-per-keystroke discipline: when not to call the model at all
- Retrieval ranking under a budget: what earns its tokens

## Prepare

- Patterns to review: [caching](../patterns/caching.md), [database indexing](../patterns/database-indexing.md), [long polling websockets sse](../patterns/long-polling-websockets-sse.md)
- Practice questions: [Design typeahead autocomplete](../questions/design-typeahead-autocomplete.md), [Design google docs](../questions/design-google-docs.md)
- Full company guide: [Cursor (Anysphere) system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-cursor-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
