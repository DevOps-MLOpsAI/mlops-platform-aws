# Terraform - AWS Platform Foundation

## What this provisions (Phase 1)
- ECR repository for container images
- S3 bucket for versioned artifacts

## Next phases
- Remote state backend (S3 + DynamoDB)
- VPC + EKS cluster + node groups
- IRSA roles and policies
- ALB ingress controller prerequisites

## Run (dev)
cd infra/terraform/envs/dev
terraform init
terraform plan
terraform apply
