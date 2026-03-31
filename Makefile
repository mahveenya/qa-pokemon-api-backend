DOCKER_COMPOSE_FILE=./docker-compose.yml
IMAGE_TAG ?= main

up:
	IMAGE_TAG=$(IMAGE_TAG) docker compose -f $(DOCKER_COMPOSE_FILE) up -d --build
down:
	docker compose -f $(DOCKER_COMPOSE_FILE) down
stop:
	docker compose -f $(DOCKER_COMPOSE_FILE) stop
start:
	docker compose -f $(DOCKER_COMPOSE_FILE) start
rebuild: down up