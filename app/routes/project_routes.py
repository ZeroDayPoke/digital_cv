#!/usr/bin/env python3
"""
project_routes.py - project routes for the Flask application
"""
# Path: app/routes/project_routes.py

from flask import Blueprint, redirect, url_for, flash, render_template, jsonify, request
from flask_login import login_required
from ..models import db, Project, Skill, ProjectCategory, ProjectStatus
from ..forms import AddProjectForm, UpdateProjectForm, DeleteProjectForm, SkillsFilterForm, ImageUploadForm
from ..utils.file_upload_helper import handle_file_upload
from app.routes.route_utils import load_skill_choices, load_project_choices, load_category_choices
from app.routes.route_utils.decorators import admin_required
from sqlalchemy.exc import SQLAlchemyError

project_routes = Blueprint('project_routes', __name__, url_prefix='')


@project_routes.route('/interface/add_project', methods=['GET', 'POST'])
@login_required
@admin_required
def add_project():
    form = AddProjectForm()
    form = load_skill_choices(form)
    form = load_category_choices(form)

    if form.validate_on_submit():
        new_project = Project(
            name=form.name.data,
            description=form.description.data,
            role=form.role.data,
            repo_link=form.repo_link.data,
            live_link=form.live_link.data,
            category_id=form.category.data,
            related_skills=Skill.query.filter(Skill.id.in_(form.related_skills.data)).all()
        )

        image_filename = handle_file_upload("projects")
        if image_filename:
            new_project.image_filename = image_filename

        db.session.add(new_project)
        db.session.commit()
        flash('Your project has been added!', 'success')
        return redirect(url_for('admin_routes.interface'))

    return redirect(url_for('admin_routes.interface'))


@project_routes.route('/interface/update_project', methods=['GET', 'POST'])
@login_required
@admin_required
def update_project():
    return redirect(url_for('admin_routes.interface'))


@project_routes.route('/interface/delete_project', methods=['POST'])
@login_required
@admin_required
def delete_project():
    form = DeleteProjectForm()
    form = load_project_choices(form)

    if form.validate_on_submit():
        project_to_delete = Project.query.get(form.project.data)
        if project_to_delete:
            db.session.delete(project_to_delete)
            db.session.commit()
            flash('Project has been deleted!', 'success')
        else:
            flash('Error: Project not found.', 'danger')
    return redirect(url_for('admin_routes.interface'))


@project_routes.route('/project/<project_id>', methods=['GET'])
def project_details(project_id):
    project = Project.query.get_or_404(project_id)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':

        project_data = {
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'role': project.role,
            'repo_link': project.repo_link,
            'live_link': project.live_link,
            'misc_link': project.misc_link,
            'misc_name': project.misc_name,
            'status': project.status,
            'category_id': project.category_id,
            'related_skills': [skill.id for skill in project.related_skills]
        }

        return jsonify(project_data)
    
    return render_template('projects/project_details.html', project=project)


@project_routes.route('/projects', methods=['GET', 'POST'])
def projects():
    form = SkillsFilterForm(request.form)

    if request.method == 'POST' and form.validate():
        selected_skills = form.skills.data
        projects = Project.query.filter(Project.related_skills.any(Skill.id.in_(selected_skills))).all()
    else:
        projects = Project.query.all()

    return render_template('projects/projects.html', projects=projects, form=form)


@project_routes.route('/edit_projects', methods=['GET'])
def edit_projects():
    project_categories = ProjectCategory.query.all()
    projects = Project.query.all()
    projects_by_category = {category.name: [] for category in project_categories}
    projects_by_category['Uncategorized'] = []

    for project in projects:
        form = UpdateProjectForm(obj=project)
        form.project_id.data = project.id
        form.category.data = project.category_id
        form.status.data = project.status.value
        form.related_skills.choices = [(skill.id, skill.name) for skill in Skill.query.all()]
        form.related_skills.data = [str(skill.id) for skill in project.related_skills]  # Set the related skills data

        project_data = {
            "form": form,
            "project_id": project.id,
        }

        category_name = project.category.name if project.category else 'Uncategorized'
        projects_by_category[category_name].append(project_data)

    featured_projects = sorted(
        [project for project in projects if project.is_featured],
        key=lambda x: (x.featured_order is None, x.featured_order)
    )

    return render_template('projects/edit.html', project_forms=projects_by_category, featured_projects=featured_projects)


@project_routes.route('/toggle_featured/<project_id>', methods=['POST'])
@login_required
@admin_required
def toggle_featured(project_id):
    project = Project.query.get(project_id)
    if project:
        try:
            if project.is_featured:
                project.is_featured = False
                project.featured_order = None
            else:
                featured_count = project.query.filter_by(is_featured=True).count()
                if featured_count < 3:
                    project.is_featured = True
                    all_orders = [s.featured_order for s in project.query.filter_by(is_featured=True).all()]
                    all_orders = sorted(filter(None, all_orders))
                    available_order = 1
                    for order in all_orders:
                        if available_order < order:
                            break
                        available_order += 1
                    project.featured_order = available_order
                else:
                    flash('Maximum limit of 3 featured projects reached.', 'warning')
                    return redirect(url_for('project_routes.edit_projects'))

            db.session.commit()
            flash(f"project '{project.name}' featured status toggled to {project.is_featured}, order set to {project.featured_order}.", 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            flash('Database error: ' + str(e), 'danger')
    else:
        flash('project not found', 'danger')

    return redirect(url_for('project_routes.edit_projects'))


@project_routes.route('/edit_project/<project_id>', methods=['POST'])
@login_required
@admin_required
def edit_project(project_id):
    project = Project.query.get(project_id)
    if project:
        form = UpdateProjectForm(request.form)
        if form.validate_on_submit():
            try:
                project.name = form.name.data
                project.description = form.description.data
                project.role = form.role.data
                project.repo_link = form.repo_link.data
                project.live_link = form.live_link.data
                project.status = ProjectStatus(form.status.data)
                project.category_id = form.category.data
                project.is_featured = form.is_featured.data
                project.featured_order = form.featured_order.data if form.is_featured.data else None

                # Update related skills
                skill_ids = form.related_skills.data
                project.related_skills = Skill.query.filter(Skill.id.in_(skill_ids)).all()

                if form.image.data:
                    image_filename = handle_file_upload("projects", form.image.data)
                    if image_filename:
                        project.image_filename = image_filename

                db.session.commit()
                flash('Project updated successfully!', 'success')
            except SQLAlchemyError as e:
                db.session.rollback()
                flash('Database error: ' + str(e), 'danger')
        else:
            flash('Form validation error', 'danger')
    else:
        flash('Project not found', 'danger')

    return redirect(url_for('project_routes.edit_projects'))

@project_routes.route('/upload_project_image/<project_id>', methods=['POST'])
@login_required
@admin_required
def upload_project_image(project_id):
    project = Project.query.get(project_id)
    if not project:
        flash('Project not found', 'danger')
        return redirect(url_for('project_routes.edit_projects'))

    form = ImageUploadForm()

    if form.validate_on_submit():
        image_filename = handle_file_upload("projects")
        if image_filename:
            project.image_filename = image_filename
            db.session.commit()
            flash('Project image updated successfully!', 'success')
        else:
            flash('Error: File not uploaded or not allowed.', 'danger')
    else:
        flash('Error: Form validation failed.', 'danger')

    return redirect(url_for('project_routes.edit_projects'))
