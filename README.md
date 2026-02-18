# Cloud-Simulated Banking System

## Month 3 Project — Cloud Architecture with AWS Open-Source Simulation

---

## Project Overview
This project simulates a real-world cloud banking architecture using 100% open-source tools that replicate core cloud service concepts. It demonstrates practical experience with cloud infrastructure, automation, API security, monitoring, and CI/CD pipelines — all running locally with zero cloud cost.

This system showcases implementation of:

- Infrastructure as Code (IaC)
- CI/CD automation
- Secure API Gateway architecture
- Monitoring & observability
- Containerized services
- Secure service communication

---

## Project Goal
Design and deploy a cloud-simulated banking platform that demonstrates real cloud architecture principles using local open-source tools that emulate managed cloud services.

---

## Architecture Overview

### System Flow
Client → API Gateway → Backend API → Database + Storage → Monitoring Stack


### Core Principles
- Private service networking
- Secure API access
- Automated provisioning
- Metrics-based monitoring
- Containerized microservices

---

## Development Timeline

---

### Week 1 — Cloud Foundations & Setup
**Focus:** Architecture concepts and environment setup

**Tasks**
- Reviewed cloud architecture fundamentals
- Installed services:
  - FastAPI (backend API)
  - MongoDB (database)
  - MinIO (object storage)
- Created cloud mapping table
- Designed architecture diagram

**Deliverables**
- Setup documentation
- Initial architecture design

---

### Week 2 — Infrastructure as Code & CI/CD
**Focus:** Automated provisioning and deployment

#### Infrastructure as Code (Terraform)

**Provisioned Resources**
- Docker network → simulates VPC
- Docker volumes → simulates persistent storage

**Run Terraform**
```bash
cd terraform
terraform init
terraform plan
terraform apply
Benefits

Repeatable environments

Automated infrastructure

Version-controlled provisioning

CI/CD Pipeline (GitHub Actions)
Pipeline Steps

Checkout repository

Build Docker image

Run container

Wait for service readiness

Test endpoint

Log failures if startup fails

Trigger

Push → main branch
Reliability Feature
Retry loop ensures API is running before testing.

Week 3 — Security & API Management
Focus: Secure routing and API gateway simulation

API Gateway Layer — Kong
Purpose

Centralized routing

Authentication enforcement

Service isolation

Request Flow

Client → Kong Gateway → FastAPI → Database/Storage
Backend service is private and only accessible through gateway.

Authentication Simulation
Implemented:

API key authentication plugin

Consumer identity system

Access control enforcement

Example Secure Request

curl -X POST http://localhost:8000/api/accounts \
-H "Content-Type: application/json" \
-H "apikey: YOUR_API_KEY" \
-d '{"name":"John","balance":1000}'
Security Advantages

Backend never publicly exposed

Access control enforced

Identity-based API usage

Week 4 — Monitoring & Observability
Focus: Performance tracking and metrics

Monitoring Stack
FastAPI → Prometheus → Grafana
Metrics Collected
Request rate

Latency

Error rates

Active connections

Endpoint usage

Prometheus Config

global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "cloud-banking-api"
    static_configs:
      - targets: ["fastapi:8000"]
    metrics_path: /metrics
Observations
Identified high-traffic endpoints

Verified stability

Minimal server errors

Normal database/storage load

Security Features
API key authentication

Private container networking

Environment-based configs

Optional service initialization

Restricted monitoring access

Technology Stack
Layer	Tool	Purpose
Backend	FastAPI	REST API
Database	MongoDB	Data storage
Object Storage	MinIO	File storage
Gateway	Kong	Routing + Security
IaC	Terraform	Infrastructure provisioning
CI/CD	GitHub Actions	Automation pipeline
Monitoring	Prometheus	Metrics collection
Visualization	Grafana	Dashboards
Runtime	Docker	Container platform
Project Structure
cloud-banking-system/
│
├── terraform/
│   └── main.tf
│
├── fastapi/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── .github/workflows/
│   └── ci-cd.yml
│
├── docker-compose.yml
└── kong_config/
Running Locally
Start services

docker-compose up -d
Verify containers

docker ps
Test API

curl http://localhost:8000/api/
Observability Deliverables
Live dashboards

Real-time metrics

Performance monitoring

Stability validation

Testing Strategy
System validation includes:

API readiness checks

Container startup logs

Endpoint accessibility

Secure routing verification

Metrics exposure validation

Challenges & Solutions
Challenge	Solution
API container not ready	Added retry loop
Missing environment variables	Conditional initialization
Cross-OS command differences	Used compatible commands
Environment consistency	Terraform provisioning
Learning Outcomes
This project demonstrates practical ability to:

Design scalable cloud architectures

Implement Infrastructure as Code

Build automated pipelines

Secure APIs using gateway layers

Monitor distributed systems

Apply real DevOps practices

Final Result
A fully functional cloud-simulated banking system showcasing modern cloud engineering principles using only open-source technologies.

Team
Group 40

License
Educational project — free for learning and demonstration use.

Future Improvements
Role-based authentication

Load balancing simulation

Distributed logging

Service mesh integration

Chaos testing

Autoscaling simulation

