#!/usr/bin/env python3
"""
skill_routes.py - skill routes for the Flask application
"""
# Path: app/routes/skill_routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from ..models import db, Skill, SkillLevel, Project, Blog, Tutorial, Education
from ..forms import AddSkillForm, DeleteSkillForm, UpdateSkillsForm, SkillForm, AssociateSkillForm, ImageUploadForm
from ..utils.file_upload_helper import handle_file_upload, allowed_file
from app.routes.route_utils import load_skill_choices, admin_required
from sqlalchemy.exc import SQLAlchemyError

skill_routes = Blueprint('skill_routes', __name__, url_prefix='')

@skill_routes.route('/interface/add_skill', methods=['GET', 'POST'])
@login_required
@admin_required
def add_skill():
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
@admin_required
def delete_skill():
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


@skill_routes.route('/interface/update_skill', methods=['POST'])
@login_required
@admin_required
def update_skill():
    skill_form = UpdateSkillsForm()

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


@skill_routes.route('/skills', methods=['GET'])
def skills():
    return render_template('skills/main.html')


@skill_routes.route('/edit_skills', methods=['GET'])
@login_required
@admin_required
def edit_skills():
    skills = Skill.query.all()
    skill_forms = {}
    skills_by_category = {}

    for skill in skills:
        form = SkillForm(obj=skill)
        form.level.data = skill.level.value if skill.level else None
        form.category.data = skill.category.name if skill.category else None
        form.skill_id.data = skill.id

        skill_forms[skill.id] = {
            "form": form,
            "association_count": skill.association_count(),
            "skill_id": skill.id
        }

        category = skill.category.name if skill.category else "Uncategorized"
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill_forms[skill.id])

    featured_skills = sorted([skill for skill in skills if skill.is_featured], key=lambda x: (x.featured_order is None, x.featured_order))

    return render_template('skills/edit.html', skill_forms=skills_by_category, featured_skills=featured_skills)


@skill_routes.route('/edit_skill/<skill_id>', methods=['POST'])
@login_required
@admin_required
def edit_skill(skill_id):
    skill = Skill.query.get(skill_id)
    if skill:
        form = SkillForm(request.form)
        if form.validate_on_submit():
            try:
                skill.name = form.name.data
                skill.level = SkillLevel(form.level.data)
                skill.is_featured = form.is_featured.data
                skill.featured_order = form.featured_order.data if form.is_featured.data else None
                skill.category = form.category.data if form.category.data else None

                if form.image.data:
                    image_filename = handle_file_upload("skills", form.image.data)
                    if image_filename:
                        skill.image_filename = image_filename

                db.session.commit()
                flash('Skill updated successfully!', 'success')
            except SQLAlchemyError as e:
                db.session.rollback()
                flash('Database error: ' + str(e), 'danger')
        else:
            flash('Form validation error', 'danger')
    else:
        flash('Skill not found', 'danger')

    return redirect(url_for('skill_routes.edit_skills'))


@skill_routes.route('/toggle_featured/<skill_id>', methods=['POST'])
@login_required
@admin_required
def toggle_featured(skill_id):
    skill = Skill.query.get(skill_id)
    if skill:
        try:
            if skill.is_featured:
                skill.is_featured = False
                skill.featured_order = None
            else:
                featured_count = Skill.query.filter_by(is_featured=True).count()
                if featured_count < 12:
                    skill.is_featured = True
                    all_orders = [s.featured_order for s in Skill.query.filter_by(is_featured=True).all()]
                    all_orders = sorted(filter(None, all_orders))
                    available_order = 1
                    for order in all_orders:
                        if available_order < order:
                            break
                        available_order += 1
                    skill.featured_order = available_order
                else:
                    flash('Maximum limit of 12 featured skills reached.', 'warning')
                    return redirect(url_for('skill_routes.edit_skills'))

            db.session.commit()
            flash(f"Skill '{skill.name}' featured status toggled to {skill.is_featured}, order set to {skill.featured_order}.", 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            flash('Database error: ' + str(e), 'danger')
    else:
        flash('Skill not found', 'danger')

    return redirect(url_for('skill_routes.edit_skills'))


@skill_routes.route('/get_available_entities/<entity_type>/<skill_id>')
@login_required
@admin_required
def get_available_entities(entity_type, skill_id):
    skill = Skill.query.get(skill_id)
    if not skill:
        return jsonify([]), 404

    available_entities = []
    if entity_type == 'project':
        available_projects = [p for p in Project.query.all() if skill not in p.related_skills]
        available_entities = [{'id': p.id, 'name': p.name} for p in available_projects]
    elif entity_type == 'blog':
        available_blogs = [b for b in Blog.query.all() if skill not in b.related_skills]
        available_entities = [{'id': b.id, 'name': b.name} for b in available_blogs]
    elif entity_type == 'tutorial':
        available_tutorials = [t for t in Tutorial.query.all() if skill not in t.related_skills]
        available_entities = [{'id': t.id, 'name': t.name} for t in available_tutorials]
    elif entity_type == 'education':
        available_educations = [e for e in Education.query.all() if skill not in e.related_skills]
        available_entities = [{'id': e.id, 'name': e.name} for e in available_educations]

    return jsonify(available_entities)


@skill_routes.route('/associate_skill/<skill_id>', methods=['POST'])
@login_required
@admin_required
def associate_skill(skill_id):
    skill = Skill.query.get(skill_id)
    if not skill:
        flash('Skill not found', 'danger')
        return redirect(url_for('skill_routes.edit_skills'))

    form = AssociateSkillForm(request.form)

    entity_type = request.form.get('entity_type')
    if entity_type:
        available_entities = get_available_entities(entity_type, skill_id).json
        form.entity_instance.choices = [(entity['id'], entity['name']) for entity in available_entities]

    if form.validate_on_submit():
        entity_type = form.entity_type.data
        entity_id = form.entity_instance.data

        if entity_type and entity_id:
            if entity_type == 'project':
                project = Project.query.get(entity_id)
                if project and skill not in project.related_skills:
                    project.related_skills.append(skill)
            elif entity_type == 'blog':
                blog = Blog.query.get(entity_id)
                if blog and skill not in blog.related_skills:
                    blog.related_skills.append(skill)
            elif entity_type == 'tutorial':
                tutorial = Tutorial.query.get(entity_id)
                if tutorial and skill not in tutorial.related_skills:
                    tutorial.related_skills.append(skill)
            elif entity_type == 'education':
                education = Education.query.get(entity_id)
                if education and skill not in education.related_skills:
                    education.related_skills.append(skill)
            else:
                flash('Invalid entity type', 'danger')
                return redirect(url_for('skill_routes.edit_skills'))

            db.session.commit()
            flash('Skill association updated successfully!', 'success')
        else:
            flash('No association made', 'warning')

    else:
        flash('Form validation error', 'danger')

    return redirect(url_for('skill_routes.edit_skills'))


@skill_routes.route('/upload_skill_image/<skill_id>', methods=['POST'])
@login_required
@admin_required
def upload_skill_image(skill_id):
    skill = Skill.query.get(skill_id)
    if not skill:
        flash('Skill not found', 'danger')
        return redirect(url_for('skill_routes.edit_skills'))

    form = ImageUploadForm()

    if form.validate_on_submit():
        image_filename = handle_file_upload("skills")
        if image_filename:
            skill.image_filename = image_filename
            db.session.commit()
            flash('Skill image updated successfully!', 'success')
        else:
            flash('Error: File not uploaded or not allowed.', 'danger')
    else:
        flash('Error: Form validation failed.', 'danger')

    return redirect(url_for('skill_routes.edit_skills'))
