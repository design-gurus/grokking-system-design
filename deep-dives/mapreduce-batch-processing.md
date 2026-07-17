# MapReduce: batch processing at scale

> Google's programming model that let ordinary engineers run computations across thousands of machines by writing two functions.

## What it is

MapReduce is a programming model plus runtime for processing huge datasets on clusters of commodity machines. The user writes a map function (transform each record into key-value pairs) and a reduce function (combine all values for a key); the framework handles distribution, parallelism, and failures. It powered Google's indexing pipeline, spawned Hadoop, and its ideas live on in Spark and every [batch processing](../patterns/batch-vs-stream-processing.md) system since.

## The problem it solves

Before MapReduce, every large computation at Google (build the index, analyze logs) was a bespoke distributed program where most of the code handled partitioning, scheduling, and machine failures rather than the actual computation. MapReduce factored that machinery out once, so a thousand-machine job became a few dozen lines of application code.

## Key design ideas

| Idea | How it works |
|------|--------------|
| Two-phase model | Map tasks process input splits in parallel; output is partitioned by key; reduce tasks pull, sort, and aggregate each partition |
| Shuffle | The all-to-all exchange between mappers and reducers, grouping every value for a key onto one reducer; it is the expensive middle of every job |
| Data locality | The master schedules map tasks on machines already holding the input block (via [GFS](gfs-distributed-file-system.md)), moving computation to data |
| Failure handling by re-execution | Tasks are deterministic and idempotent, so a failed task is simply rerun elsewhere; no distributed recovery protocol needed |

## Notable techniques

- Stragglers: one slow machine can stall a whole job, so near the end the master launches backup (speculative) copies of the last tasks and takes whichever finishes first.
- Combiners: pre-aggregate map output locally (a mini-reduce) to shrink shuffle traffic for associative operations like counting.
- Skew: one hot key (one giant reduce partition) dominates job time; real pipelines salt or split hot keys.

## Trade-offs

Every stage writes to disk, which makes jobs robust but slow; iterative algorithms (like ML training) pay the disk tax per iteration, which is exactly what Spark fixed with in-memory datasets. The rigid map-then-reduce shape also forces multi-stage pipelines into chains of jobs. And it is batch by definition: results arrive when the job ends, which is why [stream processing](../patterns/batch-vs-stream-processing.md) exists alongside it.

## Go deeper

- For the full deep dive: [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)