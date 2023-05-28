#!/usr/bin/env python3
"""
project_routes.py - project routes for the Flask application
"""
# Path: app/routes/project_routes.py

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import db, Project, Skill
from ..forms import ProjectForm, UpdateProjectForm, DeleteProjectForm

project_routes = Blueprint('project_routes', __name__, url_prefix='')


@project_routes.route('/interface/update_project', methods=['GET', 'POST'])
@login_required
def update_project():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))
    form = UpdateProjectForm()
    form.project.choices = [(str(project.id), project.name) for project in Project.query.all()]
    form.related_skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]
    if form.validate_on_submit():
        project_to_update = Project.query.get(form.project.data)
        if project_to_update:
            project_to_update.name = form.name.data
            project_to_update.description = form.description.data
            project_to_update.role = form.role.data
            project_to_update.related_skills = Skill.query.filter(Skill.id.in_(form.related_skills.data)).all()
            db.session.commit()
            flash('Project has been updated!', 'success')
        else:
            flash('Error: Project not found.', 'danger')
    return redirect(url_for('admin_routes.interface'))


@project_routes.route('/interface/delete_project', methods=['POST'])
@login_required
def delete_project():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))
    form = DeleteProjectForm()
    form.project.choices = [(str(project.id), project.name) for project in Project.query.all()]
    if form.validate_on_submit():
        project_to_delete = Project.query.get(form.project.data)
        if project_to_delete:
            db.session.delete(project_to_delete)
            db.session.commit()
            flash('Project has been deleted!', 'success')
        else:
            flash('Error: Project not found.', 'danger')
    return redirect(url_for('admin_routes.interface'))


@project_routes.route('/interface/add_project', methods=['GET', 'POST'])
@login_required
def add_project():
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
        db.session.add(new_project)
        db.session.commit()
        flash('Your project has been added!', 'success')
        return redirect(url_for('admin_routes.interface'))
    return render_template('interface.html', title='Interface', form=form)
