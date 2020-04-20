import os, logging

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

DEBUG = os.getenv("ENVIRONEMENT") == "DEV"
HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', '5000'))
SQLALCHEMY_RECORD_QUERIES = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss')
BASE_SERVER_PATH = os.environ.get("BASE_SERVER_PATH", 'http://127.0.0.1:5000/')

FIXTURES_LIST = os.environ.get("FIXTURES_LIST", 'users.json')

POSTGRES = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('POSTGRES_USER'),
    'db': os.getenv('POSTGRES_DB'),
    'pw': os.getenv('POSTGRES_PASSWORD'),
    'port': os.getenv('POSTGRES_PORT', 5432),
}
SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

logging.basicConfig(
    filename=os.getenv('SERVICE_LOG', 'server.log'),
    level=logging.DEBUG,
    format='%(levelname)s: %(asctime)s pid:%(process)s module:%(module)s %(message)s',
    datefmt='%d/%m/%y %H:%M:%S',
)


