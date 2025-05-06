DC = docker compose
.PHONY: up, down, bash, check,
up:
	${DC} up
down:
	${DC} down


bash:
	docker compose exec -it backend_api bash


check:
	isort .
	black .
	flake8 .
