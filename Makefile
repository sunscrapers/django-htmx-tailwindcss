update-deps:
	pip install -U pip && pip install pip-tools

	pip-compile requirements/base.in
	pip-compile requirements/dev.in

REQUIREMENTS_FILE = dev.txt
build:
	docker compose build --build-arg="REQUIREMENTS_FILE=$(REQUIREMENTS_FILE)"

up:
	make build
	docker compose up

down:
	docker compose down

attach:
	docker attach myproject

bash:
	docker exec -it myproject bash

shell:
	docker exec -it myproject python manage.py shell_plus --ipython

migrate:
	docker exec -it myproject python manage.py migrate

migrations:
	docker exec -it myproject python manage.py makemigrations

collectstatic:
	docker exec -it myproject python manage.py collectstatic

run-build:
	docker build . -f docker/Dockerfile -t myproject:latest --build-arg="REQUIREMENTS_FILE=$(REQUIREMENTS_FILE)"

run:
	docker run --name myproject -p 8000:8000 --rm --env-file .env -it myproject:latest

tests:
	docker exec -it myproject pytest -s --verbose

circleci-up:
	make build
	docker compose -f docker-compose-circleci.yml up -d

circleci-tests:
	docker exec -it myproject pytest -v --cov=./ --cov-config=tests/.coveragerc --junitxml=/src/test-results/junit.xml
