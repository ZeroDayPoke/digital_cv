#!/usr/bin/env python3
"""
admin_routes.py - admin routes for the Flask application
"""
# Path: app/routes/admin_routes.py

import json
import os
from app.models import Project, Pet, db
from flask import Blueprint, render_template, redirect, url_for, flash, current_app, request
from flask_login import login_required
from werkzeug.utils import secure_filename
from ..forms import (
    UploadCVForm, AddProjectForm, UpdateProjectForm, DeleteProjectForm,
    ImageSkillForm, ImageSkillForm, ImageSkillForm,
    AddBlogForm, UpdateBlogForm, DeleteBlogForm,
    TutorialForm, DeleteTutorialForm, PetForm, ImagePetForm, PetImageForm
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
    UpdateProjectForm: [load_skill_choices],
    DeleteProjectForm: [load_project_choices],
    ImageSkillForm: [],
    ImageSkillForm: [load_skill_choices],
    ImageSkillForm: [],
    AddBlogForm: [load_skill_choices],
    UpdateBlogForm: [load_blog_choices],
    DeleteBlogForm: [load_blog_choices],
    DeleteTutorialForm: [load_tutorial_choices]
}


@admin_routes.route('/interface', methods=['GET'])
def interface():
    form = UploadCVForm()
    form_instances = {}

    project_one = Project.query.first()

    for form_class, load_choice_funcs in LOAD_CHOICE_MAP.items():
        form_instance = form_class()

        for func in load_choice_funcs:
            form_instance = func(form_instance)

        form_name = form_class.__name__.lower()
        form_instances[form_name] = form_instance

    return render_template(
        'admin/interface.html',
        title='Interface',
        **form_instances,
        form=form,
    )


@admin_routes.route('/upload_cv', methods=['POST'])
def upload_cv():
    form = UploadCVForm()
    if form.validate_on_submit():
        file = form.cv.data
        cv_pdf_name = config.get('CV_PDF_NAME', 'default_cv_name.pdf')
        filename = secure_filename(cv_pdf_name)
        file.save(os.path.join(current_app.config.get(
            'CV_UPLOAD_FOLDER', 'app/static/cv/'), filename))
        flash('CV uploaded successfully', 'success')
    return redirect(url_for('admin_routes.interface'))


@admin_routes.route('/go_to_admin', methods=['GET'])
def go_to_admin():
    return redirect('/admin/')


@admin_routes.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    form = ImagePetForm()
    if form.validate_on_submit():
        new_pet = Pet(
            name=form.name.data,
            breed=form.breed.data,
            description=form.description.data,
            images=json.loads(form.images.data),
            is_featured=form.is_featured.data
        )
        db.session.add(new_pet)
        db.session.commit()
        flash('Pet added successfully', 'success')
        return redirect(url_for('admin_routes.interface'))

    return render_template('admin/add_pet.html', form=form)


@admin_routes.route('/update_pet/<pet_id>', methods=['GET', 'POST'])
def update_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm()

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.breed = form.breed.data
        pet.description = form.description.data
        pet.is_featured = form.is_featured.data

        # Extract image data from the form
        images_data = []
        for image_form in form.images:
            image_data = {
                'filename': image_form.filename.data,
                'description': image_form.img_description.data
            }
            images_data.append(image_data)
        pet.images = images_data

        db.session.commit()
        flash('Pet updated successfully')
        return redirect(url_for('admin_routes.some_route'))

    elif request.method == 'GET':
        form.name.data = pet.name
        form.breed.data = pet.breed
        form.description.data = pet.description
        form.is_featured.data = pet.is_featured

        while len(form.images) > 0:
            form.images.pop_entry()

        for image_info in pet.images:
            image_form = PetImageForm()
            image_form.filename.data = image_info.get('filename', '')
            image_form.img_description.data = image_info.get('description', '')
            form.images.append_entry(image_form)

    return render_template('admin/update_pet.html', form=form, pet_id=pet_id)

@admin_routes.route('/delete_pet/<pet_id>', methods=['POST'])
def delete_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    db.session.delete(pet)
    db.session.commit()
    flash('Pet deleted successfully', 'success')
    return redirect(url_for('admin_routes.interface'))
