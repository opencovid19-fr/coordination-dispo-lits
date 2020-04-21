build: .env
	docker-compose build

run:
	docker-compose up -d

test: build
	docker-compose -f docker-compose.yml -f docker-compose-test.yml run --rm server

initdb:
	docker-compose run --rm server python manage.py db init

migrate:
	docker-compose run --rm server python manage.py db migrate

db_upgrade:
	docker-compose run --rm server python manage.py db upgrade

.env:
	cp .env-template $@
