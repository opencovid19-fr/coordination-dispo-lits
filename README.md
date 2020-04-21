# Beds Availability Data Hub


## Project files structure

Application source code (python) in the `app/` directory is divided
in packages as follows:

   - `fixtures`:   json file used by tests or the command load fixtures
   - `commands`:   custom shell commands to manage the application
                   configured in module `manage.py`
   - `covidbed`:   buiness packages for api


Package `covidbed` is structured as follows:

   - `client`:     buiness function to interact with external sources
   - `model`:      sqlalchemy model
   - `repository`: dao functions with simple and comples sqlalchemy query
   - `resource`:   implementation of the route with flas-restful
   - `route`:      routes with blueprint using resources modeules
   - `serializer`: objects for flask-restful-swagger
   - `validator`:  mashmallow objects to serialize response
                   and validate request parameters


All config params are defined in the config module.

Dev server is launched with module `server`

Shell commands are launched with module `manage`


## Running a production instance

```
make build
make run
```

Note: overall configuration file `.env` is initialized from `.env-template`
      and should be fine for most use-cases; update to your liking as needed.

The various api routes should be displayed on `localhost:$API_PORT` where `API_PORT` is set in the `.env` file.

## Accessing containers

Require Docker >= 1.3

```shell
# use 'docker ps' to see the list of your containers
docker-compose exec db psql -Upostgres
docker-compose exec server bash
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

