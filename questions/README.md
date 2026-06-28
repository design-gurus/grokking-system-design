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

## Add a new question

1. Copy [_template.md](_template.md) to `questions/design-your-system.md`.
2. Fill in each section. Keep it at the approach and trade-offs level.
3. Add a row above.