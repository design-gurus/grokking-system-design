# Company-specific system design interviews

The same interview loop does not exist twice. Citadel budgets microseconds, ServiceNow probes upgrade safety, Anthropic hands you a problem its own teams are still solving, and Bloomberg asks "why this and not the alternative" until it finds bottom. These notes summarize how 58 companies actually run their system design rounds, so you can aim the [patterns](../patterns/) and [questions](../questions/) in this repo at the loop you are facing.

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

## Big tech

- **[Apple](apple.md)**: Loops are team-designed rather than centrally standardized, so design rounds vary widely: consumer-scale services, on-device and privacy-conscious architectures, and media delivery all appear.
- **[Microsoft](microsoft.md)**: Design rounds are structured and rubric-driven like the rest of the loop: enterprise-scale services, collaboration and productivity systems, and Azure-flavored infrastructure, with clear communication scored alongside architecture.
- **[Netflix](netflix.md)**: Design conversations lean on streaming-scale realities: CDN strategy, personalization, and resilience engineering (this is the company that invented chaos engineering).
- **[Nvidia](nvidia.md)**: Design rounds are scoped to the team: data pipelines, serving systems, driver-adjacent components, or distributed training infrastructure.
- **[Tesla](tesla.md)**: Design questions carry first-principles grilling and physical-world texture: vehicle telemetry, fleet OTA updates, and real-time data pipelines, with interviewers pushing one level deeper than your resume claims.
- **[Adobe](adobe.md)**: Design runs at three altitudes: product architecture at creative-cloud scale, object-oriented low-level design, and database judgment, increasingly with a generative-AI accent (Firefly-style features with GPU economics inside consumer products).
- **[LinkedIn](linkedin.md)**: Product-centric prompts (feed, notifications, People You May Know) that are secretly graph problems: the key instinct is designing for extreme degree skew (most members have hundreds of connections; some have millions of followers).
- **[Oracle](oracle.md)**: Loops vary by organization: OCI runs a modern distributed-systems interview (multi-tenant cloud services, replication, consistency), while application orgs lean toward practical enterprise design.

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

## Defense and frontier tech

- **[Anduril](anduril.md)**: The cloud playbook partially inverts: the network is the least reliable component, so designs run edge-first with store-and-forward sync, legible degradation, and different delivery guarantees for telemetry versus commands.
- **[Palantir](palantir.md)**: The Decomposition round is the centerpiece: a vague real-world problem (a chess game, a parking garage, infection tracking) that you must turn into buildable structure: requirements interrogated, domain modeled, components carved with interfaces, and a build order defended, with mid-session constraint twists.
- **[SpaceX](spacex.md)**: Consequence-driven reliability across an unusual range: telemetry pipelines where bandwidth is set by physics, command paths where wrong is unrecoverable, and constellation-scale infrastructure (Starlink is plausibly the largest distributed system with physics in the loop ever built).
- **[Waymo](waymo.md)**: Two altitudes: on-vehicle low-level design (traffic-signal state machines, in-vehicle pub-sub, sensor scene graphs) where unknown-state honesty is graded, and fleet-scale infrastructure where the simulation platform (billions of tested miles) is the company's safety case in executable form.

---

Company loops change. If you interviewed recently and something here is out of date, [contributions](../CONTRIBUTING.md) are welcome.
