# Flink: stateful stream processing

> Compute continuously over unbounded streams, keep large state, and still get correct results after a crash.

## What it is

Apache Flink is a distributed stream processor. Its landmark contribution is treating streaming as the general case and batch as a special case: a batch job is just a stream that happens to end (a bounded stream). What sets it apart from a simple consumer loop is that it offers real state and real correctness guarantees instead of best-effort aggregation.

## The problem it solves

Aggregating a never-ending stream raises three questions that simple consumers quietly ignore. When is a time window complete, given that events arrive late and out of order? Where does the running state live once it is too big to hold in memory? And what happens to that state when a machine dies halfway through the computation? Flink answers all three, and the answers are what make the model worth its cost.

## Key design ideas

| Idea | How it works |
|------|--------------|
| Event time vs processing time | Event time is when the thing actually happened. Processing time is when your machine saw it. Correct results need event time, because the network delivers events late and out of order |
| Watermarks | A watermark is a moving assertion that no event older than time T will still arrive. A watermark passing the end of a window is what lets that window close and emit. Events that arrive after it follow a stated policy: drop them, or update the result already emitted |
| Windows | Tumbling windows are fixed buckets that do not overlap. Sliding windows are fixed size but emitted on a shorter step, so they overlap. Session windows group events by gaps of inactivity, with no fixed size |
| Keyed state | Each key gets its own running state, stored locally in an embedded key-value store (RocksDB), so total state can far exceed memory |
| Distributed snapshots | A barrier flows through the dataflow graph, and each operator snapshots its state as the barrier passes. That produces one consistent checkpoint without stopping the stream. This is the Chandy-Lamport idea applied to a running job |

## What exactly-once really means

Checkpoints restore operator state exactly. After a crash, Flink rewinds the source to the last checkpoint, replays from there, and the internal state ends up as if the crash never happened. That is not the whole story. End-to-end exactly-once also needs the sink to be transactional (commit its output only when the checkpoint completes) or [idempotent](../patterns/idempotency.md), because a replay will re-emit the same output records. Say this plainly in an interview: exactly-once is a property of the whole pipeline, not a checkbox on one component.

## Notable techniques

- Checkpoint barriers and alignment: an operator with two inputs waits for the barrier on both before it snapshots, so the checkpoint reflects a single consistent cut across the job.
- Savepoints: a checkpoint you take deliberately and keep, used for planned upgrades, code changes, and parallelism changes. It is the difference between a job you can evolve and a job you can only restart.
- Natural backpressure: each operator reads from a bounded buffer, so a slow operator fills its buffer and the slowdown travels up the graph to the source with no extra protocol. See [backpressure](../patterns/backpressure.md).
- Rescaling: keyed state is grouped into key groups, so adding or removing workers redistributes whole groups rather than rebuilding state from scratch.
- Replay depends on a source you can re-read, which is why a durable log like [Kafka](../deep-dives/kafka-distributed-messaging.md) is the usual partner.

## Trade-offs

You get correct, stateful, low-latency stream processing. You pay in operational complexity. Checkpoint intervals need tuning, large state makes checkpoints slower, and restart time grows with state size because state must be reloaded before the job catches up. The programming model is also steeper than a queue consumer.

Be honest about when it is overkill. If your job is stateless per message (validate it, enrich it, forward it), a plain consumer is simpler and you should say so. The [batch vs stream](../patterns/batch-vs-stream-processing.md) decision comes before the tool choice. Flink earns its complexity in problems like [designing an ad click aggregator](../questions/design-ad-click-aggregator.md) and [designing a metrics and monitoring system](../questions/design-metrics-monitoring.md), where windowed counts have to be right and late-arriving events are normal, not exceptional.

## Go deeper

- For the full deep dive: [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=deep-dives-flink-stream-processing)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=deep-dives-flink-stream-processing)
