#!/usr/bin/env python3
"""
main.py - main routes for the Flask application
"""
# Path: app/routes/main_routes.py

from flask import render_template, request, Blueprint

from ..models import Project, Skill
from ..forms import SkillsFilterForm

main_routes = Blueprint('main_routes', __name__, url_prefix='')

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
