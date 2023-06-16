#!/usr/bin/env python3
"""
__init__ file for app module

# Path: digital_cv/app/__init__.py
"""

from flask import Flask
from config import config
from flask_login import LoginManager
from app.models import db, User, Blog
from .routes import main_routes, auth_routes, project_routes, skill_routes, admin_routes, blog_routes

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_blueprint(main_routes)
    app.register_blueprint(auth_routes)
    app.register_blueprint(project_routes)
    app.register_blueprint(skill_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(blog_routes)
    app.url_map.strict_slashes = False
    login_manager = LoginManager()
    login_manager.init_app(app)
    db.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # Retrieve the user object based on the user_id
        user = User.query.get(user_id)
        return user

    @app.context_processor
    def inject_blogs():
        blogs = Blog.query.all()
        return dict(blogs=blogs)

    return app
