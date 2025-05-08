ifneq (,$(wildcard ./.env))
include .env
export
ENV_FILE_PARAM = --env-file .env

endif

DOCKER_COMPOSE := docker-compose

build:
	$(DOCKER_COMPOSE) up --build -d --remove-orphans

up:
	$(DOCKER_COMPOSE) up -d

down:
	$(DOCKER_COMPOSE) down

show-logs:
	$(DOCKER_COMPOSE) logs

migrate:
	$(DOCKER_COMPOSE) exec api python3 manage.py migrate

makemigrations:
	$(DOCKER_COMPOSE) exec api python3 manage.py makemigrations

superuser:
	$(DOCKER_COMPOSE) exec api python3 manage.py createsuperuser

collectstatic:
	$(DOCKER_COMPOSE) exec api python3 manage.py collectstatic --no-input --clear

down-v:
	$(DOCKER_COMPOSE) down -v

volume:
	docker volume inspect realstate_postgres_data

estate-db:
	$(DOCKER_COMPOSE) exec postgres-db psql --username=postgres --dbname=realstate

test:
	$(DOCKER_COMPOSE) exec api pytest -p no:warnings --cov=.

test-html:
	$(DOCKER_COMPOSE) exec api pytest -p no:warnings --cov=. --cov-report html

flake8:
	$(DOCKER_COMPOSE) exec api flake8 .

black-check:
	$(DOCKER_COMPOSE) exec api black --check --exclude=migrations .

black-diff:
	$(DOCKER_COMPOSE) exec api black --diff --exclude=migrations .

black:
	$(DOCKER_COMPOSE) exec api black --exclude=migrations .

isort-check:
	$(DOCKER_COMPOSE) exec api isort . --check-only --skip env --skip migrations

isort-diff:
	$(DOCKER_COMPOSE) exec api isort . --diff --skip env --skip migrations

isort:
	$(DOCKER_COMPOSE) exec api isort . --skip env --skip migrations

