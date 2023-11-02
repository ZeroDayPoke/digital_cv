#!/usr/bin/env python3
"""
admin_routes.py - admin routes for the Flask application
"""
# Path: app/routes/admin_routes.py

import os
from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from flask_login import login_required
from werkzeug.utils import secure_filename
from ..forms import (
    UploadCVForm, AddProjectForm, UpdateProjectForm, DeleteProjectForm,
    AddSkillForm, DeleteSkillForm, UpdateSkillForm,
    AddBlogForm, UpdateBlogForm, DeleteBlogForm,
    AddTutorialForm, UpdateTutorialForm, DeleteTutorialForm
)
from .route_utils.decorators import admin_required
from decouple import Config
from .route_utils import (
    load_project_choices, load_skill_choices, load_blog_choices, load_tutorial_choices
)

config = Config('.env')
admin_routes = Blueprint('admin_routes', __name__, url_prefix='')

@admin_routes.before_request
@login_required
@admin_required
def before_request():
    pass

LOAD_CHOICE_MAP = {
    AddProjectForm: [load_skill_choices],
    UpdateProjectForm: [load_skill_choices, load_project_choices],
    DeleteProjectForm: [load_project_choices],
    AddSkillForm: [],
    DeleteSkillForm: [load_skill_choices],
    UpdateSkillForm: [load_skill_choices],
    AddBlogForm: [load_skill_choices],
    UpdateBlogForm: [load_blog_choices],
    DeleteBlogForm: [load_blog_choices],
    AddTutorialForm: [load_skill_choices],
    UpdateTutorialForm: [load_tutorial_choices],
    DeleteTutorialForm: [load_tutorial_choices]
}

@admin_routes.route('/interface', methods=['GET'])
def interface():
    form = UploadCVForm()
    form_instances = {}
    for form_class, load_choice_funcs in LOAD_CHOICE_MAP.items():
        form_instance = form_class()
        for func in load_choice_funcs:
            form_instance = func(form_instance)
        form_name = form_class.__name__.lower()
        form_instances[form_name] = form_instance
    return render_template('admin/interface.html', title='Interface', **form_instances, form=form)

@admin_routes.route('/upload_cv', methods=['POST'])
def upload_cv():
    form = UploadCVForm()
    if form.validate_on_submit():
        file = form.cv.data
        cv_pdf_name = config.get('CV_PDF_NAME', 'default_cv_name.pdf')
        filename = secure_filename(cv_pdf_name)
        file.save(os.path.join(current_app.config.get('CV_UPLOAD_FOLDER', 'app/static/cv/'), filename))
        flash('CV uploaded successfully', 'success')
    return redirect(url_for('admin_routes.interface'))

@admin_routes.route('/go_to_admin', methods=['GET'])
def go_to_admin():
    return redirect('/admin/')
