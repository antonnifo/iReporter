from flask import Blueprint, Flask

from app.api.v1.routes import VERSION_UNO as v1
from app.api.v2.routes import VERSION_TWO as v2
from app.instance.config import APP_CONFIG
from app.db_con import create_tables, test_user_admin, test_intervention, test_redflag, destroy_tables


def create_app(config_name):
    '''The create_app function wraps the creation of a new Flask object,
    and returns it after it's loaded up with configuration settings using
    app.config '''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name])
    app.url_map.strict_slashes = False
    destroy_tables()
    create_tables()
    test_user_admin()
    test_intervention()
    test_redflag()

    app.register_blueprint(v1)
    app.register_blueprint(v2)
    return app
