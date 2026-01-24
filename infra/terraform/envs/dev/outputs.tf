output "ecr_repository_url" {
  value = module.ecr.repository_url
}

output "artifacts_bucket_name" {
  value = module.artifacts_bucket.bucket_name
}

output "tf_state_bucket" {
  value = module.state_backend.state_bucket
}

output "tf_lock_table" {
  value = module.state_backend.lock_table
}
