#!/usr/bin/env python3
"""
admin_routes.py - admin routes for the Flask application
"""
# Path: app/routes/admin_routes.py

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from ..models import db, Project, Skill, Blog, Tutorial
from ..forms import (
    AddProjectForm, UpdateProjectForm, DeleteProjectForm, 
    AddSkillForm, DeleteSkillForm,
    DeleteBlogForm, UpdateBlogForm, AddBlogForm, 
    AddTutorialForm, UpdateTutorialForm, DeleteTutorialForm
)

admin_routes = Blueprint('admin_routes', __name__, url_prefix='')


def load_skill_choices(form):
    form.related_skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]
    return form


def load_project_choices(form):
    form.project.choices = [(str(project.id), project.name) for project in Project.query.all()]
    return form


def load_blog_choices(form):
    form.blog.choices = [(str(blog.id), blog.name) for blog in Blog.query.all()]
    return form


@admin_routes.route('/interface', methods=['GET'])
@login_required
def interface():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))
    
    # Load forms
    add_project_form = load_skill_choices(AddProjectForm())
    update_project_form = load_project_choices(load_skill_choices(UpdateProjectForm()))
    delete_project_form = load_project_choices(DeleteProjectForm())

    add_skill_form = AddSkillForm()
    delete_skill_form = load_skill_choices(DeleteSkillForm())

    add_blog_form = load_skill_choices(AddBlogForm())
    update_blog_form = load_blog_choices(UpdateBlogForm())
    delete_blog_form = load_blog_choices(DeleteBlogForm())

    add_tutorial_form = load_skill_choices(AddTutorialForm())

    return render_template('interface.html', title='Interface',
                           add_skill_form=add_skill_form,
                           delete_skill_form=delete_skill_form,
                           add_project_form=add_project_form,
                           update_project_form=update_project_form,
                           delete_project_form=delete_project_form,
                           add_blog_form=add_blog_form,
                           update_blog_form=update_blog_form,
                           add_tutorial_form=add_tutorial_form,
                           delete_blog_form=delete_blog_form)
