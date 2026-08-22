# Grokking System Design

> The free, open companion to the original **Grokking the System Design Interview** course by [DesignGurus.io](https://www.designgurus.io/course/grokking-the-system-design-interview), created by Arslan Ahmad and the original Grokking team.

A pattern-based guide to system design interviews. Learn the building blocks once, then apply them to any design question. This repository is a free index, summary, and cheat-sheet collection. For interactive diagrams, video lessons, and worked solutions, see the full course.

[![GitHub stars](https://img.shields.io/github/stars/design-gurus/grokking-system-design?style=social)](https://github.com/design-gurus/grokking-system-design/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/design-gurus/grokking-system-design)](https://github.com/design-gurus/grokking-system-design/commits/main)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## Contents

- [What is Grokking System Design?](#what-is-grokking-system-design)
- [Is there a PDF or book?](#is-there-a-grokking-system-design-pdf-or-book)
- [How to use this repo](#how-to-use-this-repo)
- [The interview framework](#the-system-design-interview-framework)
- [Core building blocks (patterns)](#core-building-blocks-patterns)
- [System design questions](#system-design-questions)
- [Company-specific interviews](#company-specific-interviews)
- [Distributed systems deep dives](#distributed-systems-deep-dives)
- [Cheat sheets](#cheat-sheets)
- [Study roadmaps](#study-roadmaps)
- [Glossary](#glossary)
- [Recommended reading](#recommended-reading-designgurus-blog)
- [Newsletter](#newsletter)
- [Contributing](#contributing)

---

## What is "Grokking System Design"?

"Grok" means to understand something so completely that it becomes intuitive. Grokking System Design is the pattern-based approach to system design interviews: instead of memorizing answers to a fixed list of questions, you learn a small set of reusable building blocks (caching, sharding, replication, consistency models, messaging, and more) that appear again and again across very different systems. Once you know the patterns, any new design problem feels familiar.

This methodology was created by Arslan Ahmad. The original, fully updated course lives at [DesignGurus.io](https://www.designgurus.io/course/grokking-the-system-design-interview).

## Is there a Grokking System Design PDF or book?

No. There is no official PDF, ebook, or printed book of the Grokking the System Design Interview course, and there never has been. The PDF files that circulate online are unofficial copies of an old version of the course. They are missing the newer lessons and every fix made since they were created.

This repository is the official free way to read the material: every pattern guide, question, and cheat sheet here is free in your browser, no account needed. The full, current course is online at [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview). For more detail, see [Is there a free official download?](https://www.designgurus.io/answers/detail/grokking-system-design-pdf-is-there-a-free-official-download)

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
| Caching | Read latency and load on the data store | [caching.md](patterns/caching.md) | [Course](https://www.designgurus.io/course/system-design-patterns) |
| Load balancing | Distributing traffic across servers | [load-balancing.md](patterns/load-balancing.md) | [Course](https://www.designgurus.io/course/system-design-patterns) |
| Sharding and partitioning | Scaling data beyond one machine | [sharding-partitioning.md](patterns/sharding-partitioning.md) | [Course](https://www.designgurus.io/course/system-design-patterns) |
| Replication | Availability and read scaling | [replication.md](patterns/replication.md) | [Course](https://www.designgurus.io/course/system-design-patterns) |
| Consistency models | Correctness under concurrency | [consistency-models.md](patterns/consistency-models.md) | [Course](https://www.designgurus.io/course/system-design-patterns) |
| Consistent hashing | Even distribution with minimal reshuffling | [consistent-hashing.md](patterns/consistent-hashing.md) | [Course](https://www.designgurus.io/course/system-design-patterns) |
| Message queues | Decoupling and async processing | [message-queues.md](patterns/message-queues.md) | [Course](https://www.designgurus.io/course/system-design-patterns) |
| Rate limiting | Protecting services from overload | [rate-limiting.md](patterns/rate-limiting.md) | [Course](https://www.designgurus.io/course/system-design-patterns) |
| CAP theorem | Reasoning about trade-offs under partitions | [cap-theorem.md](patterns/cap-theorem.md) | [Course](https://www.designgurus.io/course/system-design-patterns) |
| CDN | Serving static content close to users | [cdn.md](patterns/cdn.md) | [Course](https://www.designgurus.io/course/system-design-patterns) |
| Database indexing | Fast lookups | [database-indexing.md](patterns/database-indexing.md) | [Course](https://www.designgurus.io/course/system-design-patterns) |
| Bloom filters | Cheap "definitely not present" checks | [bloom-filters.md](patterns/bloom-filters.md) | [Course](https://www.designgurus.io/course/system-design-patterns) |

These are the 12 most essential building blocks. All 30 patterns live in [patterns/](patterns/), including API gateways, quorum, leader election, idempotency, write-ahead logs, circuit breakers, sagas, event sourcing, gossip, and more. To add a new pattern, copy [patterns/_template.md](patterns/_template.md).

## System design questions

Fifty-plus walkthroughs at the approach-and-trade-offs level, grouped by difficulty. Self-test with the [practice question bank](questions/practice-bank.md), and see full worked solutions in the [course](https://www.designgurus.io/course/grokking-the-system-design-interview).

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
- [Design Ticketmaster](questions/design-ticketmaster.md)
- [Design a real-time gaming leaderboard](questions/design-gaming-leaderboard.md)
- [Design a proximity service (Yelp)](questions/design-proximity-service.md)
- [Design a hotel reservation system](questions/design-hotel-reservation.md)

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
- [Design Google Maps](questions/design-google-maps.md)
- [Design a food delivery app (DoorDash)](questions/design-food-delivery.md)
- [Design Zoom](questions/design-zoom.md)
- [Design a distributed message queue](questions/design-distributed-message-queue.md)

### AI and LLM systems

The fastest-growing question category, asked heavily by AI labs and increasingly by big tech:

- [Design a RAG pipeline](questions/design-rag-pipeline.md)
- [Design semantic search (vector search)](questions/design-semantic-search.md)
- [Design an LLM inference platform](questions/design-llm-inference-platform.md)
- [Design a model evaluation pipeline](questions/design-model-evaluation-pipeline.md)
- [Design an AI agent orchestration system](questions/design-ai-agent-orchestration.md)
- [Design a GPU cluster scheduler](questions/design-gpu-cluster-scheduler.md)
- [Design an AI code assistant (Copilot)](questions/design-code-assistant.md)
- [Design an LLM gateway](questions/design-llm-gateway.md)

See the full catalog in [questions/](questions/). To add a new question, copy [questions/_template.md](questions/_template.md).

## Company-specific interviews

The same question plays differently at different companies: a rate limiter at Stripe is an API-contract exercise, at xAI it turns into implementation, and at Bloomberg it scales to Terminal fan-out. The [company index](companies/README.md) summarizes how 122 companies run their system design rounds: the signature questions candidates report, what interviewers probe, and which patterns to review for each.

Includes [Stripe](companies/stripe.md), [OpenAI](companies/openai.md), [Bloomberg](companies/bloomberg.md), [Databricks](companies/databricks.md), [Discord](companies/discord.md), [Palantir](companies/palantir.md), [Robinhood](companies/robinhood.md), [Figma](companies/figma.md), [Citadel](companies/citadel.md), [LinkedIn](companies/linkedin.md), and 112 more, grouped by sector.

## Distributed systems deep dives

Case studies of landmark systems, the "how does X work" questions common in senior interviews: Dynamo, Cassandra, BigTable, Kafka, Chubby, GFS, HDFS, Spanner, Raft, MapReduce, ZooKeeper, Memcached at Facebook, Aurora, and DynamoDB, plus the infrastructure behind modern stacks: [Borg and Kubernetes](deep-dives/borg-kubernetes.md), [Redis internals](deep-dives/redis-internals.md), [Elasticsearch and Lucene](deep-dives/elasticsearch-lucene.md), [Flink](deep-dives/flink-stream-processing.md), and [HNSW and vector databases](deep-dives/hnsw-vector-search.md). See [deep-dives/](deep-dives/) for all nineteen, with a suggested reading order.

## Cheat sheets

- [System design in one page](cheat-sheets/system-design-in-one-page.md): the whole framework, patterns, and numbers, condensed into one screenshot.
- [Back-of-the-envelope estimation](cheat-sheets/estimation.md): the latency and capacity numbers worth memorizing.
- [Latency numbers, visualized](cheat-sheets/latency-numbers.md): the full ladder from cache hit to cross-continent round trip on one log scale, and the design rules that fall out of it.
- [Interview framework](cheat-sheets/interview-framework.md): the step-by-step structure with timings.
- [Non-functional requirements](cheat-sheets/non-functional-requirements.md): scalability, availability, latency, consistency, and the rest.
- [Trade-off decision guides](cheat-sheets/trade-offs.md): the common "X vs Y" decisions and how to choose.
- [SQL vs NoSQL](cheat-sheets/sql-vs-nosql.md): how to choose, and how to justify it in an interview.
- [PostgreSQL vs DynamoDB vs Cassandra](cheat-sheets/postgres-vs-dynamodb-vs-cassandra.md): the concrete version of the SQL vs NoSQL decision.
- [Kafka vs RabbitMQ vs SQS](cheat-sheets/kafka-vs-rabbitmq-vs-sqs.md): log vs broker vs managed queue, and the one-question shortcut.
- [Kafka vs Kinesis vs Pub/Sub](cheat-sheets/kafka-vs-kinesis-vs-pubsub.md): the managed streaming decision, by cloud, capacity model, and replay needs.
- [DynamoDB vs MongoDB](cheat-sheets/dynamodb-vs-mongodb.md): access patterns known up front vs queries that evolve with the product.
- [Redis vs Memcached](cheat-sheets/redis-vs-memcached.md): data-structure server vs pure cache.
- [REST vs gRPC vs GraphQL](cheat-sheets/rest-vs-grpc-vs-graphql.md): pick the API style per boundary, not per fashion.
- [WebSockets vs SSE vs long polling](cheat-sheets/websockets-vs-sse-vs-long-polling.md): pick the real-time transport by message direction and frequency.
- [AWS vs GCP vs Azure](cheat-sheets/aws-vs-gcp-vs-azure.md): the service translation table, so you can answer in any interviewer's cloud dialect.
- [Core components reference](cheat-sheets/core-components.md): the building blocks and when to use each.
- [Common mistakes and anti-patterns](cheat-sheets/common-mistakes.md): what sinks interviews, and how to avoid it.
- [Interview communication tips](cheat-sheets/communication-tips.md): how to come across as a senior candidate.
- [Senior vs staff expectations](cheat-sheets/senior-vs-staff-expectations.md): how the same question is graded differently by level.
- [A mock interview, annotated](cheat-sheets/mock-interview-walkthrough.md): two candidates, one question, and where the hire/no-hire line actually sits.
- [Flashcards](cheat-sheets/flashcards.md): rapid-fire question and answer cards across every core pattern, for finding the gaps in your recall.

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
- Patterns course: [System Design Patterns: From Fundamentals to Real Systems](https://www.designgurus.io/course/system-design-patterns), built around the same building blocks as [patterns/](patterns/)
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