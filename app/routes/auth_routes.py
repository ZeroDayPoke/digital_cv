#!/usr/bin/env python3
"""
auth_routes.py - authentication routes for the Flask application
"""
# Path: app/routes/auth_routes.py

import requests
from flask import Blueprint, render_template, redirect, url_for, flash, current_app, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from ..models import db, User
from ..forms import SignupForm, SigninForm

auth_routes = Blueprint('auth_routes', __name__, url_prefix='')

@auth_routes.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        existing_email = User.query.filter_by(email=form.email.data).first()
        if existing_user or existing_email:
            flash('Email address already in use. Please use a different email or sign in.')
            return redirect(url_for('auth_routes.signup'))

        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Log in the new user so that current_user can be used
        login_user(new_user)

        # Send verification email after successful registration
        send_verification_email_result = send_verification_email()
        if "Verification email sent" in send_verification_email_result:
            flash('Congratulations, you are now a registered user! A verification email has been sent to your email address.')
        else:
            flash('Congratulations, you are now a registered user! However, we could not send a verification email.')

        return redirect(url_for('main_routes.index'))
    return render_template('signup.html', form=form)

@auth_routes.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password.')
            return redirect(url_for('auth_routes.signin'))
        login_user(user)
        flash('Successfully signed in.')
        return redirect(url_for('main_routes.index'))
    return render_template('signin.html', form=form)

@auth_routes.route('/signout', methods=['GET'])
@login_required
def signout():
    """Sign out the current user and redirect to the home page"""
    if current_user.is_authenticated:
        logout_user()
        flash('Successfully signed out.')
    else:
        flash('You are not signed in.')
    return redirect(url_for('main_routes.index'))

@auth_routes.route('/account', methods=['GET'])
@login_required
def account():
    return render_template('account.html')

@auth_routes.route('/send_verification_email', methods=['GET'])
@login_required
def send_verification_email():
    user_email = current_user.email
    email_service_url = current_app.config.get('EMAIL_SERVICE_URL', 'http://localhost:3000/send-email')

    response = requests.post(email_service_url, json={'to': user_email})

    if response.status_code == 200:
        token = response.json().get('token')
        if token:
            current_user.verification_token = token
            db.session.commit()
            message = 'Verification email sent! Check your inbox for the verification link.'
        else:
            message = 'Error processing the verification email.'
        return message
    else:
        message = 'There was an error sending the verification email. Please try again later.'
        return message, 500


@auth_routes.route('/verify_account_email/<token>', methods=['GET'])
def verify_account_email(token):
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
    current_password = request.form.get('current_password')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')

    if not current_user.check_password(current_password):
        flash('Incorrect current password.')
        return redirect(url_for('auth_routes.account'))

    if new_password != confirm_password:
        flash('New password and confirm password do not match.')
        return redirect(url_for('auth_routes.account'))

    current_user.password_hash = generate_password_hash(new_password)
    db.session.commit()
    flash('Password changed successfully.')
    return redirect(url_for('auth_routes.account'))
