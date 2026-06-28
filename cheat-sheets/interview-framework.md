# The system design interview framework

A repeatable structure you can apply to any question. Memorize the steps, not the answers. Below is a common pacing for a 45-minute round.

| Step | What you do | Time |
|------|-------------|------|
| 1. Requirements and scope | Clarify functional and non-functional needs; agree what is in and out of scope | 5 min |
| 2. Estimation | Back-of-the-envelope traffic, storage, and bandwidth | 3 min |
| 3. API | Define the core endpoints | 4 min |
| 4. Data model | Entities, relationships, and the store that fits the access patterns | 5 min |
| 5. High-level design | Draw the main components and the request flow | 10 min |
| 6. Deep dive | Go deep on one or two components the interviewer cares about | 13 min |
| 7. Bottlenecks and trade-offs | Identify what breaks first at scale and how you would fix it | 5 min |

## Step 1: Requirements and scope

- Functional: the core use cases (what the system must do).
- Non-functional: scale, latency, availability, consistency, durability.
- Explicitly state assumptions and confirm scope before designing. This is a top signal interviewers look for.

## Step 2: Estimation

Translate the scale into numbers: requests per second, read-to-write ratio, storage per year. Use round numbers. See the [estimation cheat sheet](estimation.md).

## Step 3: API

Keep it small and clear. Name each endpoint with inputs and outputs. The API often reveals the data model.

## Step 4: Data model

Pick the store based on access patterns, not habit. Justify SQL vs NoSQL (see [SQL vs NoSQL](sql-vs-nosql.md)).

## Step 5: High-level design

Draw boxes and arrows: clients, load balancer, services, stores, caches, queues. Walk the interviewer through one request end to end.

## Step 6: Deep dive

Let the interviewer steer. Common deep dives: the hot read path, data partitioning, the consistency model, or how you handle a specific failure.

## Step 7: Bottlenecks and trade-offs

Name the first bottleneck at scale and your fix. Reference [patterns](../patterns/) (caching, sharding, replication, queues). Stating trade-offs out loud is what separates strong candidates.

## Go deeper

- Short on time? [System Design Interview Crash Course](https://www.designgurus.io/course/system-design-interview-crash-course)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)