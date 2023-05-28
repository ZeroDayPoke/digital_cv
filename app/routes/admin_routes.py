#!/usr/bin/env python3
"""
admin_routes.py - admin routes for the Flask application
"""
# Path: app/routes/admin_routes.py

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from ..models import db, Project, Skill
from ..forms import ProjectForm, UpdateProjectForm, DeleteProjectForm, SkillForm, DeleteSkillForm

admin_routes = Blueprint('admin_routes', __name__, url_prefix='')

@admin_routes.route('/interface', methods=['GET'])
@login_required
def interface():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))
    form = ProjectForm()
    update_project_form = UpdateProjectForm()
    delete_project_form = DeleteProjectForm()
    skill_form = SkillForm()
    delete_skill_form = DeleteSkillForm()
    form.related_skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]
    update_project_form.project.choices = [(str(project.id), project.name) for project in Project.query.all()]
    update_project_form.related_skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]
    delete_project_form.project.choices = [(str(project.id), project.name) for project in Project.query.all()]
    delete_skill_form.skill.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]
    return render_template('interface.html', title='Interface', form=form, update_project_form=update_project_form, delete_project_form=delete_project_form, skill_form=skill_form, delete_skill_form=delete_skill_form)
