# Design a web crawler

> A system that systematically browses the web, fetching pages and following links, for example to build a search index.

## 1. Requirements

**Functional**
- Start from a set of seed URLs.
- Fetch pages, extract links, and queue new URLs to crawl.
- Store the fetched content for downstream processing.

**Non-functional**
- Scale to billions of pages.
- Be polite (do not overload any single site).
- Avoid crawling the same URL repeatedly.
- Be fault tolerant and resumable.

## 2. Estimation

Crawling billions of pages means very high fetch throughput and large storage. The crawl frontier (the set of URLs still to visit) is itself huge and must be partitioned. Deduplication at this scale is a core challenge.

See the [estimation cheat sheet](../cheat-sheets/estimation.md).

## 3. High-level design

```
[seed URLs] -> [URL frontier (queues)] -> [fetchers] -> [parser] -> [content store]
                       ^                                   |
                       |------------- new links -----------|
```

- URL frontier: a set of queues holding URLs to crawl, partitioned by host so politeness can be enforced per site.
- Fetchers: workers that download pages, respecting robots.txt and per-host rate limits.
- Parser: extracts links and content, feeds new URLs back to the frontier.
- Content store: object storage for raw pages, plus metadata.

## 4. Key challenges

| Challenge | Approach |
|-----------|----------|
| Politeness | Per-host rate limit and queue, honor robots.txt (see [rate limiting](../patterns/rate-limiting.md)) |
| Deduplication | Track seen URLs; a [Bloom filter](../patterns/bloom-filters.md) cheaply skips already-seen URLs |
| Duplicate content | Hash page content to detect near-duplicate pages |
| Scale | Partition the frontier across many machines by host |
| Traps and loops | Cap crawl depth and per-domain page counts |

## 5. Deep dive

- The URL frontier must balance freshness (recrawl important pages) and coverage (reach new pages), often with priority queues.
- Dedup at scale: a Bloom filter gives a cheap "definitely not seen" check before the expensive store lookup.
- Politeness vs throughput: per-host limits slow individual sites while the overall crawler stays fast across many hosts.

## 6. Bottlenecks and trade-offs

- The frontier size and dedup structure dominate memory; partition and use probabilistic structures.
- Politeness limits per-host speed by design.
- Storage of raw pages is large; compress and use object storage.

## Go deeper

- Read more (free): [How to Design a Web Crawler](https://www.designgurus.io/blog/design-web-crawler)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)