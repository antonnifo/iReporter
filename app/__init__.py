from flask import Flask,Blueprint
from app.api.v1.routes import version1 as v1

from app.instance.config import APP_CONFIG


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name])
    

    app.register_blueprint(v1)
   
    return app
    