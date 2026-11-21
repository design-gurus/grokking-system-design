# Design Reddit

> A community platform with subreddits, posts, nested comments, voting, and ranked feeds.

## 1. Requirements

**Functional**
- Create posts in communities (subreddits).
- Nested comments (threads).
- Upvote and downvote posts and comments.
- Ranked feeds (hot, top, new).

**Non-functional**
- Read-heavy.
- Low-latency feeds.
- Eventual consistency on vote counts is fine.

## 2. Key challenges

- Vote counting at scale: votes are a high-volume counter problem (see the [likes counter](design-youtube-likes-counter.md) approach: sharded or aggregated, not one write per vote).
- Ranking: "hot" combines score and age so fresh, well-voted posts rise and decay over time. The rank is usually precomputed and cached, not computed per request.
- Nested comments: store a parent reference per comment; load a subtree and render the thread. Very deep threads are paginated or lazy-loaded.

## 3. Deep dive

- Feed generation: precompute ranked lists per subreddit, cache them, and refresh on a schedule rather than ranking on every read.
- Storage: posts and comments partitioned by subreddit or post id (see [sharding](../patterns/sharding-partitioning.md)).
- Caching: hot subreddit feeds and popular posts in a cache (see [caching](../patterns/caching.md)).

## 4. Trade-offs

- Vote accuracy vs write cost: aggregate counts, accept slight lag.
- Ranking freshness vs compute: recompute hot scores periodically.

## High-level design

```mermaid
flowchart LR
    Client --> App[App Servers]
    App --> Posts[(Posts + Comments)]
    App --> Votes[Vote Counter]
    App --> Feed[(Ranked Feed Cache)]
```

## Go deeper

- Full worked solution: the chapter [Designing Reddit](https://www.designgurus.io/course-play/grokking-system-design-interview-ii/doc/design-reddit-new?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-design-reddit) in [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-design-reddit), a 7-step walkthrough.
- The frontend design: the lesson [Design a News Feed](https://www.designgurus.io/course-play/grokking-the-modern-frontend-system-design-interview/doc/design-a-news-feed?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-design-reddit) in [Grokking the Modern Frontend System Design Interview](https://www.designgurus.io/course/grokking-the-modern-frontend-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-design-reddit).
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-design-reddit)
