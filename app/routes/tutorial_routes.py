#!/usr/bin/env python3
"""
tutorial routes for the Flask application
"""
# Path: app/routes/tutorial_routes.py

from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import login_required, current_user
from .route_utils.decorators import admin_required
from ..utils.section_slicer import extract_sections_from_content
from ..models import db, Tutorial, Skill
from ..forms import AddTutorialForm, UpdateTutorialForm, DeleteTutorialForm
from ..utils.file_upload_helper import handle_file_upload
from app.routes.route_utils import load_skill_choices, load_tutorial_choices

tutorial_routes = Blueprint('tutorial_routes', __name__, url_prefix='')


def add_tutorial():
    """
    Route for adding a new tutorial to the database.

    Only users with the 'ADMIN' role can access this route. The function handles GET and POST requests.
    If the form is submitted and validated, a new Tutorial object is created with the data from the form,
    and added to the database. If an image file is uploaded, its filename is stored in the Tutorial object.
    Finally, the user is redirected to the admin interface page.

    :return: A redirect response to the admin interface page.
    """


@tutorial_routes.route('/interface/add_tutorial', methods=['GET', 'POST'])
@login_required
@admin_required
def add_tutorial():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.tutorials'))

    form = load_skill_choices(AddTutorialForm())
    if form.validate_on_submit():
        new_tutorial = Tutorial(
            name=form.name.data,
            description=form.description.data,
            content_file=form.content_file.data,
            related_skills=Skill.query.filter(
                Skill.id.in_(form.related_skills.data)).all()
        )

        image_filename = handle_file_upload("tutorials")
        if image_filename:
            new_tutorial.image_filename = image_filename

        db.session.add(new_tutorial)
        db.session.commit()
        flash('Your tutorial has been added!', 'success')
        return redirect(url_for('admin_routes.interface'))
    return redirect(url_for('admin_routes.interface'))


@tutorial_routes.route('/interface/update_tutorial', methods=['GET', 'POST'])
@login_required
@admin_required
def update_tutorial():
    """
    Update a tutorial in the database.

    If the current user is not an admin, redirect to the tutorials page.
    Otherwise, load the UpdateTutorialForm and validate it on submission.
    If the form is valid, update the tutorial in the database with the form data.
    If an image file is uploaded, update the tutorial's image filename.
    Finally, commit the changes to the database and redirect to the admin interface.

    Returns:
        A redirect response to the admin interface.
    """
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('tutorial_routes.tutorials'))

    form = load_tutorial_choices(load_skill_choices(UpdateTutorialForm()))

    if form.validate_on_submit():
        tutorial_to_update = Tutorial.query.get(form.tutorial.data)
        if tutorial_to_update:
            tutorial_to_update.name = form.name.data
            tutorial_to_update.description = form.description.data
            tutorial_to_update.content_file = form.content_file.data
            tutorial_to_update.related_skills = Skill.query.filter(
                Skill.id.in_(form.related_skills.data)).all()

            image_filename = handle_file_upload("tutorials")
            if image_filename:
                tutorial_to_update.image_filename = image_filename

            db.session.commit()
            flash('Your tutorial has been updated!', 'success')
        else:
            flash('Error: Tutorial not found.', 'danger')
    return redirect(url_for('admin_routes.interface'))


@tutorial_routes.route('/interface/delete_tutorial', methods=['GET', 'POST'])
@login_required
@admin_required
def delete_tutorial():
    """
    Route for deleting a tutorial.

    If the current user is not an admin, they will be redirected to the tutorials page.
    Otherwise, a form will be loaded with the available tutorial choices.
    If the form is submitted and valid, the selected tutorial will be deleted from the database.
    If the tutorial is not found, an error message will be flashed.
    After the tutorial is deleted, the user will be redirected to the admin interface page.
    """
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('tutorial_routes.tutorials'))

    form = load_tutorial_choices(DeleteTutorialForm())

    if form.validate_on_submit():
        tutorial_to_delete = Tutorial.query.get(form.tutorial.data)
        if tutorial_to_delete:
            db.session.delete(tutorial_to_delete)
            db.session.commit()
            flash('Your tutorial has been deleted!', 'success')
        else:
            flash('Error: Tutorial not found.', 'danger')
    return redirect(url_for('admin_routes.interface'))


@tutorial_routes.route('/tutorial/<tutorial_id>', methods=['GET'])
def tutorial_detail(tutorial_id):
    tutorial = Tutorial.query.get(tutorial_id)
    if tutorial is None:
        flash('Tutorial not found', 'error')
        return redirect(url_for('main_routes.index'))
    content_file_path = 'app/templates/tutorial/' + tutorial.content_file + '.html'
    sections = extract_sections_from_content(content_file_path)
    return render_template('tutorial/tutorial_detail.html', tutorial=tutorial, sections=sections)


@tutorial_routes.route('/tutorials', methods=['GET'])
def tutorials():
    return render_template('tutorial/tutorials.html')
