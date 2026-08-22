# Elasticsearch and Lucene: search internals

> How full-text search actually works, from the inverted index up to a distributed search cluster.

## What it is

Lucene is a search library. It builds the index, scores documents, and returns matches, all inside one process on one machine. Elasticsearch is the distributed system wrapped around Lucene: it shards the data, replicates it, and exposes it over an HTTP API. Almost every search system people build is one of these two layers, so it helps to know which layer a problem belongs to.

## The problem it solves

A database index answers "find rows where this column equals X". Search asks a different question: "find documents relevant to these words". That needs the text broken into words, ranked by how well each document matches, and returned fast over millions of documents. A B-tree, the sorted tree structure behind most [database indexes](../patterns/database-indexing.md), cannot do this. It finds an exact value well, but it has no notion of relevance and no way to match one word buried inside a long paragraph.

## Key design ideas

| Idea | How it works |
|------|--------------|
| Inverted index | Map each term to the sorted list of document ids that contain it (a posting list). A query intersects a few posting lists instead of scanning every document |
| Analysis chain | At index time the text is tokenized (split into words), lowercased, stripped of stop words, and stemmed (cut back to a root form), so "running" and "runs" both match "run" |
| Relevance scoring | A term counts for more when it appears often in one document and rarely across the whole collection, then the score is adjusted down for long documents. BM25 is the modern default |
| Immutable segments | Each flush writes a new segment file that is never modified. A search reads many segments and merges the results. Deletes are tombstones (markers) applied later |
| Translog | A [write-ahead log](../patterns/write-ahead-log.md) records every write before the segment is flushed, so an acknowledged write survives a crash |

## The distributed layer

An Elasticsearch index is split into shards ([partitions](../patterns/sharding-partitioning.md)), and each shard is a complete, independent Lucene index. Each shard also has [replicas](../patterns/replication.md) for failover and extra read capacity. A query runs as scatter-gather: the coordinating node sends it to one copy of every shard, each shard returns its own best K hits (K being the number of results requested), and the coordinator merges those lists into the final answer.

Two consequences follow. Deep pagination is expensive, because asking for page 100 forces every shard to return 100 pages worth of hits so the merge is correct, and the cost grows with the page number. Scoring is also approximate, because the term statistics that drive relevance (how rare a word is) are counted per shard rather than globally, so two shards can score the same document differently. A [web search design](../questions/design-google-search.md) runs into both problems.

## Notable techniques

- Near-real-time search: a refresh opens a new segment and makes recent writes visible, usually after about a second. Search is not instant after a write, and that is a deliberate trade-off for write throughput.
- Segment merging: a background process combines small segments into larger ones, drops tombstoned documents, and keeps the number of segments a query must touch low. It is the same compaction idea used by log-structured storage engines.
- Filters versus queries: a filter ("published is true") gives a yes or no answer, is never scored, and can be cached as a bit array and reused across requests. A scored query cannot be cached that way, so push every condition you can into filters.
- A forced merge down to a single segment before a read-only workload gives the fastest possible queries, paid for with one heavy rewrite.
- Prefix and edge-ngram indexes turn the same machinery into [typeahead autocomplete](../questions/design-typeahead-autocomplete.md).

## Trade-offs

You get fast and very flexible text search. You pay with eventual visibility of writes, heavy memory and disk use (the index is often larger than the source text), an index that is hard to reshape because the shard count is fixed when the index is created, and relevance scores that are only approximate across shards.

Keyword search has one more real limit: it matches words, not meaning. A query worded differently from the document simply misses. Vector search covers that gap, and hybrid retrieval that runs both and merges the results usually beats either one alone, which is why [semantic search designs](../questions/design-semantic-search.md) keep an inverted index alongside the vector index.

## Go deeper

- Related deep dive: [HNSW and vector search](./hnsw-vector-search.md)
- For the full deep dive: [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)
