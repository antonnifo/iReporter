"""Run docstring"""

import os
from app import create_app

APP = create_app(os.getenv("FLASK_CONF") or 'default')


