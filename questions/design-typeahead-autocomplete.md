# Design typeahead / autocomplete

> Suggest completions as a user types, ranked by popularity, with very low latency.

## Requirements

- Return suggestions for a prefix within a few milliseconds.
- Rank by popularity or relevance.
- Update suggestions as new queries trend.
- Scale to high query volume.

## Key ideas

- Data structure: a trie (prefix tree) maps prefixes to top completions. To stay fast, precompute and store the top N completions at each node rather than searching on every keystroke.
- Serving: keep the trie or precomputed prefix-to-suggestions map in memory and fronted by a cache, so each keystroke is a fast lookup.
- Ranking: completions are ranked by frequency, computed from a stream of past queries and refreshed periodically.
- Scale: shard by prefix; most traffic hits a small set of popular prefixes, which cache well.

## Go deeper

- Quick, focused prep: [System Design Interview Crash Course](https://www.designgurus.io/course/system-design-interview-crash-course)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)