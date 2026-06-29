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

## Classic system design questions

| Question | Difficulty | Key patterns | Walkthrough |
|----------|-----------|--------------|-------------|
| Design TinyURL | Easy | Hashing, caching, data modeling | [design-tinyurl.md](questions/design-tinyurl.md) |
| Design Instagram | Medium | Sharding, caching, feed generation | [design-instagram.md](questions/design-instagram.md) |
| Design Twitter | Medium | Fan-out, caching, timelines | [design-twitter.md](questions/design-twitter.md) |
| Design Uber | Hard | Geo-indexing, matching, streaming | [design-uber.md](questions/design-uber.md) |
| Design a web crawler | Hard | Frontier, dedup, politeness | [design-web-crawler.md](questions/design-web-crawler.md) |

See the full catalog in [questions/](questions/). To add a new question, copy [questions/_template.md](questions/_template.md). For full worked solutions, see the [course](https://www.designgurus.io/course/grokking-the-system-design-interview).

## Distributed systems deep dives

Case studies of landmark systems, the "how does X work" questions common in senior interviews: Dynamo, Cassandra, BigTable, Kafka, Chubby, GFS, and HDFS. See [deep-dives/](deep-dives/).

## Cheat sheets

- [Back-of-the-envelope estimation](cheat-sheets/estimation.md): the latency and capacity numbers worth memorizing.
- [Interview framework](cheat-sheets/interview-framework.md): the step-by-step structure with timings.
- [Non-functional requirements](cheat-sheets/non-functional-requirements.md): scalability, availability, latency, consistency, and the rest.
- [Trade-off decision guides](cheat-sheets/trade-offs.md): the common "X vs Y" decisions and how to choose.
- [SQL vs NoSQL](cheat-sheets/sql-vs-nosql.md): how to choose, and how to justify it in an interview.

## Study roadmaps

- [2-week plan](roadmaps/2-week-plan.md): a focused sprint before an interview.
- More plans live in [roadmaps/](roadmaps/).

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