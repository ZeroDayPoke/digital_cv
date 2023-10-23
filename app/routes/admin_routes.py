#!/usr/bin/env python3
"""
admin_routes.py - admin routes for the Flask application
"""
# Path: app/routes/admin_routes.py

import os
from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from app.routes.route_utils import (
    load_project_choices, load_skill_choices, load_blog_choices, load_tutorial_choices
)
from werkzeug.utils import secure_filename
from ..forms import (
    AddProjectForm, UpdateProjectForm, DeleteProjectForm, 
    AddSkillForm, DeleteSkillForm,
    DeleteBlogForm, UpdateBlogForm, AddBlogForm, 
    AddTutorialForm, UpdateTutorialForm, DeleteTutorialForm,
    UploadCVForm
)
from decouple import Config

config = Config('.env')

admin_routes = Blueprint('admin_routes', __name__, url_prefix='')

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

    form = UploadCVForm()

    # Initialize and populate form instances.
    form_instances = {}
    for form_class, load_choice_funcs in LOAD_CHOICE_MAP.items():
        form_instance = form_class()
        for func in load_choice_funcs:
            form_instance = func(form_instance)
        form_name = form_class.__name__.lower()
        form_instances[form_name] = form_instance

    return render_template('interface.html', title='Interface', **form_instances, form=form)

@admin_routes.route('/upload_cv', methods=['POST'])
@login_required
def upload_cv():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main.index'))

    form = UploadCVForm()
    if form.validate_on_submit():
        file = form.cv.data

        # Get the CV name from the environment variables
        cv_pdf_name = config.get('CV_PDF_NAME', 'default_cv_name.pdf')
        
        # Secure the filename
        filename = secure_filename(cv_pdf_name)
        
        # Save the file
        file.save(os.path.join(current_app.config.get('CV_UPLOAD_FOLDER', 'app/static/cv/'), filename))
        
        flash('CV uploaded successfully', 'success')
    return redirect(url_for('admin_routes.interface'))

@admin_routes.route('/go_to_admin', methods=['GET'])
@login_required
def go_to_admin():
    """
    Redirects to the default Flask-Admin interface if the user has an ADMIN role.
    """
    if current_user.has_role('ADMIN'):
        return redirect('/admin/')
    else:
        flash('You do not have permission to access the admin interface.', 'danger')
        return redirect(url_for('main_routes.projects'))
