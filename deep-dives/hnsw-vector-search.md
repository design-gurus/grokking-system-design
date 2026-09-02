# HNSW and vector databases

> Find the nearest vectors among billions, fast, by giving up the guarantee that they are exactly the nearest.

## What it is

HNSW (hierarchical navigable small world) is a graph index for nearest-neighbor search. It sits underneath most vector databases and most vector search features added to existing databases. A vector database is the storage system built around such an index: it adds metadata filtering, persistence, replication, and updates on top of the raw search structure.

## The problem it solves

An embedding is a list of numbers a model produces for a piece of text, an image, or code, arranged so that similar meaning lands at nearby points. Search then becomes "find the points nearest the query point". Exact nearest-neighbor search compares the query against every stored vector, which costs time linear in corpus size and does not work at a billion vectors. The familiar structures fail here too: [database indexes](../patterns/database-indexing.md) split on one dimension at a time, and in high dimensions the distances between points become nearly uniform, so a split no longer separates anything. The escape is approximation. Accept that a true neighbor is occasionally missed, and search time drops to something close to logarithmic.

## Key design ideas

| Idea | How it works |
|------|--------------|
| Proximity graph | Each vector is a node linked to its near neighbors; a search starts at some node and greedily walks to whichever neighbor is closer to the query |
| Hierarchy of layers | Upper layers hold few nodes with long links for large jumps, lower layers are dense for fine search; it works like a skip list laid over space, and it is what makes the walk fast |
| M (build parameter) | How many neighbors each node keeps; a higher M raises recall and costs memory and build time |
| efSearch (query parameter) | How many candidates the walk keeps in play; higher means slower queries and higher recall |
| Recall versus latency | The main choice. What fraction of the true neighbors you must return is a product decision, not a tuning detail |

Two alternatives are worth knowing. IVF (inverted file index) groups the vectors into clusters and searches only the clusters nearest the query, which uses far less memory and shards cleanly. Product quantization compresses each vector into a short code so many more fit in memory, at some cost in accuracy. In practice these get combined: quantized vectors held inside an HNSW or IVF index is a common production shape.

## Notable techniques

- Filtered search is the hard part. Applying a metadata filter after the graph walk can return too few results, because the walk did not know it should have looked elsewhere. Applying it during the walk can disconnect the graph, since the only route to a good region may pass through filtered-out nodes. Pre-filtering versus post-filtering is a real design decision and a common interview probe: permission filtering in a [RAG pipeline](../questions/design-rag-pipeline.md) is exactly this problem.
- Deletes are tombstones. Other nodes' searches route through a node's edges, so those edges cannot be cleanly removed. A deleted vector is marked and skipped at query time, and the index is rebuilt on a schedule to reclaim the space.
- Memory is the binding constraint. The graph, and usually the vectors themselves, live in RAM, so capacity planning for [semantic search](../questions/design-semantic-search.md) starts with a memory estimate rather than a disk one.
- Keyword and vector retrieval are complements, not competitors. An inverted index like [Lucene](../deep-dives/elasticsearch-lucene.md) is better at exact terms, rare names, and identifiers; vectors are better at paraphrase. Hybrid retrieval, running both and merging the two ranked lists, is the production answer, including for a [code assistant](../questions/design-code-assistant.md) where symbol names matter as much as intent.

## Trade-offs

You get sub-linear search over billions of vectors. You pay with results that are approximate (recall below 100 percent, and you choose how far below), high memory use, index builds that are expensive in time and CPU, and updates and deletes awkward enough to need a rebuild schedule.

## Go deeper

- How this is used in an AI system, including the permission filtering trap: [vector indexes](https://github.com/design-gurus/grokking-ai-system-design/blob/main/building-blocks/vector-indexes.md)
- For the full deep dive: [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=deep-dives-hnsw-vector-search)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=deep-dives-hnsw-vector-search)
