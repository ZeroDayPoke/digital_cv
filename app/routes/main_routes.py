#!/usr/bin/env python3
"""
main.py - main routes for the Flask application
"""
# Path: app/routes/main_routes.py

from flask import render_template, request, Blueprint, current_app, redirect, url_for, jsonify, flash
from flask_login import login_required, current_user

from .route_utils.decorators import admin_required
from ..models import Project, Skill, Blog, Message, db
from ..forms import SkillsFilterForm, MessageAdminForm
from app.routes.route_utils import load_skill_choices, load_project_choices, load_blog_choices, load_tutorial_choices

main_routes = Blueprint('main_routes', __name__, url_prefix='')

@main_routes.route('/')
def index():
    return render_template('default/index.html', include_header=True)

@main_routes.route('/about')
def about():
    return render_template('about/main.html', title='About')


@main_routes.route('/resume')
def resume():
    """
    Render the resume page.
    """
    domain_name = current_app.config.get('FLASK_APP_DOMAIN', 'https://zerodaypoke.com')
    pdf_name = current_app.config.get('CV_PDF_NAME', 'dynamic_cv_name.pdf')
    return render_template('resume/main.html', title='Resume', domain_name=domain_name, pdf_name=pdf_name)

@main_routes.route('/exit_admin')
def exit_admin():
    return redirect(url_for('main_routes.index'))

@main_routes.route('/demo')
def demo():
    return render_template('demo.html')

@main_routes.route('/send_message', methods=['POST'])
@login_required
def send_message():
    form = MessageAdminForm()
    if form.validate_on_submit():
        if current_user.verified and not current_user.has_role('ADMIN'):
            new_message = Message(
                sender_id=current_user.id,
                message_body=form.message_body.data
            )
            db.session.add(new_message)
            db.session.commit()
            flash('Message sent successfully.')
            return redirect(url_for('main_routes.index'))
        else:
            flash('Must be verified and not the admin to send.')
            return redirect(url_for('auth_routes.account'))
    else:
        flash('Invalid form.')
        return redirect(url_for('auth_routes.account'))

@main_routes.route('/get_messages', methods=['GET'])
@login_required
@admin_required
def get_messages():
    messages = Message.query.all()
    return jsonify({'messages': [message.message_body for message in messages]}), 200

@main_routes.route('/mark_as_read/<message_id>', methods=['POST'])
@login_required
@admin_required
def mark_as_read(message_id):
    message = Message.query.get(message_id)
    if message:
        message.is_read = True
        db.session.commit()
        return redirect(url_for('auth_routes.account'))
    return jsonify({'status': 'Message not found'}), 404

@main_routes.route('/edit_message', methods=['POST'])
@login_required
def edit_message():
    form = MessageAdminForm()
    if form.validate_on_submit():
        if current_user.verified and not current_user.has_role('ADMIN'):
            existing_message = Message.query.filter_by(sender_id=current_user.id).first()
            if existing_message:
                existing_message.message_body = form.message_body.data
                db.session.commit()
                flash('Message edited successfully.')
            else:
                flash('No existing message to edit.')
            return redirect(url_for('auth_routes.account'))
        else:
            flash('Must be verified and not the admin to edit.')
            return redirect(url_for('auth_routes.account'))
    else:
        flash('Invalid form.')
        return redirect(url_for('auth_routes.account'))
