# Question catalog

Classic system design interview questions. Each walkthrough stays at the level of approach, key decisions, and trade-offs. For full, worked, interactive solutions, see the courses linked in each file.

## Core questions

| Question | Difficulty | Key patterns | Status |
|----------|-----------|--------------|--------|
| [Design TinyURL](design-tinyurl.md) | Easy | Hashing, caching, data modeling | Written |
| [Design Instagram](design-instagram.md) | Medium | Sharding, caching, feed generation | Written |
| [Design Twitter](design-twitter.md) | Medium | Fan-out, caching, timelines | Written |
| [Design WhatsApp](design-whatsapp.md) | Medium | Connections, message delivery, presence | Written |
| [Design a rate limiter](design-rate-limiter.md) | Medium | Token bucket, distributed counters | Written |
| [Design a notification system](design-notification-system.md) | Medium | Queues, fan-out, channels | Written |
| [Design Uber](design-uber.md) | Hard | Geo-indexing, matching, streaming | Written |
| [Design Netflix](design-netflix.md) | Hard | CDN, encoding, recommendations | Written |
| [Design Dropbox](design-dropbox.md) | Hard | Chunking, metadata, sync | Written |
| [Design a web crawler](design-web-crawler.md) | Hard | Frontier, dedup, politeness | Written |

## Advanced questions

Deeper problems, mapped to the [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii) topics.

| Question | Difficulty | Key idea | Status |
|----------|-----------|----------|--------|
| [Design a unique ID generator](design-unique-id-generator.md) | Medium | Snowflake-style distributed IDs | Written |
| [Design a likes counter (YouTube)](design-youtube-likes-counter.md) | Medium | High-volume distributed counters | Written |
| [Design Reddit](design-reddit.md) | Medium | Voting, ranking, nested comments | Written |
| [Design Google Calendar](design-google-calendar.md) | Medium | Recurrence, timezones, reminders | Written |
| [Design a recommendation system](design-recommendation-system.md) | Medium | Candidate generation and ranking | Written |
| [Design Gmail](design-gmail.md) | Medium | Mail storage, search, spam | Written |
| [Design Google News](design-google-news.md) | Medium | Ingestion, clustering, ranking | Written |
| [Design a code judging system](design-code-judging-system.md) | Medium | Sandboxing, queueing, security | Written |
| [Design a payment system](design-payment-system.md) | Hard | Idempotency, ledger, reconciliation | Written |
| [Design a flash sale system](design-flash-sale-system.md) | Hard | No oversell, spike control | Written |
| [Design a reminder and alert system](design-reminder-alert-system.md) | Hard | Scheduling at scale, reliable firing | Written |

## More systems

A broad set of commonly-asked systems, mapped to the [System Design Interview Crash Course](https://www.designgurus.io/course/system-design-interview-crash-course).

| Question | Key idea |
|----------|----------|
| [Design YouTube](design-youtube.md) | Video upload, transcoding, CDN streaming |
| [Design a distributed cache (Redis)](design-distributed-cache.md) | Sharded in-memory cache, eviction |
| [Design Discord](design-discord.md) | Servers, channels, real-time fan-out |
| [Design a metrics and monitoring system](design-metrics-monitoring.md) | Time-series ingestion, alerting |
| [Design Amazon S3](design-amazon-s3.md) | Durable object storage |
| [Design Google Ads](design-google-ads.md) | Ad auction, click tracking, budgets |
| [Design Amazon shopping cart](design-amazon-shopping-cart.md) | Always-available per-user cart |
| [Design a stock exchange](design-stock-exchange.md) | Matching engine, order book |
| [Design People You May Know](design-people-you-may-know.md) | Friends-of-friends graph |
| [Design LinkedIn connections](design-linkedin-connections.md) | Connection graph, degrees |
| [Design a collaborative whiteboard](design-collaborative-whiteboard.md) | Real-time shared canvas |
| [Design Google Docs](design-google-docs.md) | Collaborative editing (OT/CRDT) |
| [Design an ad click aggregator](design-ad-click-aggregator.md) | High-volume stream aggregation |
| [Design a live comment streaming service](design-live-comment-streaming.md) | Massive real-time fan-out |
| [Design a code deployment system](design-code-deployment-system.md) | Artifact distribution, safe rollout |
| [Design an API gateway](design-api-gateway.md) | Routing, auth, rate limiting |
| [Design Amazon Lambda](design-amazon-lambda.md) | Serverless function execution |
| [Design ChatGPT](design-chatgpt.md) | LLM inference serving, streaming |
| [Design typeahead / autocomplete](design-typeahead-autocomplete.md) | Prefix trie, popularity ranking |
| [Design Google Search](design-google-search.md) | Crawl, inverted index, ranking |
| [Design Airbnb](design-airbnb.md) | Geo search, no double-booking |
| [Design a distributed job scheduler](design-distributed-job-scheduler.md) | Scheduling at scale, reliable firing |

## Add a new question

1. Copy [_template.md](_template.md) to `questions/design-your-system.md`.
2. Fill in each section. Keep it at the approach and trade-offs level.
3. Add a row above.