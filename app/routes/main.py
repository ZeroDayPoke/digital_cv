#!/usr/bin/env python3
"""
main.py - main routes for the Flask application
"""
# app/routes/main.py

from flask import render_template, request, redirect, url_for, flash, Blueprint
from flask_login import login_required, LoginManager, UserMixin, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash
from ..models import db, Project, Skill, User
from ..forms import ProjectForm, SignupForm, SigninForm

main_routes = Blueprint('main_routes', __name__, url_prefix='')

login_manager = LoginManager()


@main_routes.route('/')
def index():
    return render_template('index.html')


@main_routes.route('/projects')
def projects():
    projects = Project.query.all()
    return render_template('projects.html', projects=projects)

@main_routes.route('/interface', methods=['GET', 'POST'])
@login_required
def interface():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))
    form = ProjectForm()
    form.related_skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]
    if form.validate_on_submit():
        new_project = Project(
            name=form.name.data,
            description=form.description.data,
            role=form.role.data,
            related_skills=Skill.query.filter(Skill.id.in_(form.related_skills.data)).all()
        )
        if form.validate_on_submit():
            print(form.related_skills.data)
        db.session.add(new_project)
        db.session.commit()
        flash('Your project has been added!')
        return redirect(url_for('main_routes.projects'))
    else:
        print(form.errors)
    return render_template('interface.html', form=form)

@main_routes.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main_routes.index'))
    else:
        print(form.errors)
        flash('Invalid email or password. Please try again.')

    return render_template('signup.html', form=form)

@main_routes.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user)
        flash('Successfully signed in.')
        return redirect(url_for('main_routes.index'))
    else:
        flash('Invalid email or password. Please try again.')

    return render_template('signin.html', form=form)

@main_routes.route('/signout', methods=['GET'], strict_slashes=False)
@login_required
def signout():
    """Sign out the current user and redirect to the home page"""
    logout_user()
    flash('Successfully logged out.')
    return render_template('index.html')
