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

# Mapping of models to their respective forms
MODEL_FORM_MAP = {
    Skill: [AddSkillForm, DeleteSkillForm],
    Project: [AddProjectForm, UpdateProjectForm, DeleteProjectForm],
    Blog: [AddBlogForm, UpdateBlogForm, DeleteBlogForm],
    Tutorial: [AddTutorialForm, UpdateTutorialForm, DeleteTutorialForm]
}

def load_choices(form, model):
    form.choices = [(str(item.id), item.name) for item in model.query.all()]
    return form

@admin_routes.route('/interface', methods=['GET'])
@login_required
def interface():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))
    
    # Load forms dynamically
    forms = {}
    for model, form_classes in MODEL_FORM_MAP.items():
        for form_class in form_classes:
            form_name = form_class.__name__.lower()
            if 'skill' in form_name:
                forms[form_name] = load_choices(form_class(), Skill)
            else:
                forms[form_name] = load_choices(form_class(), model)

    return render_template('interface.html', title='Interface', forms=forms, **forms)
