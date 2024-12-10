# Data Pipeline Automation with Kubernetes and ELK

This repository automates the deployment of a scalable data pipeline on Kubernetes. It integrates Kafka, Spark, HDFS, and Atlas for data lineage tracking and error-checking, alongside ELK (Elasticsearch, Logstash, Kibana) for advanced monitoring and logging.

## Features
- **Data Processing**: Stream and batch processing with Apache Spark.
- **Data Lineage**: Apache Atlas integration.
- **Monitoring**: ELK Stack with Filebeat for log aggregation.
- **Scalability**: Kubernetes for container orchestration.
- **Automation**: Spark jobs with Kubernetes CronJobs.

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/data-pipeline-k8s.git
   cd data-pipeline-k8s
   ```

2. Deploy infrastructure components:
   ```bash
   kubectl apply -f manifests/
   ```

3. Monitor logs and metrics in Kibana.

## Repository Structure
```
data-pipeline-k8s/
├── README.md
├── helm-charts/
├── manifests/
├── spark-scripts/
├── config/
├── LICENSE
└── .gitignore
```
