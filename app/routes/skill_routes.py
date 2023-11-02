#!/usr/bin/env python3
"""
skill_routes.py - skill routes for the Flask application
"""
# Path: app/routes/skill_routes.py

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import db, Skill, SkillLevel
from ..forms import AddSkillForm, DeleteSkillForm, UpdateSkillForm
from ..utils.file_upload_helper import handle_file_upload
from app.routes.route_utils import load_skill_choices

skill_routes = Blueprint('skill_routes', __name__, url_prefix='')

@skill_routes.route('/interface/add_skill', methods=['GET', 'POST'])
@login_required
def add_skill():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))

    skill_form = AddSkillForm()

    if skill_form.validate_on_submit():
        skill = Skill(name=skill_form.name.data)
        
        # Handle file upload for skill image
        image_filename = handle_file_upload("skills")
        if image_filename:
            skill.image_filename = image_filename

        db.session.add(skill)
        db.session.commit()
        flash('Your skill has been added!', 'success')
        return redirect(url_for('admin_routes.interface'))

    return render_template('admin/interface.html', title='Interface', skill_form=skill_form)


@skill_routes.route('/interface/delete_skill', methods=['POST'])
@login_required
def delete_skill():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))

    form = load_skill_choices(DeleteSkillForm())

    if form.validate_on_submit():
        skill_to_delete = Skill.query.get(form.skill.data)
        if skill_to_delete:
            db.session.delete(skill_to_delete)
            db.session.commit()
            flash('Skill has been deleted!', 'success')
        else:
            flash('Error: Skill not found.', 'danger')
    return redirect(url_for('admin_routes.interface'))

@skill_routes.route('/skills', methods=['GET'])
def skills():
    return render_template('skills/main.html')

@skill_routes.route('/interface/update_skill', methods=['POST'])
@login_required
def update_skill():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))

    skill_form = UpdateSkillForm()

    if skill_form.validate_on_submit():
        skill_to_update = Skill.query.get(skill_form.related_skills.data)
        if skill_to_update:
            skill_to_update.name = skill_form.name.data
            skill_to_update.level = SkillLevel[skill_form.skill_level.data]

            image_filename = handle_file_upload("skills")
            if image_filename:
                skill_to_update.image_filename = image_filename

            db.session.commit()
            flash('Skill has been updated!', 'success')
        else:
            flash('Error: Skill not found.', 'danger')

    flash('Error: Skill not found.', 'danger')
    return redirect(url_for('admin_routes.interface'))
