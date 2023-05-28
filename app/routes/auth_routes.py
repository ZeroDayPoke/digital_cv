#!/usr/bin/env python3
"""
auth_routes.py - authentication routes for the Flask application
"""
# Path: app/routes/auth_routes.py

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash
from ..models import db, User
from ..forms import SignupForm, SigninForm

auth_routes = Blueprint('auth_routes', __name__, url_prefix='')

@auth_routes.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main_routes.index'))
    return render_template('signup.html', form=form)

@auth_routes.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user)
        flash('Successfully signed in.')
        return redirect(url_for('main_routes.index'))
    return render_template('signin.html', form=form)

@auth_routes.route('/signout', methods=['GET'], strict_slashes=False)
@login_required
def signout():
    """Sign out the current user and redirect to the home page"""
    logout_user()
    flash('Successfully logged out.')
    return render_template('index.html')
