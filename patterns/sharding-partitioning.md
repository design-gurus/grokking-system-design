# Sharding and partitioning

> Split a dataset across multiple machines so it can grow beyond what a single database can hold or serve.

## What it is

Partitioning divides a large dataset into smaller pieces. Sharding is horizontal partitioning across separate database servers (shards), where each shard holds a subset of the rows. It is how you scale writes and storage past the limit of one machine.

## Partitioning strategies

| Strategy | How it works | Watch out for |
|----------|--------------|---------------|
| Range based | Partition by a key range (for example A to M, N to Z) | Hot ranges and uneven load |
| Hash based | Hash the key to choose a shard | Hard to do range queries; resharding is costly |
| Consistent hashing | Hash onto a ring to limit data movement | More complex (see [consistent hashing](consistent-hashing.md)) |
| Directory based | A lookup service maps keys to shards | The directory becomes a critical dependency |

## Choosing a shard key

The shard key decides everything. A good key spreads load evenly and keeps related data together. A poor key creates hot shards (one shard taking most of the traffic) or forces queries to fan out across every shard.

## Trade-offs

| Pro | Con |
|-----|-----|
| Scales writes and storage horizontally | Cross-shard queries and joins are hard |
| Limits the blast radius of a failure | Rebalancing and resharding are operationally painful |
| Each shard is smaller and faster | Transactions across shards are complex |

## How to talk about it in an interview

Name the shard key and justify it from the access patterns, explain how you avoid hot shards, and say how you would reshard when a shard gets too big. Mentioning the cost of cross-shard queries is a strong signal.

## Go deeper

- Read more (free): [Database Sharding Guide](https://www.designgurus.io/blog/database-sharding-guide-2026)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)