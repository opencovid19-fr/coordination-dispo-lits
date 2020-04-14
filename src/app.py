from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow

from model.abc import db, ma


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    db.app = app
    db.init_app(app)
    ma.init_app(app)
    JWTManager(app)

    CORS(
        app,
        resources={r"/*": {"origins": "*"}},
        headers=['Content-Type', 'X-Requested-With', 'Authorization']
    )
    from route.api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    from route.common import common_blueprint
    app.register_blueprint(common_blueprint, url_prefix="/")
    return app