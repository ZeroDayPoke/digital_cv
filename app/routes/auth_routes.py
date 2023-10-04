#!/usr/bin/env python3
"""
auth_routes.py - authentication routes for the Flask application
"""
# Path: app/routes/auth_routes.py

import requests
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
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

@auth_routes.route('/signout', methods=['GET'])
@login_required
def signout():
    """Sign out the current user and redirect to the home page"""
    logout_user()
    flash('Successfully logged out.')
    return render_template('index.html')

@auth_routes.route('/account', methods=['GET'])
@login_required
def account():
    return render_template('account.html')

@auth_routes.route('/send_verification_email', methods=['GET'])
@login_required
def send_verification_email():
    user_email = current_user.email

    response = requests.post('http://localhost:3000/send-email', json={'to': user_email})

    if response.status_code == 200:
        token = response.json()['token']
        current_user.verification_token = token
        db.session.commit()

        return 'Verification email sent! Check your inbox for the verification link.'
    else:
        return 'There was an error sending the verification email. Please try again later.', 500

@auth_routes.route('/verify-account/<token>', methods=['GET'])
def verify_account(token):
    user = User.query.filter_by(verification_token=token).first()
    if user and not user.token_expired():
        user.verified = True
        user.verification_token = None
        user.token_generated_at = None
        db.session.commit()
        return 'Account successfully verified!'
    else:
        return 'Invalid or expired verification link!', 400

@auth_routes.route('/change_password', methods=['POST'])
@login_required
def change_password():
    current_password = requests.request.form.get('current_password')
    new_password = requests.request.form.get('new_password')
    confirm_password = requests.request.form.get('confirm_password')

    if not current_user.check_password(current_password):
        flash('Incorrect current password.')
        return redirect(url_for('auth_routes.account'))

    if new_password != confirm_password:
        flash('New password and confirm password do not match.')
        return redirect(url_for('auth_routes.account'))

    current_user.password = generate_password_hash(new_password)
    db.session.commit()
    flash('Password changed successfully.')
    return redirect(url_for('auth_routes.account'))
