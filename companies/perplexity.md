# Perplexity: system design interview

> How Perplexity actually runs its system design round, the signature questions candidates report, and what interviewers probe. Part of the [company-specific interviews](README.md) index.

**How Perplexity runs it.** Every design question orbits AI search: RAG, retrieval, crawling freshness, LLM serving, and caching. The grading rubric is the cost-latency-quality triangle: every decision should be priced in the other two currencies, out loud.

## Signature questions

- Design an end-to-end answer engine: query understanding, retrieval, reranking, synthesis with citations, streamed inside a ~2 second budget
- Design real-time web crawling and indexing so answers reflect pages that changed an hour ago
- Design the LLM serving path: model routing by query complexity, batching, token streaming, provider failover
- Design a semantic cache with staleness bounds that vary by query class

## What interviewers probe

- Latency budgets with millisecond arithmetic, designed around time-to-first-token
- Retrieval quality literacy: chunking tradeoffs, hybrid lexical-plus-vector search, evaluation
- Citation and trust mechanics: provenance tracked from retrieval through synthesis

## Prepare

- Patterns to review: [caching](../patterns/caching.md), [cdn](../patterns/cdn.md), [message queues](../patterns/message-queues.md), [database indexing](../patterns/database-indexing.md)
- Practice questions: [Design google search](../questions/design-google-search.md), [Design web crawler](../questions/design-web-crawler.md), [Design typeahead autocomplete](../questions/design-typeahead-autocomplete.md)
- Full company guide: [Perplexity system design interview](https://www.designgurus.io/answers/detail/what-to-expect-in-the-perplexity-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design)
