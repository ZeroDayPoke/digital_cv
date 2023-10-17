#!/usr/bin/env python3
"""
main.py - main routes for the Flask application
"""
# Path: app/routes/main_routes.py

from flask import render_template, request, Blueprint, current_app, redirect, url_for, jsonify, flash
from flask_login import login_required, current_user

from ..models import Project, Skill, Blog, Message, db
from ..forms import SkillsFilterForm, MessageAdminForm
from app.routes.route_utils import load_skill_choices, load_project_choices, load_blog_choices, load_tutorial_choices

main_routes = Blueprint('main_routes', __name__, url_prefix='')

@main_routes.route('/')
def index():
    return render_template('index.html', include_header=True)

@main_routes.route('/about')
def about():
    return render_template('about.html', title='About')

@main_routes.route('/projects', methods=['GET', 'POST'])
def projects():
    form = SkillsFilterForm(request.form)
    form.skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]

    if request.method == 'POST' and form.validate():
        selected_skills = form.skills.data
        projects = Project.query.filter(Project.related_skills.any(Skill.id.in_(selected_skills))).all()
    else:
        projects = Project.query.all()

    return render_template('projects.html', projects=projects, form=form)

@main_routes.route('/blogs', methods=['GET', 'POST'])
def blogs():
    form = SkillsFilterForm(request.form)
    form.skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]

    if request.method == 'POST' and form.validate():
        selected_skills = form.skills.data
        blogs = Blog.query.filter(Blog.related_skills.any(Skill.id.in_(selected_skills))).all()
    else:
        blogs = Blog.query.all()

    return render_template('blogs.html', blogs=blogs, form=form)

@main_routes.route('/resume')
def resume():
    """
    Render the resume page.
    """
    domain_name = current_app.config.get('DOMAIN_NAME', 'https://zerodaypoke.com')
    pdf_name = current_app.config.get('CV_PDF_NAME', 'dynamic_cv_name.pdf')
    return render_template('resume/main.html', title='Resume', domain_name=domain_name, pdf_name=pdf_name)

@main_routes.route('/exit_admin')
def exit_admin():
    return redirect(url_for('main_routes.index'))

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
def get_messages():
    if current_user.has_role('ADMIN'):
        messages = Message.query.all()
        return jsonify({'messages': [message.message_body for message in messages]}), 200

    return jsonify({'status': 'Unauthorized'}), 403

@main_routes.route('/mark_as_read/<message_id>', methods=['POST'])
@login_required
def mark_as_read(message_id):
    if not current_user.has_role('ADMIN'):
        return jsonify({'status': 'Unauthorized'}), 403
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
