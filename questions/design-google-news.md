# Design Google News

> Aggregate articles from many sources, group them by story, rank them, and personalize a news feed.

## 1. Requirements

**Functional**
- Ingest articles from many publishers.
- Group articles that cover the same event.
- Rank stories and personalize per user.

**Non-functional**
- Freshness (news is time-sensitive).
- Scale to many sources and readers.
- Read-heavy.

## 2. Key challenges

- Ingestion: crawl or receive feeds from publishers continuously (see the [web crawler](design-web-crawler.md) for the crawl side).
- Clustering: group articles about the same event into one story. This is the defining problem, usually done with text similarity and grouping.
- Deduplication: detect near-duplicate articles so the same story is not shown many times.
- Ranking: balance freshness, source authority, and personalization.

## 3. Deep dive

- Pipeline: ingest, extract content, deduplicate, cluster into stories, rank, then serve.
- Freshness: stories must update quickly as new articles arrive, so processing is streaming, not nightly batch.
- Personalization: blend a global ranking with user interests.

## 4. Trade-offs

- Clustering accuracy vs latency: better grouping costs more compute, but news must stay fresh.
- Global ranking vs personalization: combine both rather than choosing one.

## Go deeper

- For the full worked solution: [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)