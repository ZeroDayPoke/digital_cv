#!/usr/bin/env python3
"""
tutorial routes for the Flask application
"""
# Path: app/routes/tutorial_routes.py

from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import login_required, current_user
from ..utils.section_slicer import extract_sections_from_content
from ..models import db, Tutorial, Skill
from ..forms import AddTutorialForm, UpdateTutorialForm, DeleteTutorialForm

tutorial_routes = Blueprint('tutorial_routes', __name__, url_prefix='')


@tutorial_routes.route('/interface/add_tutorial', methods=['GET', 'POST'])
@login_required
def add_tutorial():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.tutorials'))
    form = AddTutorialForm()
    form.related_skills.choices = [
        (str(skill.id), skill.name) for skill in Skill.query.all()]
    if form.validate_on_submit():
        new_tutorial = Tutorial(
            name=form.name.data,
            description=form.description.data,
            content_file=form.content_file.data,
            related_skills=Skill.query.filter(
                Skill.id.in_(form.related_skills.data)).all()
        )
        db.session.add(new_tutorial)
        db.session.commit()
        flash('Your tutorial has been added!', 'success')
        return redirect(url_for('admin_routes.interface'))
    return redirect(url_for('admin_routes.interface'))


@tutorial_routes.route('/interface/update_tutorial', methods=['GET', 'POST'])
@login_required
def update_tutorial():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('tutorial_routes.tutorials'))
    form = UpdateTutorialForm()
    form.tutorial.choices = [(str(tutorial.id), tutorial.name)
                             for tutorial in Tutorial.query.all()]
    form.related_skills.choices = [
        (str(skill.id), skill.name) for skill in Skill.query.all()]
    if form.validate_on_submit():
        tutorial = Tutorial.query.get(form.tutorial.data)
        tutorial.name = form.name.data
        tutorial.description = form.description.data
        tutorial.content_file = form.content_file.data
        tutorial.related_skills = Skill.query.filter(
            Skill.id.in_(form.related_skills.data)).all()
        db.session.commit()
        flash('Your tutorial has been updated!', 'success')
        return redirect(url_for('admin_routes.interface'))
    return redirect(url_for('admin_routes.interface'))


@tutorial_routes.route('/interface/delete_tutorial', methods=['GET', 'POST'])
@login_required
def delete_tutorial():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('tutorial_routes.tutorials'))
    form = DeleteTutorialForm()
    form.tutorial.choices = [(str(tutorial.id), tutorial.name)
                             for tutorial in Tutorial.query.all()]
    if form.validate_on_submit():
        tutorial = Tutorial.query.get(form.tutorial.data)
        db.session.delete(tutorial)
        db.session.commit()
        flash('Your tutorial has been deleted!', 'success')
        return redirect(url_for('admin_routes.interface'))
    return redirect(url_for('admin_routes.interface'))

@tutorial_routes.route('/tutorial/<tutorial_id>', methods=['GET'])
def tutorial_detail(tutorial_id):
    tutorial = Tutorial.query.get(tutorial_id)
    if tutorial is None:
        flash('Tutorial not found', 'error')
        return redirect(url_for('main_routes.index'))
    content_file_path = 'app/templates/tutorial/' + tutorial.content_file + '.html'
    sections = extract_sections_from_content(content_file_path)
    return render_template('tutorial_detail.html', tutorial=tutorial, sections=sections)

@tutorial_routes.route('/tutorials', methods=['GET'])
def tutorials():
    tutorials = Tutorial.query.all()
    return render_template('tutorials.html', tutorials=tutorials)
