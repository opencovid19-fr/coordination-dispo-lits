build: .env
	docker-compose build

run:
	docker-compose up -d

test: build test_db
	docker-compose -f docker-compose.yml -f docker-compose-test.yml run --rm server

initdb:
	docker-compose run --rm server python manage.py db init

migrate:
	docker-compose run --rm server python manage.py db migrate

db_upgrade:
	docker-compose run --rm server python manage.py db upgrade

test_db: compose.files = -f docker-compose.yml -f docker-compose-test.yml
test_db:
	docker-compose ${compose.files} up -d testdb
	docker-compose ${compose.files} exec -T testdb bash -c \
		"while ! pg_isready ; do sleep .1; done"

clean: containers = hub_testdb_1 hub_db_1
clean:
	docker stop ${containers}
	docker rm   ${containers}
	docker-compose down

.env:
	cp .env-template $@
