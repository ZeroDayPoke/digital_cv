#!/usr/bin/env python3
"""
__init__ file for app module

# Path: digital_cv/app/__init__.py
"""

from flask import Flask
from config import config
from flask_login import LoginManager
from app.models import db, User
from app.routes.main import main_routes as main_blueprint

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.url_map.strict_slashes = False
    login_manager = LoginManager()
    login_manager.init_app(app)
    db.init_app(app)
    app.register_blueprint(main_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        # Retrieve the user object based on the user_id
        user = User.query.get(user_id)
        return user

    return app
