#!/usr/bin/env python3
"""
project_routes.py - project routes for the Flask application
"""
# Path: app/routes/project_routes.py

from requests import request
from flask import Blueprint, redirect, url_for, flash, render_template, jsonify
from flask_login import login_required
from ..models import db, Project, Skill
from ..forms import AddProjectForm, UpdateProjectForm, DeleteProjectForm
from ..utils.file_upload_helper import handle_file_upload
from app.routes.route_utils import load_skill_choices, load_project_choices, load_category_choices
from app.routes.route_utils.decorators import admin_required

project_routes = Blueprint('project_routes', __name__, url_prefix='')


@project_routes.route('/interface/add_project', methods=['GET', 'POST'])
@login_required
@admin_required
def add_project():
    form = AddProjectForm()
    form = load_skill_choices(form)
    form = load_category_choices(form)

    if form.validate_on_submit():
        new_project = Project(
            name=form.name.data,
            description=form.description.data,
            role=form.role.data,
            repo_link=form.repo_link.data,
            live_link=form.live_link.data,
            category_id=form.category.data,
            related_skills=Skill.query.filter(Skill.id.in_(form.related_skills.data)).all()
        )

        image_filename = handle_file_upload("projects")
        if image_filename:
            new_project.image_filename = image_filename

        db.session.add(new_project)
        db.session.commit()
        flash('Your project has been added!', 'success')
        return redirect(url_for('admin_routes.interface'))

    return redirect(url_for('admin_routes.interface'))


@project_routes.route('/interface/update_project/<project_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    form = UpdateProjectForm(obj=project)
    form = load_project_choices(form)
    form = load_skill_choices(form)
    form = load_category_choices(form)

    if request.method == 'GET':
        form.project.data = project_id
        form.name.data = project.name
        form.description.data = project.description
        form.role.data = project.role
        form.repo_link.data = project.repo_link
        form.live_link.data = project.live_link
        form.category.data = project.category_id
        form.related_skills.data = [skill.id for skill in project.related_skills]

    elif request.method == 'POST' and form.validate_on_submit():
        project.name = form.name.data
        project.description = form.description.data
        project.role = form.role.data
        project.repo_link = form.repo_link.data
        project.live_link = form.live_link.data
        project.category_id = form.category.data
        project.related_skills = Skill.query.filter(Skill.id.in_(form.related_skills.data)).all()

        image_filename = handle_file_upload("projects")
        if image_filename:
            project.image_filename = image_filename

        db.session.commit()
        flash('Project has been updated!', 'success')
        return redirect(url_for('admin_routes.interface'))

    return redirect(url_for('admin_routes.interface'))


@project_routes.route('/interface/delete_project', methods=['POST'])
@login_required
@admin_required
def delete_project():
    form = DeleteProjectForm()
    form = load_project_choices(form)

    if form.validate_on_submit():
        project_to_delete = Project.query.get(form.project.data)
        if project_to_delete:
            db.session.delete(project_to_delete)
            db.session.commit()
            flash('Project has been deleted!', 'success')
        else:
            flash('Error: Project not found.', 'danger')
    return redirect(url_for('admin_routes.interface'))


@project_routes.route('/project/<project_id>', methods=['GET'])
def project_details(project_id):
    project = Project.query.get_or_404(project_id)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':

        project_data = {
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'role': project.role,
            'repo_link': project.repo_link,
            'live_link': project.live_link,
            'misc_link': project.misc_link,
            'misc_name': project.misc_name,
            'status': project.status,
            'category_id': project.category_id,
            'related_skills': [skill.id for skill in project.related_skills]
        }

        return jsonify(project_data)
    
    return render_template('project_details.html', project=project)
