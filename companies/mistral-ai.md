# Mistral AI: system design interview

> How Mistral AI actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Mistral AI runs it.** Rounds center on production RAG and agentic systems, with cost/performance tradeoffs graded as the core discipline and the efficiency thesis (capability per dollar) as the house aesthetic. Self-hosted, open-weight serving constraints appear often.

## Signature questions

- Design enterprise RAG on self-hosted open weights: chunking, hybrid retrieval, ACL-aware indexing, evaluation, on a fixed GPU budget
- Design an agentic workflow: a graph of LLM calls and tools with budgets, step limits, and failure semantics
- Design the serving layer for open-weight models: quantization, continuous batching, model-size routing

## What interviewers probe

- Cost-per-query arithmetic, fluent: tokens, GPU-hours, batching efficiency multiplied aloud
- Chunking and retrieval consequences argued, not asserted
- Model-size routing judgment: most queries do not need the largest model

## Prepare

- Patterns to review: [caching](../patterns/caching.md), [message queues](../patterns/message-queues.md), [rate limiting](../patterns/rate-limiting.md)
- Practice questions: [Design chatgpt](../questions/design-chatgpt.md), [Design google search](../questions/design-google-search.md)
- Full company guide: [Mistral AI system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-mistral-ai-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
