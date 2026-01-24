module "ecr" {
  source       = "../../modules/ecr"
  project_name = var.project_name
  environment  = var.environment
}

module "artifacts_bucket" {
  source       = "../../modules/s3_artifacts"
  project_name = var.project_name
  environment  = var.environment
}

module "state_backend" {
  source       = "../../modules/state_backend"
  project_name = var.project_name
  environment  = var.environment
}
