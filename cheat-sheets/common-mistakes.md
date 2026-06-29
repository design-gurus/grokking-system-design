# Common mistakes and anti-patterns

The mistakes that sink system design interviews, and how to avoid each. Most are about process and communication, not missing knowledge.

| Mistake | Why it hurts | The fix |
|---------|--------------|---------|
| Jumping straight into design | You solve the wrong problem | Clarify requirements and scope first (see the [framework](interview-framework.md)) |
| Skipping estimation | The design is not grounded in scale | Do a quick [back-of-the-envelope](estimation.md) with numbers |
| Designing in silence | The interviewer cannot follow your thinking | Think out loud (see [communication tips](communication-tips.md)) |
| Over-engineering | Wasted time and added risk | Start simple, add complexity only when a requirement demands it |
| Ignoring non-functional requirements | You miss what the system must be | State scale, latency, availability, and consistency targets ([NFRs](non-functional-requirements.md)) |
| Buzzword-driven choices | "I will use NoSQL because it scales" signals shallow thinking | Justify every choice from the access patterns ([SQL vs NoSQL](sql-vs-nosql.md)) |
| Not discussing trade-offs | You look like you do not understand the costs | Name the [trade-off](trade-offs.md) and why you chose your side |
| Rabbit-holing on one detail | You run out of time | Cover the whole design first, then go deep |
| Ignoring interviewer hints | You miss the path they want | Treat questions and nudges as signals, and follow them |
| Forgetting bottlenecks and failure | The design does not survive scale | Always end with bottlenecks, scaling, and what happens when a component fails |
| No structure | The answer wanders | Use the [framework](interview-framework.md) as your spine |

## The meta-lesson

Most failed system design interviews are not about missing knowledge. They are about poor process: not clarifying, not communicating, not managing time, and not discussing trade-offs. Fix the process and your existing knowledge goes much further.

## Go deeper

- Practice live: [mock interviews with ex-FAANG engineers](https://www.designgurus.io/mock-interviews)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)