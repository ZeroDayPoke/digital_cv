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
    """
    View function for the signup page.

    GET: Renders the signup form.
    POST: Validates the form data and creates a new user if the data is valid.

    Returns:
        GET: Rendered signup form.
        POST: Redirects to the index page if the user is created successfully, otherwise redirects back to the signup page.
    """
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter(
            (User.username == form.username.data) | (User.email == form.email.data)
        ).first()

        if existing_user:
            if existing_user.username == form.username.data:
                flash('Username already in use.')
            if existing_user.email == form.email.data:
                flash('Email address already in use.')
            return redirect(url_for('auth_routes.signup'))

        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        send_verification_email_result = send_verification_email()
        if "Verification email sent" in send_verification_email_result:
            flash('Congratulations, you are now a registered user! A verification email has been sent to your email address.')
        else:
            flash('Congratulations, you are now a registered user! However, we could not send a verification email.')

        return redirect(url_for('main_routes.index'))
    return render_template('signup.html', form=form)

@auth_routes.route('/signin', methods=['GET', 'POST'])
def signin():
    """
    Renders a signin form for the user to enter their email and password.
    If the form is submitted and valid, it checks if the email exists in the database.
    If the email exists, it checks if the password is correct.
    If the password is correct, it logs in the user and redirects to the index page.
    If the email does not exist or the password is incorrect, it flashes an error message and redirects to the signin page.
    """
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            if not user.check_password(form.password.data):
                flash('Incorrect password.')
                return redirect(url_for('auth_routes.signin'))
            login_user(user)
            flash('Successfully signed in.')
        else:
            flash('Email does not exist.')
        
        return redirect(url_for('main_routes.index'))
    return render_template('signin.html', form=form)

@auth_routes.route('/signout', methods=['GET'])
@login_required
def signout():
    """
    Signs out the current user if they are authenticated, and redirects to the index page.
    If the user is not authenticated, a message is flashed indicating that they are not signed in.
    """
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
    """
    Sends a verification email to the current user's email address and saves the verification token in the database.

    Returns:
        str: A message indicating whether the email was sent successfully or not.
    """
    user_email = current_user.email
    email_service_url = current_app.config.get('EMAIL_SERVICE_URL', 'http://localhost:3000/send-email')
    
    try:
        response = requests.post(email_service_url, json={'to': user_email})
        if response.status_code == 200:
            token = response.json().get('token')
            if token:
                current_user.verification_token = token
                db.session.commit()
                message = 'Verification email sent! Check your inbox for the verification link.'
            else:
                message = 'Error processing the verification email.'
            flash(message)
            return message
        else:
            flash('There was an error sending the verification email. Please try again later.')
    except requests.RequestException:
        flash('Network error while sending verification email.')

    return "Verification email could not be sent", 500


@auth_routes.route('/verify_account_email/<token>', methods=['GET'])
def verify_account_email(token):
    """
    Verify the user's account email using the verification token.

    Args:
        token (str): The verification token.

    Returns:
        redirect: Redirects the user to the appropriate page based on the verification status.
    """
    user = User.query.filter_by(verification_token=token).first()
    if user is None:
        flash('Invalid verification link.')
        return redirect(url_for('main_routes.index'))
    elif user.token_expired():
        flash('Expired verification link.')
        return redirect(url_for('main_routes.index'))
    else:
        user.verified = True
        user.verification_token = None
        user.token_generated_at = None
        db.session.commit()
        flash('Account successfully verified!')
        return redirect(url_for('main_routes.account'))


@auth_routes.route('/change_password', methods=['POST'])
@login_required
def change_password():
    """
    Endpoint for changing user password.

    Accepts POST requests with the following form data:
    - current_password: string, required
    - new_password: string, required
    - confirm_password: string, required

    If the current password is incorrect, the function flashes an error message and redirects to the account page.
    If the new password and confirm password do not match, the function flashes an error message and redirects to the account page.
    If the password change is successful, the function flashes a success message and redirects to the account page.
    """
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
