# Consistency models

> The contract for what a read is allowed to return when data is replicated and being written concurrently.

## What it is

A consistency model defines how up to date and ordered reads are across replicas. Stronger models are easier to reason about but cost latency and availability; weaker models are faster and more available but can return stale or out-of-order data.

## The spectrum (strong to weak)

| Model | What it guarantees |
|-------|--------------------|
| Linearizable (strong) | Every read sees the most recent write, as if there were one copy |
| Sequential | All clients see operations in the same order, not necessarily the latest |
| Causal | Operations that are causally related are seen in order; unrelated ones may differ |
| Read your writes | A client always sees its own writes |
| Eventual | Replicas converge over time; a read may be stale until they do |

## Common session guarantees

These make eventual consistency usable in practice:

- Read your writes: you always see your own updates.
- Monotonic reads: you never see time go backward across reads.
- Monotonic writes: your writes apply in order.

## How to choose

Pick the weakest model the product can tolerate, because weaker is faster and more available. A bank balance wants linearizable. A like counter is fine with eventual. State the staleness budget explicitly.

## How to talk about it in an interview

Name the model per piece of data, not for the whole system. Tie it to [replication](replication.md) and the [CAP theorem](cap-theorem.md): the model you can offer depends on how you replicate and what you do during a partition.

## Go deeper

- For harder, distributed-systems depth: [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)