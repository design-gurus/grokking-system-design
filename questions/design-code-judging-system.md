# Design a code judging system

> Accept code submissions, run them against test cases in a sandbox, and return a verdict, safely and at scale.

## 1. Requirements

**Functional**
- Accept a submission (code plus problem id).
- Run it against hidden test cases.
- Return a verdict (accepted, wrong answer, time limit exceeded, runtime error).

**Non-functional**
- Run untrusted code safely (isolation).
- Scale to bursts (contests).
- Fair and timely results.

## 2. Key challenges

- Sandboxing: untrusted code must run isolated, with strict CPU, memory, and time limits, no network, and no host access (containers or microVMs).
- Queueing: submissions go to a [queue](../patterns/message-queues.md); a pool of judge workers pulls and executes them, so spikes are absorbed.
- Test cases: stored centrally; workers fetch the problem's tests, run the code, and compare output.

## 3. Deep dive

- Worker pool: each worker compiles and runs the submission in a fresh sandbox, enforces limits, then reports the verdict.
- Security: drop privileges, disable networking, cap resources, and destroy the sandbox after each run.
- Contests: a spike of submissions is handled by scaling workers and prioritizing the queue.
- Determinism: pin language and runtime versions so results are reproducible.

## 4. Trade-offs

- Isolation strength vs startup cost: stronger sandboxes (microVMs) are safer but slower to start; pooling helps.
- Throughput vs fairness: prioritize and rate-limit so one user cannot starve others.

## Go deeper

- For the full worked solution: [Advanced System Design Interview, Volume II](https://www.designgurus.io/course/grokking-system-design-interview-ii)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)