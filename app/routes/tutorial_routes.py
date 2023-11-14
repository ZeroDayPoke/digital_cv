#!/usr/bin/env python3
"""
tutorial routes for the Flask application
"""
# Path: app/routes/tutorial_routes.py

from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import login_required
from .route_utils.decorators import admin_required
from ..models import db, Tutorial, Skill
from ..forms import TutorialForm, DeleteTutorialForm
from ..utils.file_upload_helper import handle_file_upload
from app.routes.route_utils import load_skill_choices, load_tutorial_choices

tutorial_routes = Blueprint('tutorial_routes', __name__, url_prefix='')


@tutorial_routes.route('/interface/update_tutorial/<tutorial_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def update_tutorial(tutorial_id):
    tutorial_to_update = Tutorial.query.get_or_404(tutorial_id)
    form = TutorialForm(obj=tutorial_to_update)

    form = load_skill_choices(form)

    if form.validate_on_submit():
        tutorial_to_update.title = form.title.data
        tutorial_to_update.description = form.description.data
        tutorial_to_update.content_file = form.content_file.data
        tutorial_to_update.content_html = form.content_html.data
        tutorial_to_update.related_skills = Skill.query.filter(
            Skill.id.in_(form.related_skills.data)).all()

        image_filename = handle_file_upload("tutorials")
        if image_filename:
            tutorial_to_update.image_filename = image_filename

        db.session.commit()
        flash('Your tutorial has been updated!', 'success')
        return redirect(url_for('tutorial_routes.tutorial_detail', tutorial_id=tutorial_id))

    return render_template('tutorial/update_tutorial.html', form=form, tutorial_id=tutorial_id)


@tutorial_routes.route('/interface/delete_tutorial', methods=['GET', 'POST'])
@login_required
@admin_required
def delete_tutorial():
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
    form = TutorialForm()
    tutorial = Tutorial.query.get(tutorial_id)
    if tutorial is None:
        flash('Tutorial not found', 'error')
        return redirect(url_for('main_routes.index'))

    sections = tutorial.get_sections()
    return render_template('tutorial/tutorial_detail.html', tutorial=tutorial, sections=sections, form=form)


@tutorial_routes.route('/tutorials', methods=['GET'])
def tutorials():
    return render_template('tutorial/tutorials.html')
