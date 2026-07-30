# Low-level design (object-oriented design)

Where [system design](../questions/) asks *how do the boxes fit together at scale*, **low-level design (LLD)** asks *how do the classes inside one box fit together*. It's the object-oriented design (OOD) round: given a problem like "design a parking lot," you produce the classes, their relationships, the key methods, and the design patterns that keep it clean and extensible.

These rounds are common at many companies (especially for backend and senior roles) and reward a different skill than HLD: modeling a domain in code, applying [SOLID](#the-solid-principles), and reaching for the right [design pattern](#design-patterns-worth-knowing) without over-engineering.

## The problems

| Problem | Core idea | Patterns it exercises |
|---------|-----------|-----------------------|
| [Parking lot](parking-lot.md) | Model spots, vehicles, tickets, pricing | Strategy, Factory, Singleton |
| [Elevator system](elevator-system.md) | Scheduling requests across cars | State, Strategy, Observer |
| [LRU cache](lru-cache.md) | O(1) get/put with eviction | Hash map + doubly linked list |
| [Rate limiter](rate-limiter.md) | Allow/deny under a rate, in code | Strategy, token bucket |
| [Vending machine](vending-machine.md) | A classic finite state machine | State, Strategy |
| [In-memory key-value store](key-value-store.md) | Thread-safe store with TTL | Concurrency, expiry |

To add one, copy [_template.md](_template.md).

## How to approach an LLD question

A repeatable structure, much like the [HLD framework](../cheat-sheets/interview-framework.md) but at the class level:

1. **Clarify requirements and scope.** What must it do? What's explicitly out of scope? Nail down the use cases before drawing classes.
2. **Identify the core objects (nouns).** Entities become classes; the things they do (verbs) become methods. "A parking lot has levels; a level has spots; a spot holds a vehicle" → `ParkingLot`, `Level`, `ParkingSpot`, `Vehicle`.
3. **Define relationships.** Association, aggregation, composition, inheritance. Prefer **composition over inheritance**.
4. **Sketch the class diagram.** Classes, key fields, key methods, and the arrows between them. A [Mermaid `classDiagram`](https://mermaid.js.org/syntax/classDiagram.html) is perfect here — every problem below has one.
5. **Walk a use case through the methods.** "Park a car" → which objects collaborate, in what order. This surfaces missing methods.
6. **Apply patterns where they earn their place.** Pricing that varies → [Strategy](#design-patterns-worth-knowing); object creation that varies → Factory; one shared instance → Singleton. Name the pattern and *why*.
7. **Handle concurrency and edge cases.** Two cars for the last spot; a full lot; thread safety. State your assumptions.

## The SOLID principles

The five ideas interviewers listen for:

- **S — Single responsibility**: a class has one reason to change.
- **O — Open/closed**: open for extension, closed for modification (add a new `PricingStrategy`, don't edit the old one).
- **L — Liskov substitution**: subtypes must be usable anywhere their base type is.
- **I — Interface segregation**: many small interfaces beat one fat one.
- **D — Dependency inversion**: depend on abstractions, not concretions (inject a `PricingStrategy` interface, not a concrete class).

## Design patterns worth knowing

The handful that show up again and again in LLD rounds:

| Pattern | Use when | Example here |
|---------|----------|--------------|
| **Strategy** | An algorithm varies and should be swappable | Parking [pricing](parking-lot.md), [rate-limit](rate-limiter.md) algorithm |
| **Factory** | Object creation varies by input | Creating the right `Vehicle`/`ParkingSpot` |
| **Singleton** | Exactly one shared instance | The [parking lot](parking-lot.md) controller |
| **Observer** | Many objects react to a state change | [Elevator](elevator-system.md) display updates |
| **State** | Behavior depends on an internal mode | [Vending machine](vending-machine.md), elevator car |
| **Decorator** | Add behavior without subclassing | Wrapping a store with metrics/TTL |

Don't force a pattern in. The senior move is reaching for one only when it removes real duplication or a real "if/else on type" smell.

## Go deeper

- Related: the [system design questions](../questions/) (the HLD counterpart) and [patterns](../patterns/).
- Read more (free): [Object-Oriented Design Interview](https://www.designgurus.io/blog/object-oriented-design-ood-interview)
- Full course: [Grokking the Low Level Design (LLD) Interview](https://www.designgurus.io/course/grokking-the-low-level-design-interview-using-ood)
