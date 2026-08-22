# AWS vs GCP vs Azure: the service translation table

System design interviews are cloud-neutral. Design in components (an object store, a queue, a managed relational database), then name a vendor service only to be concrete. This table translates between the three big clouds, so you can follow any interviewer's dialect and answer in it.

## Compute

| Component | AWS | GCP | Azure |
|-----------|-----|-----|-------|
| Virtual machines | EC2 | Compute Engine | Virtual Machines |
| Serverless functions | Lambda | Cloud Functions | Azure Functions |
| Managed Kubernetes | EKS | GKE | AKS |
| Serverless containers | Fargate (on ECS) | Cloud Run | Container Apps |

## Storage

| Component | AWS | GCP | Azure |
|-----------|-----|-----|-------|
| Object storage | S3 | Cloud Storage | Blob Storage |
| Block storage (VM disks) | EBS | Persistent Disk | Managed Disks |
| Shared file system | EFS | Filestore | Azure Files |

## Databases

| Component | AWS | GCP | Azure |
|-----------|-----|-----|-------|
| Managed relational | RDS | Cloud SQL | Azure SQL Database |
| Cloud-native relational | Aurora | AlloyDB | SQL Database Hyperscale |
| Key-value / document | DynamoDB | Firestore | Cosmos DB |
| Wide-column | Keyspaces | Bigtable | Cosmos DB (Cassandra API) |
| In-memory cache | ElastiCache | Memorystore | Azure Cache for Redis |
| Data warehouse | Redshift | BigQuery | Synapse Analytics |

## Messaging and streaming

| Component | AWS | GCP | Azure |
|-----------|-----|-----|-------|
| Queue (work distribution) | SQS | Cloud Tasks | Service Bus |
| Pub/sub notifications | SNS | Pub/Sub | Event Grid |
| Event streaming | Kinesis, or MSK for managed Kafka | Pub/Sub | Event Hubs |

On GCP, Pub/Sub covers both the notification and the streaming row; it is one global service rather than two products. The full decision is in [Kafka vs Kinesis vs Pub/Sub](kafka-vs-kinesis-vs-pubsub.md).

## Networking and delivery

| Component | AWS | GCP | Azure |
|-----------|-----|-----|-------|
| CDN | CloudFront | Cloud CDN | Front Door |
| DNS | Route 53 | Cloud DNS | Azure DNS |
| Load balancer | ELB (ALB and NLB) | Cloud Load Balancing | Load Balancer, Application Gateway |
| API gateway | API Gateway | API Gateway, Apigee | API Management |

## Operations, security, and ML

| Component | AWS | GCP | Azure |
|-----------|-----|-----|-------|
| Monitoring and logs | CloudWatch | Cloud Monitoring | Azure Monitor |
| Identity and access | IAM | Cloud IAM | Entra ID with RBAC |
| Secrets | Secrets Manager | Secret Manager | Key Vault |
| ML platform | SageMaker | Vertex AI | Azure Machine Learning |

## The ones with no true twin

Most services translate cleanly. A few do not, and knowing them is senior-level signal:

- Spanner (GCP): a relational database that stays strongly consistent across regions, built on synchronized clocks ([deep dive](../deep-dives/spanner-global-sql.md)). The other clouds approximate it with read replicas and application logic.
- BigQuery (GCP): a data warehouse with no cluster to size; you pay per query. Redshift and Synapse are cluster-shaped.
- DynamoDB (AWS): single-digit-millisecond key-value at any scale, billed per request ([deep dive](../deep-dives/dynamodb-managed-nosql.md)). Firestore and Cosmos DB are cousins, not clones.
- Cosmos DB (Azure): one service that speaks several database APIs (document, Cassandra, Gremlin) with turnkey multi-region writes.

## How to talk about it in an interview

Do not brand-drop ("I will use S3, Lambda, and DynamoDB") before the design exists. Say "uploads land in an object store, a queue feeds the transcoding workers, and metadata lives in a managed relational database", then translate into whatever cloud the interviewer speaks. Component-first answers show the design transfers; brand-first answers suggest you know one vendor's catalog rather than the underlying system.

## Go deeper

- The components themselves: [core components](core-components.md) and the [patterns](../patterns/)
- Landmark systems behind these services: [Spanner](../deep-dives/spanner-global-sql.md), [DynamoDB](../deep-dives/dynamodb-managed-nosql.md), [Bigtable](../deep-dives/bigtable-wide-column-store.md)
- Full course: [Grokking the System Design Interview](https://www.designgurus.io/course/grokking-the-system-design-interview)
