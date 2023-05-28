#!/usr/bin/env python3
"""
skill_routes.py - skill routes for the Flask application
"""
# Path: app/routes/skill_routes.py

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import db, Skill
from ..forms import SkillForm, DeleteSkillForm

skill_routes = Blueprint('skill_routes', __name__, url_prefix='')

@skill_routes.route('/interface/add_skill', methods=['GET', 'POST'])
@login_required
def add_skill():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))
    skill_form = SkillForm()
    if skill_form.validate_on_submit():
        skill = Skill(name=skill_form.name.data)
        db.session.add(skill)
        db.session.commit()
        flash('Your skill has been added!', 'success')
        return redirect(url_for('admin_routes.interface'))
    return render_template('interface.html', title='Interface', skill_form=skill_form)

@skill_routes.route('/interface/delete_skill', methods=['POST'])
@login_required
def delete_skill():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))
    form = DeleteSkillForm()
    form.skill.choices = [(skill.id, skill.name) for skill in Skill.query.all()]
    if form.validate_on_submit():
        skill_to_delete = Skill.query.get(form.skill.data)
        if skill_to_delete:
            db.session.delete(skill_to_delete)
            db.session.commit()
            flash('Skill has been deleted!', 'success')
        else:
            flash('Error: Skill not found.', 'danger')
    return redirect(url_for('admin_routes.interface'))
