build: .env
	docker-compose build

run:
	docker-compose up -d

test: build test_db
	docker-compose ${compose.test} run --rm server

prod:
	docker-compose ${compose.prod} up -d

initdb:
	docker-compose run --rm server python manage.py db init

migrate:
	docker-compose run --rm server python manage.py db migrate

db_upgrade:
	docker-compose run --rm server python manage.py db upgrade

test_db:
	docker-compose ${compose.test} up -d testdb
	docker-compose ${compose.test} exec -T testdb bash -c \
		"while ! pg_isready ; do sleep .1; done"

clean: containers = hub_testdb_1 hub_db_1
clean:
	docker stop ${containers}
	docker rm   ${containers}
	docker-compose down

compose.main = -f docker-compose.yml
compose.test = ${compose.main} -f docker-compose-test.yml
compose.prod = ${compose.main} -f docker-compose-prod.yml

.env:
	cp .env-template $@
