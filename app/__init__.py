from flask import Flask
from flask_cors import CORS
from config import config
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    cors_config = {"origins": []}
    CORS(app, resources={"/*": cors_config}, supports_credentials=True)

    db.init_app(app)

    from app.api import api
    from app.api.api_v1 import api_v1

    api.register_blueprint(api_v1)
    app.register_blueprint(api)

    return app
