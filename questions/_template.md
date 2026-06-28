# Design [System]

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

Link to the full worked solution in the [course](https://www.designgurus.io/course/grokking-the-system-design-interview).