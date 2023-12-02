#!/usr/bin/env python3
"""
__init__ file for app module

# Path: digital_cv/app/__init__.py
"""

import os
from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.menu import MenuLink
from flask_babel import Babel
from flask_login import LoginManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .utils import get_locale
from config import config
from .models import db, User, Blog, Tutorial, Skill, Project, Education, Message, Experience, ProjectCategory, SkillCategory, Pet, Award, Service
from .routes import (main_routes, auth_routes, project_routes,
                     skill_routes, admin_routes, blog_routes, tutorial_routes, services_routes)
from admin import ProjectAdminView, SkillAdminView, BlogAdminView, TutorialAdminView, EducationAdminView, UserAdminView, MessageAdminView, ExperienceAdminView, ProjectCategoryAdminView, PetAdminView, AwardAdminView
import logging
from flask_wtf import CSRFProtect
from flask_ckeditor import CKEditor

# Initialize database


def init_db(app):
    db.init_app(app)


# Initialize admin interface
def init_admin(app):
    admin_name = app.config.get('ADMIN_NAME', 'Digital CV Admin')
    admin = Admin(app, name=admin_name, template_mode='bootstrap4')
    admin.add_view(ProjectAdminView(Project, db.session))
    admin.add_view(SkillAdminView(Skill, db.session))
    admin.add_view(BlogAdminView(Blog, db.session))
    admin.add_view(TutorialAdminView(Tutorial, db.session))
    admin.add_view(EducationAdminView(Education, db.session))
    admin.add_view(UserAdminView(User, db.session))
    admin.add_view(MessageAdminView(Message, db.session))
    admin.add_view(ExperienceAdminView(Experience, db.session))
    admin.add_view(ProjectCategoryAdminView(ProjectCategory, db.session))
    admin.add_view(PetAdminView(Pet, db.session))
    admin.add_view(AwardAdminView(Award, db.session))
    admin.add_link(MenuLink(name='Back to Central App', url='/'))


# Initialize login manager
def init_login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id: str) -> User:
        return User.query.get(user_id)


# Register blueprints
def register_blueprints(app):
    app.register_blueprint(main_routes)
    app.register_blueprint(auth_routes)
    app.register_blueprint(project_routes)
    app.register_blueprint(skill_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(blog_routes)
    app.register_blueprint(tutorial_routes)
    app.register_blueprint(services_routes)


# Register context processors
def register_context_processors(app):
    @app.context_processor
    def inject_data() -> dict:
        return {
            'blogs': Blog.query.all(),
            'tutorials': Tutorial.query.all(),
            'projects': Project.query.all(),
            'skills': Skill.query.all(),
            'educations': Education.query.all(),
            'experiences': Experience.query.all(),
            'project_categories': ProjectCategory.query.all(),
            'skill_categories': [category.value for category in SkillCategory],
            'featured_skills': Skill.query.filter_by(is_featured=True).all(),
            'featured_projects': Project.query.filter_by(is_featured=True).all(),
            'featured_pet': Pet.query.filter_by(is_featured=True).first(),
            'awards': Award.query.all(),
            'services': Service.query.all(),
            'pets': Pet.query.all(),
        }


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

    init_db(app)
    init_admin(app)
    init_login_manager(app)
    register_blueprints(app)
    register_context_processors(app)

    # Initialize localization
    babel = Babel()
    babel.init_app(app, locale_selector=lambda: get_locale(app))

    redis_host = app.config.get('REDIS_HOST', 'redis')
    redis_port = app.config.get('REDIS_PORT', 6379)

    storage_uri = f"redis://{redis_host}:{redis_port}"

    default_limits = app.config.get('DEFAULT_LIMITS', "1280 per hour")

    limiter = Limiter(
        app=app,
        key_func=get_remote_address,
        storage_uri=storage_uri,
        default_limits=[default_limits]
    )

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('default/404.html'), 404

    logging.info(f"App created with config: {config_name}")

    app.secret_key = os.environ.get('SECRET_KEY')
    CSRFProtect(app)
    ckeditor = CKEditor(app)
    return app
