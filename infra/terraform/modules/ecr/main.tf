variable "project_name" { type = string }
variable "environment"  { type = string }

resource "aws_ecr_repository" "this" {
  name                 = "${var.project_name}-${var.environment}"
  image_tag_mutability = "IMMUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}

output "repository_url" {
  value = aws_ecr_repository.this.repository_url
}
