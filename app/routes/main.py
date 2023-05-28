#!/usr/bin/env python3
"""
main.py - main routes for the Flask application
"""
# app/routes/main.py

from flask import render_template, request, redirect, url_for, flash, Blueprint
from flask_login import login_required
from ..models import db, Project, Skill
from ..forms import ProjectForm

main_routes = Blueprint('main_routes', __name__, url_prefix='')

@main_routes.route('/')
def index():
    return render_template('index.html')


@main_routes.route('/projects')
def projects():
    projects = Project.query.all()
    return render_template('projects.html', projects=projects)

@main_routes.route('/interface', methods=['GET', 'POST'])
# Login Required
def interface():
    form = ProjectForm()
    form.related_skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]
    if form.validate_on_submit():
        new_project = Project(
            name=form.name.data,
            description=form.description.data,
            role=form.role.data,
            related_skills=Skill.query.filter(Skill.id.in_(form.related_skills.data)).all()
        )
        if form.validate_on_submit():
            print(form.related_skills.data)
        db.session.add(new_project)
        db.session.commit()
        flash('Your project has been added!')
        return redirect(url_for('main_routes.projects'))
    else:
        print(form.errors)
    return render_template('interface.html', form=form)
