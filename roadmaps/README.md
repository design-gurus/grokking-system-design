# Roadmaps

Pick the plan that fits your timeline or your role, or the refresher if you have interviewed before.

| Plan | Best when | Time |
|------|-----------|------|
| [1-day plan](1-day-plan.md) | Your interview is tomorrow | About 6 hours, once |
| [1-week crash plan](1-week-plan.md) | Your interview is days away | 2 to 3 hours per day |
| [2-week sprint](2-week-plan.md) | You have a couple of weeks | 1 to 2 hours per day |
| [6-week study plan](6-week-plan.md) | You are building depth from a baseline | About 1 hour per day |
| [3-month study plan](3-month-plan.md) | You start from zero, or you work full time | 30 to 45 minutes per day |
| [New grad and junior plan](new-grad-plan.md) | You face an entry-level round | About 45 minutes per day, 4 weeks |
| [Engineering manager plan](engineering-manager-plan.md) | You are in a management loop | About 1 hour per day, 3 weeks |
| [Senior and staff refresher](senior-staff-refresher.md) | You have done this before and are rusty | 6 to 10 hours total |

```mermaid
flowchart TD
    Q1{"Have you interviewed<br/>for system design before?"}
    Q1 -->|"yes, but not recently"| REF["Senior and staff refresher<br/>6 to 10 hours"]
    Q1 -->|"no, or not successfully"| Q0{"Which describes you?"}
    Q0 -->|"student or<br/>under 2 years"| NG["New grad and<br/>junior plan"]
    Q0 -->|"manager or<br/>tech lead"| EM["Engineering<br/>manager plan"]
    Q0 -->|"engineer"| Q2{"How long<br/>until the interview?"}
    Q2 -->|"one day"| D1["1-day plan"]
    Q2 -->|"days"| W1["1-week plan"]
    Q2 -->|"two weeks"| W2["2-week sprint"]
    Q2 -->|"a month<br/>or more"| W6["6-week plan"]
    Q2 -->|"three months"| M3["3-month plan"]
```

## How much each plan covers

The repo holds 30 patterns, 60 questions, and 19 deep dives. No plan covers all of it, and choosing what to leave out is most of what a plan does for you.

| Plan | Patterns | Questions | Deep dives |
|------|----------|-----------|------------|
| 1-day plan | 4 | 2 | none |
| 1-week crash plan | 8 | 5 | none |
| 2-week sprint | 11 | 5 | optional skim |
| 6-week study plan | all 30 | about 18 | all 19, in reading order |
| 3-month study plan | all 30 | 8 timed | 4 selected |
| New grad and junior plan | 8 | 4, plus 2 in mocks | none |
| Engineering manager plan | 10 | 4 timed, plus 1 recorded | none |
| Senior and staff refresher | only your gaps | 3 timed | only your gaps |

The timeline plans and the two role plans share one order: learn the [framework](../cheat-sheets/interview-framework.md) and [patterns](../patterns/) first, then practice with [questions](../questions/), then do timed [mock interviews](https://www.designgurus.io/mock-interviews?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design&utm_content=roadmaps-readme).

The refresher inverts that. It assumes you already know the material, so it starts with a recorded diagnostic to find your actual gaps, and then fixes only those.

## What every plan has in common

Whichever one you pick, three things do most of the work:

1. **The [interview framework](../cheat-sheets/interview-framework.md) comes first.** It is what carries you through a question you have never seen, which is the situation you should plan for.
2. **Practice means out loud, timed, from a blank page.** Reading a walkthrough teaches you the answer. It does not teach you the performance, and the performance is what is graded.
3. **At least one timed mock before the real round.** The first mock usually goes badly for reasons unrelated to knowledge. It is much better for that to happen in practice.
