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
    """
    Populate the choices for skill-related fields in a form.

    Args:
        form (Form): A Flask-WTF form object.

    Returns:
        Form: The updated form object with skill choices loaded.
    """
    form.related_skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]
    return form


def load_project_choices(form):
    form.project.choices = [(str(project.id), project.name) for project in Project.query.all()]
    return form


def load_blog_choices(form):
    form.blog.choices = [(str(blog.id), blog.name) for blog in Blog.query.all()]
    return form

def load_tutorial_choices(form):
    form.tutorial.choices = [(str(tutorial.id), tutorial.name) for tutorial in Tutorial.query.all()]
    return form

LOAD_CHOICE_MAP = {
    AddProjectForm: [load_skill_choices],
    UpdateProjectForm: [load_skill_choices, load_project_choices],
    DeleteProjectForm: [load_project_choices],
    AddSkillForm: [],
    DeleteSkillForm: [load_skill_choices],
    AddBlogForm: [load_skill_choices],
    UpdateBlogForm: [load_blog_choices],
    DeleteBlogForm: [load_blog_choices],
    AddTutorialForm: [load_skill_choices],
    UpdateTutorialForm: [load_tutorial_choices],
    DeleteTutorialForm: [load_tutorial_choices]
}

@admin_routes.route('/interface', methods=['GET'])
@login_required
def interface():
    """
    Admin interface for managing Projects, Skills, Blogs, and Tutorials.

    The function initializes forms for different CRUD operations and populates
    choices for SelectFields as necessary.

    Returns:
        Rendered HTML template for the admin interface.
    """
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))
    
    # Initialize and populate form instances.
    form_instances = {}
    for form_class, load_choice_funcs in LOAD_CHOICE_MAP.items():
        form_instance = form_class()
        for func in load_choice_funcs:
            form_instance = func(form_instance)
        form_name = form_class.__name__.lower()
        form_instances[form_name] = form_instance

    return render_template('interface.html', title='Interface', **form_instances)
