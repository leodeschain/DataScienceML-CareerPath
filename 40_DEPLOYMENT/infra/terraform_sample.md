# Exemplo de Código Terraform (Conceitual)

Este não é um código funcional, mas um exemplo de como a infraestrutura para o deploy da API poderia ser definida usando Terraform.

## Provedor e Recurso

```terraform
provider "aws" {
  region = "us-east-1"
}

resource "aws_ecr_repository" "app_ecr_repo" {
  name = "iris-classifier-api"
}

resource "aws_ecs_cluster" "main_cluster" {
  name = "main-cluster"
}

resource "aws_ecs_task_definition" "api_task" {
  family                   = "api-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  
  container_definitions = jsonencode([
    {
      name      = "iris-api-container"
      image     = "${aws_ecr_repository.app_ecr_repo.repository_url}:latest"
      portMappings = [
        {
          containerPort = 80
          hostPort      = 80
        }
      ]
    }
  ])
}

resource "aws_ecs_service" "api_service" {
  name            = "api-service"
  cluster         = aws_ecs_cluster.main_cluster.id
  task_definition = aws_ecs_task_definition.api_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets         = ["subnet-xxxxxx"]
    security_groups = ["sg-xxxxxx"]
    assign_public_ip = true
  }
}
```
