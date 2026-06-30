# Grokking System Design

> The free, open companion to the original **Grokking the System Design Interview** course by [DesignGurus.io](https://www.designgurus.io/course/grokking-the-system-design-interview), created by Arslan Ahmad and the original Grokking team.

A pattern-based guide to system design interviews. Learn the building blocks once, then apply them to any design question. This repository is a free index, summary, and cheat-sheet collection. For interactive diagrams, video lessons, and worked solutions, see the full course.

<!-- Add badges once the repo is live, for example: stars, license, last commit. -->

---

## What is "Grokking System Design"?

"Grok" means to understand something so completely that it becomes intuitive. Grokking System Design is the pattern-based approach to system design interviews: instead of memorizing answers to a fixed list of questions, you learn a small set of reusable building blocks (caching, sharding, replication, consistency models, messaging, and more) that appear again and again across very different systems. Once you know the patterns, any new design problem feels familiar.

This methodology was created by Arslan Ahmad. The original, fully updated course lives at [DesignGurus.io](https://www.designgurus.io/course/grokking-the-system-design-interview).

## How to use this repo

1. Read the [interview framework](cheat-sheets/interview-framework.md) so you have a repeatable structure for any question.
2. Work through the [core patterns](patterns/) until each one is intuitive.
3. Practice with the [question catalog](questions/), applying the patterns.
4. Follow a [study roadmap](roadmaps/) to stay on track.
5. Go deeper in the [full course](https://www.designgurus.io/course/grokking-the-system-design-interview) when you want interactive lessons and worked solutions.

## The system design interview framework

A repeatable structure beats memorized answers. The short version:

1. Clarify requirements and scope (functional and non-functional).
2. Estimate scale (traffic, storage, bandwidth).
3. Define the API.
4. Design the data model.
5. Sketch the high-level architecture.
6. Deep dive on one or two components.
7. Identify bottlenecks and trade-offs.

Full breakdown with timings: [cheat-sheets/interview-framework.md](cheat-sheets/interview-framework.md).

## Core building blocks (patterns)

| Pattern | What it solves | Cheat sheet | Learn in depth |
|---------|----------------|-------------|----------------|
| Caching | Read latency and load on the data store | [caching.md](patterns/caching.md) | [Course](https://www.designgurus.io/course/grokking-the-system-design-interview) |
| Load balancing | Distributing traffic across servers | [load-balancing.md](patterns/load-balancing.md) | [Course](https://www.designgurus.io/course/grokking-the-system-design-interview) |
| Sharding and partitioning | Scaling data beyond one machine | [sharding-partitioning.md](patterns/sharding-partitioning.md) | [Course](https://www.designgurus.io/course/grokking-the-system-design-interview) |
| Replication | Availability and read scaling | [replication.md](patterns/replication.md) | [Course](https://www.designgurus.io/course/grokking-the-system-design-interview) |
| Consistency models | Correctness under concurrency | [consistency-models.md](patterns/consistency-models.md) | [Course](https://www.designgurus.io/course/grokking-the-system-design-interview) |
| Consistent hashing | Even distribution with minimal reshuffling | [consistent-hashing.md](patterns/consistent-hashing.md) | [Course](https://www.designgurus.io/course/grokking-the-system-design-interview) |
| Message queues | Decoupling and async processing | [message-queues.md](patterns/message-queues.md) | [Course](https://www.designgurus.io/course/grokking-the-system-design-interview) |
| Rate limiting | Protecting services from overload | [rate-limiting.md](patterns/rate-limiting.md) | [Course](https://www.designgurus.io/course/grokking-the-system-design-interview) |

See the full list in [patterns/](patterns/). To add a new pattern, copy [patterns/_template.md](patterns/_template.md).

## System design questions

Forty-plus walkthroughs at the approach-and-trade-offs level, grouped by difficulty. Self-test with the [practice question bank](questions/practice-bank.md), and see full worked solutions in the [course](https://www.designgurus.io/course/grokking-the-system-design-interview).

### Basic

- [Design TinyURL](questions/design-tinyurl.md)
- [Design a rate limiter](questions/design-rate-limiter.md)
- [Design a unique ID generator](questions/design-unique-id-generator.md)
- [Design a distributed cache](questions/design-distributed-cache.md)
- [Design an API gateway](questions/design-api-gateway.md)
- [Design typeahead / autocomplete](questions/design-typeahead-autocomplete.md)
- [Design a notification system](questions/design-notification-system.md)
- [Design a YouTube likes counter](questions/design-youtube-likes-counter.md)
- [Design Amazon shopping cart](questions/design-amazon-shopping-cart.md)

### Advanced

- [Design Instagram](questions/design-instagram.md)
- [Design Twitter](questions/design-twitter.md)
- [Design WhatsApp](questions/design-whatsapp.md)
- [Design Reddit](questions/design-reddit.md)
- [Design YouTube](questions/design-youtube.md)
- [Design Discord](questions/design-discord.md)
- [Design Amazon S3](questions/design-amazon-s3.md)
- [Design Google Calendar](questions/design-google-calendar.md)
- [Design Gmail](questions/design-gmail.md)
- [Design Airbnb](questions/design-airbnb.md)
- [Design a metrics and monitoring system](questions/design-metrics-monitoring.md)
- [Design a recommendation system](questions/design-recommendation-system.md)
- [Design People You May Know](questions/design-people-you-may-know.md)
- [Design LinkedIn connections](questions/design-linkedin-connections.md)
- [Design an ad click aggregator](questions/design-ad-click-aggregator.md)
- [Design a live comment streaming service](questions/design-live-comment-streaming.md)
- [Design a code deployment system](questions/design-code-deployment-system.md)
- [Design Google News](questions/design-google-news.md)
- [Design a code judging system](questions/design-code-judging-system.md)
- [Design a distributed job scheduler](questions/design-distributed-job-scheduler.md)

### Expert

- [Design Uber](questions/design-uber.md)
- [Design Netflix](questions/design-netflix.md)
- [Design Dropbox](questions/design-dropbox.md)
- [Design a web crawler](questions/design-web-crawler.md)
- [Design a payment system](questions/design-payment-system.md)
- [Design a flash sale system](questions/design-flash-sale-system.md)
- [Design a reminder and alert system](questions/design-reminder-alert-system.md)
- [Design Google Search](questions/design-google-search.md)
- [Design Google Docs](questions/design-google-docs.md)
- [Design a collaborative whiteboard](questions/design-collaborative-whiteboard.md)
- [Design a stock exchange](questions/design-stock-exchange.md)
- [Design Google Ads](questions/design-google-ads.md)
- [Design ChatGPT](questions/design-chatgpt.md)
- [Design Amazon Lambda](questions/design-amazon-lambda.md)

See the full catalog in [questions/](questions/). To add a new question, copy [questions/_template.md](questions/_template.md).

## Distributed systems deep dives

Case studies of landmark systems, the "how does X work" questions common in senior interviews: Dynamo, Cassandra, BigTable, Kafka, Chubby, GFS, and HDFS. See [deep-dives/](deep-dives/).

## Cheat sheets

- [Back-of-the-envelope estimation](cheat-sheets/estimation.md): the latency and capacity numbers worth memorizing.
- [Interview framework](cheat-sheets/interview-framework.md): the step-by-step structure with timings.
- [Non-functional requirements](cheat-sheets/non-functional-requirements.md): scalability, availability, latency, consistency, and the rest.
- [Trade-off decision guides](cheat-sheets/trade-offs.md): the common "X vs Y" decisions and how to choose.
- [SQL vs NoSQL](cheat-sheets/sql-vs-nosql.md): how to choose, and how to justify it in an interview.
- [Core components reference](cheat-sheets/core-components.md): the building blocks and when to use each.
- [Common mistakes and anti-patterns](cheat-sheets/common-mistakes.md): what sinks interviews, and how to avoid it.
- [Interview communication tips](cheat-sheets/communication-tips.md): how to come across as a senior candidate.

## Study roadmaps

- [1-week crash plan](roadmaps/1-week-plan.md): when your interview is days away.
- [2-week sprint](roadmaps/2-week-plan.md): a focused sprint before an interview.
- [6-week study plan](roadmaps/6-week-plan.md): build depth from a baseline.
- Pick by timeline in [roadmaps/](roadmaps/).

## Glossary

New to the vocabulary? Start with the [glossary](glossary.md).

## Recommended reading (DesignGurus blog)

Free, in-depth articles that pair well with this repo.

**Start here**
- [25 Fundamental System Design Concepts](https://www.designgurus.io/blog/system-design-interview-fundamentals)
- [System Design Interview Guide (2026): Framework and How to Prepare](https://www.designgurus.io/blog/complete-guide-sys-design)
- [The Ultimate System Design Cheat Sheet](https://www.designgurus.io/blog/system-design-cheat-sheet)
- [185+ System Design Guides: The Interview Library](https://www.designgurus.io/blog/system-design-interview-library)

**Core concepts**
- [Back-of-the-Envelope Estimation](https://www.designgurus.io/blog/back-of-the-envelope-system-design-interview)
- [Scalability in System Design](https://www.designgurus.io/blog/grokking-system-design-scalability)
- [High Availability in System Design](https://www.designgurus.io/blog/high-availability-system-design-basics)
- [CAP Theorem vs PACELC](https://www.designgurus.io/blog/system-design-interview-basics-cap-vs-pacelc)
- [Consistency Patterns in Distributed Systems](https://www.designgurus.io/blog/consistency-patterns-distributed-systems)

**Architecture and APIs**
- [19 Essential Microservices Patterns](https://www.designgurus.io/blog/19-essential-microservices-patterns-for-system-design-interviews)
- [Monolithic vs Microservices vs SOA](https://www.designgurus.io/blog/monolithic-service-oriented-microservice-architecture)
- [REST vs GraphQL vs gRPC](https://www.designgurus.io/blog/rest-graphql-grpc-system-design)

## Go deeper: the full course

This repo gives you the map. The course gives you the territory: interactive diagrams, video lessons, worked solutions, and practice.

- Course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)
- Practice live: [Mock interviews with ex-FAANG engineers](https://www.designgurus.io/mock-interviews)
- More reading: [DesignGurus blog](https://www.designgurus.io/blog)

## Newsletter

System design and interview tips, straight to your inbox.

[Subscribe on Substack](https://designgurus.substack.com/)

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). If this repo helps you, please star it so more engineers can find it.

## License

Content is licensed under [Creative Commons Attribution 4.0 (CC BY 4.0)](LICENSE). You may share and adapt with attribution.

## About

Maintained by [DesignGurus.io](https://www.designgurus.io/), the home of the original Grokking the System Design Interview course by Arslan Ahmad.