import config
from app import create_app

server = create_app(config)
server.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

if __name__ == "__main__":
    server.run(host=config.HOST, port=config.PORT)
