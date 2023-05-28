#!/usr/bin/env python3
"""
main.py - main routes for the Flask application
"""
# app/routes/main.py

from flask import render_template, request, redirect, url_for, flash, Blueprint
from flask_login import login_required, LoginManager, UserMixin, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash
from ..models import db, Project, Skill, User
from ..forms import ProjectForm, SignupForm, SigninForm, SkillsFilterForm, SkillForm, DeleteSkillForm, UpdateProjectForm, DeleteProjectForm

main_routes = Blueprint('main_routes', __name__, url_prefix='')
login_manager = LoginManager()

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/projects', methods=['GET', 'POST'])
def projects():
    form = SkillsFilterForm(request.form)
    form.skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]  # assuming you have a Skill model

    if request.method == 'POST' and form.validate():
        selected_skills = form.skills.data
        projects = Project.query.filter(Project.related_skills.any(Skill.id.in_(selected_skills))).all()
    else:
        projects = Project.query.all()

    return render_template('projects.html', projects=projects, form=form)


@main_routes.route('/interface/delete_skill', methods=['POST'])
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
    return redirect(url_for('main_routes.interface'))

@main_routes.route('/interface/update_project', methods=['GET', 'POST'])
@login_required
def update_project():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))
    form = UpdateProjectForm()
    form.project.choices = [(str(project.id), project.name) for project in Project.query.all()]
    form.related_skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]
    if form.validate_on_submit():
        project_to_update = Project.query.get(form.project.data)
        if project_to_update:
            project_to_update.name = form.name.data
            project_to_update.description = form.description.data
            project_to_update.role = form.role.data
            project_to_update.related_skills = Skill.query.filter(Skill.id.in_(form.related_skills.data)).all()
            db.session.commit()
            flash('Project has been updated!', 'success')
        else:
            flash('Error: Project not found.', 'danger')
    return redirect(url_for('main_routes.interface'))


@main_routes.route('/interface/delete_project', methods=['POST'])
@login_required
def delete_project():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))
    form = DeleteProjectForm()
    form.project.choices = [(str(project.id), project.name) for project in Project.query.all()]
    if form.validate_on_submit():
        project_to_delete = Project.query.get(form.project.data)
        if project_to_delete:
            db.session.delete(project_to_delete)
            db.session.commit()
            flash('Project has been deleted!', 'success')
        else:
            flash('Error: Project not found.', 'danger')
    return redirect(url_for('main_routes.interface'))


@main_routes.route('/interface/add_project', methods=['GET', 'POST'])
@login_required
def add_project():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))
    form = ProjectForm()
    form.related_skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]
    if form.validate_on_submit():
        new_project = Project(
            name=form.name.data,
            description=form.description.data,
            role=form.role.data,
            related_skills=Skill.query.filter(Skill.id.in_(form.related_skills.data)).all()
        )
        db.session.add(new_project)
        db.session.commit()
        flash('Your project has been added!', 'success')
        return redirect(url_for('main_routes.interface'))
    return render_template('interface.html', title='Interface', form=form)

@main_routes.route('/interface/add_skill', methods=['GET', 'POST'])
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
        return redirect(url_for('main_routes.interface'))
    return render_template('interface.html', title='Interface', skill_form=skill_form)


@main_routes.route('/interface', methods=['GET'])
@login_required
def interface():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))
    form = ProjectForm()
    update_project_form = UpdateProjectForm()
    delete_project_form = DeleteProjectForm()
    skill_form = SkillForm()
    delete_skill_form = DeleteSkillForm()
    form.related_skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]
    update_project_form.project.choices = [(str(project.id), project.name) for project in Project.query.all()]
    update_project_form.related_skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]
    delete_project_form.project.choices = [(str(project.id), project.name) for project in Project.query.all()]
    delete_skill_form.skill.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]
    return render_template('interface.html', title='Interface', form=form, update_project_form=update_project_form, delete_project_form=delete_project_form, skill_form=skill_form, delete_skill_form=delete_skill_form)


@main_routes.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main_routes.index'))
    return render_template('signup.html', form=form)

@main_routes.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user)
        flash('Successfully signed in.')
        return redirect(url_for('main_routes.index'))
    return render_template('signin.html', form=form)

@main_routes.route('/signout', methods=['GET'], strict_slashes=False)
@login_required
def signout():
    """Sign out the current user and redirect to the home page"""
    logout_user()
    flash('Successfully logged out.')
    return render_template('index.html')
