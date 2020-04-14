# coordination-dispo-lits
Dépôt support pour la coordination des initiatives concernant la disponibilité des lits


## Project's arboscence

Application source in python is included in the src directory and divided in package as followed:
   - client groups all buiness function to interact with external sources
   - commands groups all custom shell commands to manage the application and are configure in the module `manage.py`
   - fixtures groups json file used by tests or the command load fixtures
   - model groups sqlalchemy model.
   - repository groups dao functions with simple and comples sqlalchemy query
   - resource groups implementation of the route with flas-restful
   - route delares routes with blueprint using resources modeules
   - serializer declares objects for flask-restful-swagger
   - validator declares mashmallow objects to serialize, response and validate request parameters

All config params are defined in the config module.

Dev server is launch with module `server`

Shell commands are launch with module `manage`


## Installation

Pre-requisite: copy .env-template to .env

```
docker-compose run --rm server pip install -r requirements.txt --user --upgrade
docker-compose up -d server
```

## Accessing containers

Require Docker >= 1.3

```shell
# use 'docker ps' to see the list of your containers
docker exec -it <project_name>_db_1 psql -Upostgres
docker exec -it <project_name>_db_server_1 bash
```

## Migration process

```shell
# Prior to the first migration
docker-compose run --rm server python manage.py db init

# Create a new version of the database
docker-compose run --rm server python manage.py db migrate
# check file + remove comment + improve file if needed
sudo vim migration/versions/<migration_id>.py

# Upgrade your database to the last version
docker-compose run --rm server python manage.py db upgrade
```

## Run tests

```shell
docker-compose run --rm testserver python -m unittest
```

## Commands

```shell
# Screenshot of python vendors
docker-compose run --rm server pip freeze > requirements.txt

# Run a command in the server container:
docker-compose run --rm server <command>
```

