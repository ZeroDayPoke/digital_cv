#!/usr/bin/env python3
"""
__init__ file for app module

# Path: digital_cv/app/__init__.py
"""

from flask import Flask, request, g, redirect, url_for, flash
from flask_admin import Admin
from flask_babel import Babel
from flask_login import LoginManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import redis
from config import config
from .models import db, User, Blog, Tutorial, Skill, Project
from .routes import (main_routes, auth_routes, project_routes,
                     skill_routes, admin_routes, blog_routes, tutorial_routes)
from admin import ProjectAdminView, SkillAdminView, BlogAdminView, TutorialAdminView
import logging

def create_app(config_name='default') -> Flask:
    """
    Create and configure the Flask application.

    Args:
        config_name (str): Configuration type ('development', 'production', etc.)

    Returns:
        Flask: Configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize database
    db.init_app(app)

    # Initialize localization
    babel = Babel()
    babel.init_app(app, locale_selector=lambda: get_locale(app))

    # Initialize admin interface
    admin_name = app.config.get('ADMIN_NAME', 'AdInt')
    admin = Admin(app, name=admin_name, template_mode='bootstrap4')
    admin.add_view(ProjectAdminView(Project, db.session))
    admin.add_view(SkillAdminView(Skill, db.session))
    admin.add_view(BlogAdminView(Blog, db.session))
    admin.add_view(TutorialAdminView(Tutorial, db.session))

    # Initialize login manager and user loader
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id: str) -> User:
        """
        Load a user from the database using the user ID.

        Args:
            user_id (str): The ID of the user to load.

        Returns:
            User: The loaded user object, or None if the user doesn't exist.
        """
        return User.query.get(user_id)

    # Register blueprints
    app.register_blueprint(main_routes)
    app.register_blueprint(auth_routes)
    app.register_blueprint(project_routes)
    app.register_blueprint(skill_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(blog_routes)
    app.register_blueprint(tutorial_routes)

    # Register context processors
    @app.context_processor
    def inject_blogs() -> dict:
        """
        Inject all blog entries into the template context.

        Returns:
            dict: A dictionary containing all blog entries.
        """
        blogs = Blog.query.all()
        return dict(blogs=blogs)

    @app.context_processor
    def inject_tutorials() -> dict:
        """
        Inject all tutorial entries into the template context.

        Returns:
            dict: A dictionary containing all tutorial entries.
        """
        tutorials = Tutorial.query.all()
        return dict(tutorials=tutorials)
    
    @app.context_processor
    def inject_projects() -> dict:
        """
        Inject all project entries into the template context.

        Returns:
            dict: A dictionary containing all project entries.
        """
        projects = Project.query.all()
        return dict(projects=projects)
    
    # Initialize Redis
    redis_store = redis.StrictRedis(host='localhost', port=6379, db=0)

    # Initialize Flask-Limiter
    limiter = Limiter(
        app=app,
        key_func=get_remote_address,
        storage_uri="redis://localhost:6379",
        default_limits=["60 per hour"]
    )

    logging.info(f"App created with config: {config_name}")

    return app

def get_locale(app: Flask) -> str:
    """
    Determine the best locale to use for translations.

    Args:
        app (Flask): The current Flask application instance.

    Returns:
        str: Locale code.
    """
    requested_locale = request.args.get('locale')
    if requested_locale in app.config['LANGUAGES']:
        return requested_locale

    user = g.get('user', None)
    if user:
        user_locale = user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    if best_match:
        return best_match

    return app.config['BABEL_DEFAULT_LOCALE']
