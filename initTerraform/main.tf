provider "aws" {
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
  region     = "us-east-1"

}

# Cluster
resource "aws_ecs_cluster" "aws-ecs-cluster" {
  name = "DevApp-cluster"
  tags = {
    Name = "dev-ecs"
  }
}

resource "aws_cloudwatch_log_group" "log-group" {
  name = "/ecs/dev-logs"

  tags = {
    Application = "dev-app"
  }
}

# Task Definition

resource "aws_ecs_task_definition" "aws-ecs-task" {
  family = "dev-task"

  container_definitions = <<EOF
  [
  {
      "name": "dev-container",
      "image": "tsanderson77/tasks_app:v1",
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/dev-logs",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      },
      "portMappings": [
        {
          "containerPort": 3000
        }
      ]
    }
  ]
  EOF

  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  memory                   = "1024"
  cpu                      = "512"
  execution_role_arn       = "arn:aws:iam::266686430719:role/ecsTaskExecutionRole"
  task_role_arn            = "arn:aws:iam::266686430719:role/ecsTaskExecutionRole"

}

# ECS Service
resource "aws_ecs_service" "aws-ecs-service" {
  name                 = "dev-ecs-service"
  cluster              = aws_ecs_cluster.aws-ecs-cluster.id
  task_definition      = aws_ecs_task_definition.aws-ecs-task.arn
  launch_type          = "FARGATE"
  scheduling_strategy  = "REPLICA"
  desired_count        = 1
  force_new_deployment = true

  network_configuration {
    subnets = [
      aws_subnet.private_a.id,
      aws_subnet.private_b.id
    ]
    assign_public_ip = false
    security_groups  = [aws_security_group.ingress_app.id]
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.url-app.arn
    container_name   = "dev-container"
    container_port   = 3000
  }

}

