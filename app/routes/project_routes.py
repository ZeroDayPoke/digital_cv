#!/usr/bin/env python3
"""
project_routes.py - project routes for the Flask application
"""
# Path: app/routes/project_routes.py

from flask import Blueprint, redirect, url_for, flash, render_template, request
from flask_login import login_required, current_user
from ..models import db, Project, Skill
from ..forms import AddProjectForm, UpdateProjectForm, DeleteProjectForm
from ..utils.file_upload_helper import handle_file_upload
from app.routes.route_utils import load_skill_choices, load_project_choices

project_routes = Blueprint('project_routes', __name__, url_prefix='')


@project_routes.route('/interface/add_project', methods=['GET', 'POST'])
@login_required
def add_project():
    """
    Route for adding a new project to the database.

    If the current user is not an admin, they will be redirected to the projects page.
    Otherwise, the user will be presented with a form to add a new project.
    If the form is submitted and valid, a new project will be created and added to the database.
    If an image is uploaded, it will be saved and associated with the new project.
    Finally, the user will be redirected to the admin interface page.
    """
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))

    form = load_skill_choices(AddProjectForm())

    if form.validate_on_submit():
        new_project = Project(
            name=form.name.data,
            description=form.description.data,
            role=form.role.data,
            live_link=form.live_link.data,
            repo_link=form.repo_link.data,
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
def update_project():
    """
    Route for updating a project. Only accessible by users with the 'ADMIN' role.
    On GET request, loads the UpdateProjectForm with project and skill choices.
    On POST request, updates the project with the form data and commits the changes to the database.
    If the project is not found, flashes an error message.
    Redirects to the admin interface page after completion.
    """
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))

    form = load_project_choices(load_skill_choices(UpdateProjectForm()))
    
    if form.validate_on_submit():
        project_to_update = Project.query.get(form.project.data)
        if project_to_update:
            project_to_update.name = form.name.data
            project_to_update.description = form.description.data
            project_to_update.role = form.role.data
            project_to_update.live_link = form.live_link.data
            project_to_update.repo_link = form.repo_link.data
            project_to_update.related_skills = Skill.query.filter(Skill.id.in_(form.related_skills.data)).all()

            image_filename = handle_file_upload("projects")
            if image_filename:
                project_to_update.image_filename = image_filename

            db.session.commit()
            flash('Project has been updated!', 'success')
        else:
            flash('Error: Project not found.', 'danger')
    return redirect(url_for('admin_routes.interface'))


@project_routes.route('/interface/delete_project', methods=['POST'])
@login_required
def delete_project():
    """
    Route for deleting a project from the database.

    Only users with the 'ADMIN' role can access this route.

    Returns:
        Redirect to the admin interface page.
    """
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))

    form = load_project_choices(DeleteProjectForm())

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
    """
    Display the details of an individual project.

    Args:
        project_id (str): The ID of the project to display.

    Returns:
        Rendered template for project details.
    """
    # Query the database for the project with the given ID
    project = Project.query.get_or_404(project_id)

    # Render the 'project_detail.html' template, passing in the project
    return render_template('project_details.html', project=project)
