# Cheat sheets: the fast reference

> Twenty-seven pages for recall and decisions: the structure to follow, the numbers to quote, and the "which one would you pick" answers interviewers ask for by name.

The pages you reread the week before an interview. Patterns teach you how something works and questions give you practice. These sheets are what you carry into the room.

They are also the most-read pages in this repo. Four of the six most-viewed content pages are cheat sheets, which is why the collection keeps growing.

## Start here

1. [The interview framework](interview-framework.md), the most-read page in the repo, and the structure to apply to any question.
2. [System design in one page](system-design-in-one-page.md), the whole map on one screen.
3. [Non-functional requirements](non-functional-requirements.md), the constraints that drive every later choice.
4. [Back-of-the-envelope estimation](estimation.md), the numbers worth memorizing.

## Find the sheet by the decision

Every comparison sheet starts from one question. Find yours here.

| The question in front of you | The sheet |
|------------------------------|-----------|
| Which database? | [SQL vs NoSQL](sql-vs-nosql.md), then [PostgreSQL vs DynamoDB vs Cassandra](postgres-vs-dynamodb-vs-cassandra.md) |
| Do I know every query up front? | [DynamoDB vs MongoDB](dynamodb-vs-mongodb.md) |
| Which cache, and how does it stay correct? | [Redis vs Memcached](redis-vs-memcached.md), [caching strategies](caching-strategies.md) |
| A log, a broker, or a managed queue? | [Kafka vs RabbitMQ vs SQS](kafka-vs-rabbitmq-vs-sqs.md), [Kafka vs Kinesis vs Pub/Sub](kafka-vs-kinesis-vs-pubsub.md) |
| Which API style? | [REST vs gRPC vs GraphQL](rest-vs-grpc-vs-graphql.md) |
| How do updates reach the client? | [WebSockets vs SSE vs long polling](websockets-vs-sse-vs-long-polling.md) |
| Which read may be stale? | [Strong vs eventual consistency](strong-vs-eventual-consistency.md) |
| How do I split the data? | [Sharding strategies](sharding-strategies.md) |
| Write the feed, or build it on read? | [Push vs pull feeds](push-vs-pull-feeds.md) |
| How do I count requests per client? | [Rate limiting algorithms](rate-limiting-algorithms.md) |
| Which layer does the balancer work at? | [L4 vs L7 load balancing](l4-vs-l7-load-balancing.md) |
| What is this called in the other cloud? | [AWS vs GCP vs Azure](aws-vs-gcp-vs-azure.md) |

## Running the interview

How to structure the round, what earns signal, and what loses it.

| Sheet | What it answers | Status |
|-------|-----------------|--------|
| [The interview framework](interview-framework.md) | What do I do, in what order, and for how long? | Written |
| [System design in one page](system-design-in-one-page.md) | Can I see the framework, patterns, and numbers at once? | Written |
| [Non-functional requirements](non-functional-requirements.md) | Which qualities should I clarify before designing? | Written |
| [Interview communication tips](communication-tips.md) | How do I come across as senior while I think out loud? | Written |
| [Common mistakes and anti-patterns](common-mistakes.md) | What sinks candidates who know the material? | Written |
| [Senior vs staff expectations](senior-vs-staff-expectations.md) | Why does the same answer get graded differently by level? | Written |
| [A mock interview, annotated](mock-interview-walkthrough.md) | Where exactly does the hire and no-hire line sit? | Written |

## Numbers and recall

The things you need loaded in memory, not looked up.

| Sheet | What it answers | Status |
|-------|-----------------|--------|
| [Back-of-the-envelope estimation](estimation.md) | How do I size traffic, storage, and bandwidth quickly? | Written |
| [Latency numbers](latency-numbers.md) | How slow is each layer, and what does that force on the design? | Written |
| [Core components reference](core-components.md) | What are the building blocks, and when do I reach for each? | Written |
| [Trade-off decision guides](trade-offs.md) | What is the one-line answer to each common "X vs Y"? | Written |
| [Flashcards](flashcards.md) | Where are the gaps in my recall? | Written |

## Choosing a technology

The comparison sheets. Each one starts from the question you should ask first, then gives the decision you can say out loud.

| Sheet | The question it starts from | Status |
|-------|-----------------------------|--------|
| [SQL vs NoSQL](sql-vs-nosql.md) | What are the access patterns? | Written |
| [PostgreSQL vs DynamoDB vs Cassandra](postgres-vs-dynamodb-vs-cassandra.md) | Relational, managed key-value, or write-optimized? | Written |
| [DynamoDB vs MongoDB](dynamodb-vs-mongodb.md) | Do you know every query up front, or will they evolve? | Written |
| [Redis vs Memcached](redis-vs-memcached.md) | Do you need anything besides GET and SET? | Written |
| [Kafka vs RabbitMQ vs SQS](kafka-vs-rabbitmq-vs-sqs.md) | Does the consumer need a log, routing, or just a queue? | Written |
| [Kafka vs Kinesis vs Pub/Sub](kafka-vs-kinesis-vs-pubsub.md) | Whose log is it, and do you need replay? | Written |
| [REST vs gRPC vs GraphQL](rest-vs-grpc-vs-graphql.md) | Who is the client, and do you control it? | Written |
| [WebSockets vs SSE vs long polling](websockets-vs-sse-vs-long-polling.md) | Which direction do messages go, and how often? | Written |
| [AWS vs GCP vs Azure](aws-vs-gcp-vs-azure.md) | What is this service called in the interviewer's cloud? | Written |
| [Caching strategies](caching-strategies.md) | Who writes to the cache, and when? | Written |
| [Push vs pull feeds](push-vs-pull-feeds.md) | Do you pay for fan-out at write time or read time? | Written |
| [Rate limiting algorithms](rate-limiting-algorithms.md) | Do you need to allow bursts, and how much memory can you spend per client? | Written |
| [Sharding strategies](sharding-strategies.md) | What do you shard on, and which query breaks if you choose wrong? | Written |
| [Strong vs eventual consistency](strong-vs-eventual-consistency.md) | Which read is allowed to be stale, and who would notice? | Written |
| [L4 vs L7 load balancing](l4-vs-l7-load-balancing.md) | Does the balancer need to read the request to decide? | Written |

## How these fit with the rest of the repo

The comparison sheets are the decision; the [patterns](../patterns/) are the mechanism. When a sheet tells you to pick WebSockets, the [long polling, WebSockets, and SSE pattern](../patterns/long-polling-websockets-sse.md) explains how each one actually works. Read the pattern once, then keep the sheet for the interview.

The same split holds for the [questions](../questions/): a walkthrough shows the framework applied end to end, and [the framework sheet](interview-framework.md) is what you carry into a question you have never seen.

## Add a new cheat sheet

1. For a comparison, copy [sql-vs-nosql.md](sql-vs-nosql.md): quick comparison table, then how to choose, then what to say in an interview.
2. For a reference or process sheet, copy [non-functional-requirements.md](non-functional-requirements.md).
3. Keep it to one screen of real content. A sheet that needs scrolling is a pattern page.
4. Add a row to the right table above, and a bullet to the cheat sheet list in the root [README](../README.md).

## Go deeper

- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=cheat-sheets-readme)
- Short on time: [System Design Interview Crash Course](https://www.designgurus.io/course/system-design-interview-crash-course?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=cheat-sheets-readme)
- Practice live: [Mock interviews with ex-FAANG engineers](https://www.designgurus.io/mock-interviews?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=cheat-sheets-readme)
