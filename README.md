# mlops-platform-aws #
AWS EKS MLOps platform demo 
(IaC, CI/CD, model artifacts, serving, monitoring)

## High-Level Architecture
## Core Components
### API Service
- FastAPI-based inference service
- Health and prediction endpoints
- Artifact-aware startup lifecycle

Path:
app/service/main.py

### Artifact Lifecycle (MLOps)
- Deterministic artifact generation
- Separate metrics and metadata
- Artifacts stored outside Git

Path:
platform/model_pipeline/

### CI Pipeline
- GitHub Actions based CI
- Automated unit tests on every push
- Early feedback on integration issues

path:
.github/workflows/ci.yml


### Infrastructure as Code
- Modular Terraform design
- Reusable modules for AWS resources
- Designed for EKS and cloud-native workloads

Path:
infra/terraform/




