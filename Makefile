.PHONY: storages
storages:
	sudo docker compose -f docker_compose/storages.yaml --env-file .env up -d

.PHONY: storages-down
storages-down:
	sudo docker compose -f docker_compose/storages.yaml down

.PHONY: storages-logs
storages-logs:
	sudo docker logs main_db -f

.PHONY: postgres
postgres:
	sudo docker exec -it main_db psql -U postgres

.PHONY: app
app:
	sudo docker compose -f docker_compose/app.yaml -f docker_compose/storages.yaml --env-file .env up --build -d

.PHONY: app-logs
app-logs:
	sudo docker logs main_app -f

.PHONY: superuser
superuser:
	sudo docker exec -it main_app python manage.py createsuperuser

.PHONY: migrations
migrations:
	sudo docker exec -it main_app python manage.py makemigrations

.PHONY: migrate
migrate:
	sudo docker exec -it main_app python manage.py migrate

.PHONY: collectstatic
collectstatic:
	sudo docker exec -it main_app python manage.py collectstatic
