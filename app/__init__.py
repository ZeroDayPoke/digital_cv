#!/usr/bin/env python3
"""
__init__ file for app module

# Path: digital_cv/app/__init__.py
"""

from flask import Flask, request, g, redirect, url_for, flash
from flask_login import LoginManager
from flask_babel import Babel, gettext as _
from flask_admin import Admin
from config import config
from admin import AdminModelView, ProjectAdminView, SkillAdminView, BlogAdminView, TutorialAdminView
from .models import db, User, Blog, Tutorial, Skill, Project
from .routes import main_routes, auth_routes, project_routes, skill_routes, admin_routes, blog_routes, tutorial_routes

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_blueprint(main_routes)
    app.register_blueprint(auth_routes)
    app.register_blueprint(project_routes)
    app.register_blueprint(skill_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(blog_routes)
    app.register_blueprint(tutorial_routes)
    app.url_map.strict_slashes = False

    babel = Babel()

    def get_locale():
        # 1. Locale from URL parameters
        requested_locale = request.args.get('locale')
        print(requested_locale)
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale

        # 2. Locale from user settings
        user = g.get('user', None)
        if user:
            user_locale = user.get('locale')
            if user_locale in app.config['LANGUAGES']:
                return user_locale

        # 3. Locale from request
        best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
        if best_match:
            return best_match

        # 4. Default locale
        return app.config['BABEL_DEFAULT_LOCALE']

    babel.init_app(app, locale_selector=get_locale)

    admin = Admin(app, name='AdInt', template_mode='bootstrap4')
    admin.add_view(ProjectAdminView(Project, db.session))
    admin.add_view(SkillAdminView(Skill, db.session))
    admin.add_view(BlogAdminView(Blog, db.session))
    admin.add_view(TutorialAdminView(Tutorial, db.session))

    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthorized():
        flash('You must be logged in to view that page.')
        return redirect(url_for('main_routes.index'))

    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # Retrieve the user object based on the user_id
        user = User.query.get(user_id)
        return user

    @app.context_processor
    def inject_blogs():
        blogs = Blog.query.all()
        return dict(blogs=blogs)
    
    @app.context_processor
    def inject_tutorials():
        tutorials = Tutorial.query.all()
        return dict(tutorials=tutorials)

    print("App created with config: " + config_name)
    return app
