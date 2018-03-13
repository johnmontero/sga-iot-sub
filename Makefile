.DEFAULT_GOAL := help


PROYECT_NAME = sga_iot_sub


start: ## Up the docker containers, use me with: make start
	docker-compose up -d

stop: ## Stops the docker containers, use me with: make stop
	docker-compose stop

status: ## Show containers status, use me with: make status
	docker-compose ps

down: ## Stops and removes the docker containers, use me with: make down
	docker-compose down

delete: ## Delete the docker containers, use me with: make delete
	docker-compose rm -fv

build: ## Build the docker containers, use me with: make build
	docker-compose build

rebuild: ## Rebuild the docker containers, use me with: make rebuild
	make stop
	make delete
	make build
	make start

logs: ## Logss the docker containers, use me with: make logs
	docker-compose logs -f

ssh: ## SSH connect to container, se me with: make ssh target=api
		docker-compose -p $(PROYECT_NAME) run --rm  sh -c "bash"

###### Help
help:
	@echo  'Development commands for project ${PROYECT_NAME}'
	@echo
	@echo 'Usage: make COMMAND'
	@echo
	@echo 'Targets:'
	@echo
	@echo '  app            Application sga-oti-sub'
	@echo
	@echo 'Commands:'
	@echo
	@grep -E '^[a-zA-Z_-]+.+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'
	@echo
