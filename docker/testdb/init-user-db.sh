# Everything commented as we are not needing any startup configuration right now
# #!/bin/bash
# set -e
#
# psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
#     CREATE USER docker with password 'docker';
#     CREATE DATABASE docker;
#     GRANT ALL PRIVILEGES ON DATABASE docker TO docker;
# EOSQL
