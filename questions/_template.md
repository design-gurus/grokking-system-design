# Design [System]

<!-- Before you commit: replace questions-QUESTION-SLUG in the designgurus.io links below with this file path, slashes turned into dashes and .md dropped. -->

> One-line description of what the system does.

## 1. Requirements

**Functional**
- What the system must do (the core use cases).

**Non-functional**
- Scale, latency, availability, consistency expectations.

## 2. Estimation

Rough numbers: users, requests per second, reads vs writes, storage per year. See the [estimation cheat sheet](../cheat-sheets/estimation.md).

## 3. API

List the core endpoints (name, inputs, outputs).

## 4. Data model

The main entities and how they relate. Note the access patterns that drive the choice of store.

## 5. High-level design

A short description plus a simple diagram:

```
[client] --> [load balancer] --> [service] --> [data store]
```

## 6. Deep dive

Pick one or two interesting parts (for example the hot path, the data partitioning, or the consistency model) and go deeper.

## 7. Bottlenecks and trade-offs

What breaks first at scale, and how you would address it. Reference the [patterns](../patterns/) you used.

## Go deeper

<!-- Lead with the course lesson that solves this problem. Link the lesson itself at /course-play/COURSE-SLUG/doc/LESSON-SLUG and use its exact title. Then add lessons from other courses that cover the same problem from another angle (API, frontend, mobile, microservices, Redis, Kafka). If no lesson matches, link the course instead. Free blog posts go last. -->

- Full worked solution: the lesson [LESSON TITLE](https://www.designgurus.io/course-play/grokking-the-system-design-interview/doc/LESSON-SLUG?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-QUESTION-SLUG) in [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=questions-QUESTION-SLUG).
