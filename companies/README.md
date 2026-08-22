# Company-specific system design interviews

The same interview loop does not exist twice. Citadel budgets microseconds, ServiceNow probes upgrade safety, Anthropic hands you a problem its own teams are still solving, and Bloomberg asks "why this and not the alternative" until it finds bottom. These notes summarize how 122 companies actually run their system design rounds, so you can aim the [patterns](../patterns/) and [questions](../questions/) in this repo at the loop you are facing.

Each company page covers: how the round runs, the signature questions candidates report, what interviewers probe, and which patterns in this repo to review, with a link to the full company guide on DesignGurus.io for the complete round-by-round breakdown.

How to use these notes:

1. Read your company's page to learn the round's shape and register.
2. Review the linked [patterns](../patterns/README.md) until they are fluent.
3. Rehearse the signature questions using the [interview framework](../cheat-sheets/interview-framework.md).
4. Go deeper with the full company guide and the [course](https://www.designgurus.io/course/grokking-the-system-design-interview?utm_source=github&utm_medium=repo&utm_campaign=grokking-system-design).

## AI labs and AI infrastructure

- **[Anthropic](anthropic.md)**: Prompts wear AI framing (GPU clusters, inference batches) but the core problems are classic infrastructure: queuing, batching, routing, and failure handling, with the model treated as a black box.
- **[OpenAI](openai.md)**: You may face system design twice: a practical screen and a deeper onsite round.
- **[xAI](xai.md)**: Nearly every round except the hiring manager conversation involves coding, design, or practical infrastructure, and the boundary blurs: a design conversation can turn into "now implement that component." First-principles derivation beats recited reference architectures.
- **[Google DeepMind](google-deepmind.md)**: Software engineers get a Google-style design round with an ML accent; research engineers get the rarer conversation: designing the machinery of frontier AI itself (distributed training, evaluation harnesses, experiment infrastructure).
- **[Perplexity](perplexity.md)**: Every design question orbits AI search: RAG, retrieval, crawling freshness, LLM serving, and caching.
- **[Scale AI](scale-ai.md)**: The distinctive dimension is humans as a component in the architecture: slow, expensive, variable, and indispensable.
- **[Cursor (Anysphere)](cursor.md)**: Design conversations live where ML serving meets editor experience: latency budgets are perceptual (keystroke-visible), costs are per-keystroke, and cancellation is a first-class primitive because the user's next keypress invalidates in-flight work constantly.
- **[Databricks](databricks.md)**: Prompts start standard and then expand, layer after layer, until the interviewer finds where your understanding ends.
- **[Mistral AI](mistral-ai.md)**: Rounds center on production RAG and agentic systems, with cost/performance tradeoffs graded as the core discipline and the efficiency thesis (capability per dollar) as the house aesthetic.
- **[Cohere](cohere.md)**: The round runs on enterprise AI serving: multi-tenant models at low latency, retrieval with measured quality, and deployment into customer VPCs.
- **[Hugging Face](hugging-face.md)**: Design thinking is evaluated through take-homes and discussions rather than a whiteboard hour, drawn from Hub-scale problems: hosting a million models, serving open weights, and library architecture where APIs are public contracts and backward compatibility is sacred.
- **[ElevenLabs](elevenlabs.md)**: The product decomposition round asks for the user experience and the system together, founder-style, for voice-product use cases.
- **[Groq](groq.md)**: Conversations run on inference-at-speed atop deterministic, compiler-scheduled silicon: execution time is knowable, which turns scheduling into bin-packing and admission control into a real-time capacity ledger that can make honest promises.
- **[Cerebras](cerebras.md)**: The round splits by team: cloud and platform roles get a classic distributed systems question, while systems software roles get lower-level design covering memory, scheduling, and data movement on unusual hardware.
- **[Harvey](harvey.md)**: Legal constraints are the grading rubric: results must respect matter-level permissions, and answers must cite the source text they came from.
- **[Runway](runway.md)**: Questions come straight from the product: multi-gigabyte video assets, GPU workers, and users who sit waiting while a render finishes.
- **[Sierra](sierra.md)**: The system design round replaced the coding screen, which the company has said publicly, so this session decides more of the result than at most places.
- **[Together AI](together-ai.md)**: Every question traces back to serving open-source models through an API: routing by model name, batching requests for GPU efficiency, and streaming tokens back one at a time.

## Big tech

- **[Apple](apple.md)**: Loops are team-designed rather than centrally standardized, so design rounds vary widely: consumer-scale services, on-device and privacy-conscious architectures, and media delivery all appear.
- **[Microsoft](microsoft.md)**: Design rounds are structured and rubric-driven like the rest of the loop: enterprise-scale services, collaboration and productivity systems, and Azure-flavored infrastructure, with clear communication scored alongside architecture.
- **[Netflix](netflix.md)**: Design conversations lean on streaming-scale realities: CDN strategy, personalization, and resilience engineering (this is the company that invented chaos engineering).
- **[Nvidia](nvidia.md)**: Design rounds are scoped to the team: data pipelines, serving systems, driver-adjacent components, or distributed training infrastructure.
- **[Tesla](tesla.md)**: Design questions carry first-principles grilling and physical-world texture: vehicle telemetry, fleet OTA updates, and real-time data pipelines, with interviewers pushing one level deeper than your resume claims.
- **[Adobe](adobe.md)**: Design runs at three altitudes: product architecture at creative-cloud scale, object-oriented low-level design, and database judgment, increasingly with a generative-AI accent (Firefly-style features with GPU economics inside consumer products).
- **[LinkedIn](linkedin.md)**: Product-centric prompts (feed, notifications, People You May Know) that are secretly graph problems: the key instinct is designing for extreme degree skew (most members have hundreds of connections; some have millions of followers).
- **[Oracle](oracle.md)**: Loops vary by organization: OCI runs a modern distributed-systems interview (multi-tenant cloud services, replication, consistency), while application orgs lean toward practical enterprise design.
- **[IBM](ibm.md)**: Three qualities decide this 45 to 60 minute round: scalability, reliability, and maintainability, and the last one carries unusual weight because the designs are expected to run for years inside banks and governments.

## Consumer, marketplace, and commerce

- **[Uber](uber.md)**: Marketplace systems with physical-world constraints: matching, location, pricing, and ETAs, where every design decision trades rider experience against driver earnings.
- **[Airbnb](airbnb.md)**: Two-sided marketplace design with inventory that is unique and calendar-bound: search and ranking over listings, booking consistency (no double-booked nights), and trust systems.
- **[DoorDash](doordash.md)**: Three-sided logistics at street level: consumers, Dashers, and merchants, with dispatch, ETAs, and pay systems as the native territory.
- **[Spotify](spotify.md)**: Spotify-flavored prompts (shuffle, notifications, podcast search, playlist sync) at streaming scale, with a communication bar that exceeds the algorithmic one: a clean medium solution narrated well outperforms a hard one delivered messily.
- **[Shopify](shopify.md)**: Commerce infrastructure with merchant obsession as the grading lens: designs are judged on how they protect a small business owner's sale.
- **[ByteDance / TikTok](bytedance-tiktok.md)**: Short-video planet scale: the For You feed backend, video upload and transcoding, and live-streaming infrastructure, with one grading behavior above the rest: justify tradeoffs explicitly, down to why you sacrificed consistency for availability during a viral spike.
- **[Reddit](reddit.md)**: Community-scale systems: feeds and ranking that balance engagement against community health, comment trees at enormous depth, and moderation tooling where volunteer moderators are load-bearing infrastructure.
- **[Roblox](roblox.md)**: Gaming-platform physics: real-time multiplayer state under human-reflex latency budgets, matchmaking and session placement, a real virtual economy, and safety systems for an audience heavy with minors.
- **[Discord](discord.md)**: The famous real-time canon: message fan-out where three-friend groups and million-member servers share one product surface, presence at hundreds of millions, and low-latency voice.
- **[Walmart Global Tech](walmart-global-tech.md)**: Retail at the world's largest scale: omnichannel inventory truth across 10,000+ stores and a digital catalog, Black Friday burst engineering, and supply-chain systems.
- **[Booking.com](booking-com.md)**: Selling the same room twice is treated as a real customer disaster, so correctness is graded ahead of raw scale.
- **[Dropbox](dropbox.md)**: Simplicity is graded directly, so adding queues, caches, and shards without a stated reason counts against you in this one hour round.
- **[Duolingo](duolingo.md)**: Prompts come straight from the product's own machinery: streaks, reminder timing, the experimentation platform, and the models that pick each exercise.
- **[eBay](ebay.md)**: Auction mechanics are the sharpest test in this loop: many bids on one item in the same second, a hard deadline, and exactly one winner.
- **[Epic Games](epic-games.md)**: Game constraints govern the hour: players notice delay above roughly 100 milliseconds and state updates arrive many times per second, so a design that works for a web shop can fail for a shooter.
- **[Expedia](expedia.md)**: Reported difficulty is easy to medium next to other large tech companies, so clean decomposition and steady narration carry the round more than exotic techniques.
- **[Instacart](instacart.md)**: The source of truth is a physical shelf the company does not control, and that one fact generates most of the round.
- **[Lyft](lyft.md)**: Different parts of one design get different guarantees, and saying so is the senior signal: locations may be slightly stale, trip and payment records may never be wrong.
- **[Snap](snap.md)**: Deletion is a first-class requirement here, so storage answers need a time to live and a delete path that survives a failed job.
- **[Twitch](twitch.md)**: Everything reduces to fan-out arithmetic said out loud: a million viewers times thousands of chat messages per second is billions of deliveries, and that number justifies every choice after it.
- **[Zoom](zoom.md)**: Two formats share the same 60 minute slot: a high-level architecture question, or a low-level one about the classes and API contracts inside a single service.

## Fintech and quantitative finance

- **[Stripe](stripe.md)**: API contracts and data models weigh more than boxes and arrows: a rigorous interface with a modest architecture beats the reverse.
- **[PayPal](paypal.md)**: Classic distributed-systems prompts steered by follow-ups into money-grade territory: idempotent payment processing, ledger consistency, reconciliation, and fraud-check placement in the transaction path.
- **[Robinhood](robinhood.md)**: Brokerage-grade correctness under consumer-scale experience: real-time market data to millions of app sessions, order paths where a bug is someone's money, and market-open bursts as the capacity benchmark.
- **[Ramp](ramp.md)**: Pragmatic fintech: card authorization under a hard latency budget, receipt matching as confidence-tiered automation, and integration-heavy systems where banks and accounting APIs are treated as unreliable dependencies.
- **[Citadel](citadel.md)**: A different sport from web-scale design: the unit of latency is the microsecond, the data source is a market-data firehose, and correctness bugs convert directly into lost money.
- **[Jane Street](jane-street.md)**: There is usually no classic whiteboard design round: systems thinking is evaluated inside long, evolving coding problems (the input no longer fits in memory; updates are now concurrent; the process can crash) and in design-review-style depth conversations for senior candidates.
- **[Two Sigma](two-sigma.md)**: The signature format is design-and-implementation: architect a small system, then build it as working code within the session, so designs must be buildable in an hour by you.
- **[Bloomberg](bloomberg.md)**: Consistently reported as the loop's hardest round: real-time financial systems probed with relentless "why this and not the alternative" follow-ups.
- **[Capital One](capital-one.md)**: Bank-grade constraints on cloud-native architecture: security, compliance, consistency, and fault tolerance are explicit evaluation criteria, and the business dimension surfaces even in design rounds (this is the company that gives engineers case interviews).
- **[Intuit](intuit.md)**: Money-grade correctness at consumer scale with the industry's most extreme seasonal burst: tax season compresses a year of traffic into weeks.
- **[Affirm](affirm.md)**: For senior roles, candidates report this round carries the most weight in the loop, and every question comes from the lending domain.
- **[Block (Square)](block-square.md)**: Every question is a money movement question, drawn from Square merchant payments, Cash App transfers, and Afterpay installments.
- **[Brex](brex.md)**: A stated company value, complexity is the enemy, shows up in the grading: a simple design defended with reasons scores better than extra services added to look impressive.
- **[Chime](chime.md)**: Mobile check deposit is the reported signature question, and it is not a photo upload problem: the hard part is clearing that takes days, the state machine around it, and money correctness.
- **[D. E. Shaw](d-e-shaw.md)**: Design sessions go mainly to senior candidates, one 45 to 60 minute session in the final round, and the weight sits on correctness rather than scale.
- **[Deel](deel.md)**: Design is folded into the technical interview alongside live coding, not run as a separate whiteboard round for every candidate.
- **[Goldman Sachs](goldman-sachs.md)**: One dedicated design round at the Superday can set the level of the offer, and the interviewer spends much of it pushing on failure cases: what happens when this feed stops, and who notices first.
- **[Gusto](gusto.md)**: Every reported question is a money-correctness question: a payroll calculation engine with tax rules that differ by state, a direct deposit flow where bank transfers come back days later, and an audit log that cannot be altered.
- **[Hudson River Trading](hudson-river-trading.md)**: There is no classic web-scale round here: the design questions are about one machine and the microseconds between a packet arriving and an output leaving.
- **[JPMorgan Chase](jpmorgan-chase.md)**: Losing a record or paying a customer twice counts as a failed round, so consistency and auditability outrank scale numbers in the grading.
- **[Jump Trading](jump-trading.md)**: Systems questions are spread across the loop instead of concentrated in one design round, and the emphasis stays low-level: memory, threads, sockets, and the cost of each.
- **[Klarna](klarna.md)**: The recurring test is a checkout that never double charges, at millions of purchases a day.
- **[Nubank](nubank.md)**: Immutable data and functional programming are public parts of the engineering culture, and they change what a good answer sounds like: append new facts, keep history, and derive read models from them.
- **[Plaid](plaid.md)**: Every question starts from one hard fact: thousands of bank APIs fail, return partial pages, or send the same record twice, and the system must stay correct anyway.
- **[Revolut](revolut.md)**: Design is graded in two places: an architecture review of your own take-home project, about 45 to 60 minutes, and for senior candidates a separate discussion about money systems.
- **[Toast](toast.md)**: Restaurant internet failing during dinner service is the constraint the whole round is built on, so terminals must keep taking orders offline and sync later without losing or doubling anything.
- **[Wise](wise.md)**: Correctness outranks raw scale, and the problem usually arrives as a business case, mostly for senior roles: a transfer flow, a ledger, or an integration with unreliable bank partners.

## Developer tools and enterprise software

- **[GitHub](github.md)**: Notably domain-specific: developer infrastructure rather than generic social prompts, with the platform's traffic shape (extreme read dominance punctuated by webhook, CI, and notification storms when a repo goes viral) driving the probes.
- **[Atlassian](atlassian.md)**: SaaS collaboration at multi-tenant scale: Jira and Confluence shape the prompts, so tenancy, permissions, search over user content, and integrations recur.
- **[ServiceNow](servicenow.md)**: Enterprise platform design almost nobody practices: thousands of customers configure everything, workflows run for months, and every design must survive customer customization and platform upgrades simultaneously.
- **[Salesforce](salesforce.md)**: Enterprise CRM scale: multi-tenant data platforms, configurable objects and workflows, and integration surfaces, with trust (the company's first value) shaping how data-handling questions are probed.
- **[Snowflake](snowflake.md)**: Distributed data systems with database-internals depth: storage formats, query execution, caching tiers, and multi-tenant resource isolation, in the architecture the company itself pioneered (storage separated from compute).
- **[Cloudflare](cloudflare.md)**: Internet-infrastructure scale: global edge networks, DDoS-magnitude traffic, and systems that must degrade gracefully when the internet itself misbehaves.
- **[Figma](figma.md)**: Classic infrastructure with a real-time multiplayer tilt: WebSocket scaling, presence, and state recovery on disconnect.
- **[Notion](notion.md)**: Grounded in its real architecture: everything is a block, users define their own schemas, and offline-first sync must never lose a user's writing.
- **[Canva](canva.md)**: Consumer-scale creative infrastructure: real-time collaboration, media processing pipelines, template search for hundreds of millions of users, and export rendering, with async-work-plus-waiting-human as the recurring shape.
- **[Vercel](vercel.md)**: The platform's own shapes: atomic immutable deployments, preview environments, build systems with layered caching, and edge networks, with developer experience graded as a design requirement (time-from-push-to-preview is the product).
- **[Wiz](wiz.md)**: Cloud-security platform design: agentless ingestion living inside cloud providers' API rate limits, the Security Graph (hundreds of millions of nodes per tenant), and toxic-combination detection as incremental multi-hop pattern queries.
- **[Workday](workday.md)**: Enterprise systems of record for HR and financials: the signature concept is effective-dated temporal data (every change has validity ranges; the org chart is a time-travel query), with paycheck-grade correctness and enterprise seasonality (payroll runs, open enrollment).
- **[Rippling](rippling.md)**: The compound-startup architecture: one employee graph powering payroll, IT, and finance, so prompts run on shared data models with many consumers, event cascades across products, and the offboarding guarantee (access revocation must complete, on time, provably).
- **[Airtable](airtable.md)**: Expect a requirement to be added partway through, because candidates report the mid-design change as a deliberate pattern, and adapting without restarting is part of the grade.
- **[Cisco](cisco.md)**: Scale is counted in devices rather than users, so a telemetry design serving fifty thousand routers is decided by write volume, not by read traffic.
- **[Confluent](confluent.md)**: Follow ups go past the component diagram and into guarantees: what a client sees when a node dies mid write, and whether ordering survives it.
- **[Docker](docker.md)**: Interviewers work on infrastructure daily, so vague storage math gets caught: being specific about layer sizes, bandwidth, and request rates matters more here than at most companies.
- **[Elastic](elastic.md)**: One concept sits under almost every question: the inverted index, and you should be able to draw it and explain it in plain words.
- **[GitLab](gitlab.md)**: Design often has no room of its own: it surfaces inside the technical and leadership rounds at senior and staff level, as an open discussion rather than one fixed prompt.
- **[Glean](glean.md)**: Enterprise search is the entire question space, and permission-aware retrieval is the signature problem.
- **[Grafana Labs](grafana-labs.md)**: Every box in your diagram needs a number attached to it: the company calls the exercise non abstract system design, and an estimate that is wrong but reasoned scores while a design with no arithmetic does not.
- **[HashiCorp](hashicorp.md)**: Every prompt maps onto one of the company's own tools: secrets storage (Vault), job placement (Nomad), shared state with locking (Terraform), and service discovery (Consul).
- **[Linear](linear.md)**: The client is offline-first, so the whole round turns on sync: a local copy that answers every read, and a server that decides one global order for incoming changes.
- **[Miro](miro.md)**: The round happens on a Miro board, so the diagram is graded as communication: labeled arrows and a readable layout count, because the product is the drawing tool.
- **[Okta](okta.md)**: Security awareness is graded as a fourth signal next to structure, numbers, and depth, so token expiry, key rotation, encryption, and least privilege have to come up without a prompt.
- **[Palo Alto Networks](palo-alto-networks.md)**: Networking is tested harder here than at most product companies, so TCP, TLS, and load balancing follow-ups arrive inside whatever design you are drawing.
- **[Redis](redis.md)**: A design that scales but never mentions memory or latency misses what the company actually sells, because the managed business rests on low latency, high availability, and predictable memory use.
- **[SAP](sap.md)**: Multi-tenancy is the lens on almost every follow-up question, and interviewers push on each shared cache and shared queue to find where one customer's data could leak into another's.
- **[SentinelOne](sentinelone.md)**: Concurrency sits beside distributed design here: candidates report multi-threaded queue questions, including lock-free versions, in the same conversation as event pipeline design.
- **[Slack](slack.md)**: Most of the score sits in the connection layer: a pool of gateway servers holding WebSockets, with pub/sub behind them so each gateway receives only the channels its connected users belong to.
- **[Snyk](snyk.md)**: Interviewers listen for one specific insight: a reverse index from package version to the projects that use it, instead of rescanning every project each time a new vulnerability record arrives.
- **[Supabase](supabase.md)**: Deep Postgres knowledge counts more here than at most companies, because each prompt is a platform piece bolted onto a real database: write ahead log streaming, row level security, and connection pooling.
- **[Temporal](temporal.md)**: Name the guarantees before drawing any component: at least once delivery, idempotency, leases, and event history are used precisely here, and interviewers notice when they are not.
- **[Twilio](twilio.md)**: Three reliability concepts carry most of the score, and you are expected to raise all three yourself: idempotency keys, retries with exponential backoff, and a dead-letter queue.
- **[Unity](unity.md)**: The round splits by track, so backend candidates design distributed services while engine candidates design memory, allocation, and object lifetimes against a frame budget.

## Defense and frontier tech

- **[Anduril](anduril.md)**: The cloud playbook partially inverts: the network is the least reliable component, so designs run edge-first with store-and-forward sync, legible degradation, and different delivery guarantees for telemetry versus commands.
- **[Palantir](palantir.md)**: The Decomposition round is the centerpiece: a vague real-world problem (a chess game, a parking garage, infection tracking) that you must turn into buildable structure: requirements interrogated, domain modeled, components carved with interfaces, and a build order defended, with mid-session constraint twists.
- **[SpaceX](spacex.md)**: Consequence-driven reliability across an unusual range: telemetry pipelines where bandwidth is set by physics, command paths where wrong is unrecoverable, and constellation-scale infrastructure (Starlink is plausibly the largest distributed system with physics in the loop ever built).
- **[Waymo](waymo.md)**: Two altitudes: on-vehicle low-level design (traffic-signal state machines, in-vehicle pub-sub, sensor scene graphs) where unknown-state honesty is graded, and fleet-scale infrastructure where the simulation platform (billions of tested miles) is the company's safety case in executable form.
- **[AMD](amd.md)**: Questions sit at the hardware-software boundary, and many rounds end with you implementing one component in real C or C++.
- **[Boston Dynamics](boston-dynamics.md)**: The clients in your diagram are robots, and a wrong answer can move a heavy machine near a person, so safety is treated as a requirement rather than a feature.
- **[Intel](intel.md)**: Which team you face decides the whole round, so ask the recruiter first: cloud and services teams ask standard scalable design, while embedded, driver, and platform teams go low level.
- **[Neuralink](neuralink.md)**: No interview questions are published, so the round is best predicted from the product: an implanted brain-computer interface and the systems around it.
- **[Qualcomm](qualcomm.md)**: Low-level design is the default here, not web-scale design, so a candidate who only practiced URL shorteners and news feeds will be surprised.
- **[Rivian](rivian.md)**: Every question connects back to the vehicle, so a design that works for a phone app but breaks for a truck offline in a remote area will be found out.
- **[Samsara](samsara.md)**: Sensor streams set the agenda: hundreds of thousands of devices reporting every few seconds, data arriving late and out of order, and gateways that drop off the network in a tunnel.
- **[Zoox](zoox.md)**: Designs are graded by what happens when a part fails with a rider inside a driverless vehicle, so the failure discussion decides the round.

---

Company loops change. If you interviewed recently and something here is out of date, [contributions](../CONTRIBUTING.md) are welcome.
