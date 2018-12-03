from flask import Flask,Blueprint
from app.api.v1 import version1 as v1
# from .api.v2 import version2 as v2
from app.instance.config import APP_CONFIG
# from db_con import create_tables

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name])
    # create_tables()

    app.register_blueprint(v1)
    # app.register_blueprint(v2)
    
    return app
    