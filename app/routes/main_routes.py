#!/usr/bin/env python3
"""
main.py - main routes for the Flask application
"""
# Path: app/routes/main_routes.py

from flask import render_template, request, Blueprint, current_app, redirect, url_for

from ..models import Project, Skill, Blog
from ..forms import SkillsFilterForm
from app.routes.route_utils import load_skill_choices, load_project_choices, load_blog_choices, load_tutorial_choices

main_routes = Blueprint('main_routes', __name__, url_prefix='')

@main_routes.route('/')
def index():
    return render_template('index.html', include_header=True)

@main_routes.route('/about')
def about():
    return render_template('about.html', title='About')

@main_routes.route('/projects', methods=['GET', 'POST'])
def projects():
    form = SkillsFilterForm(request.form)
    form.skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]

    if request.method == 'POST' and form.validate():
        selected_skills = form.skills.data
        projects = Project.query.filter(Project.related_skills.any(Skill.id.in_(selected_skills))).all()
    else:
        projects = Project.query.all()

    return render_template('projects.html', projects=projects, form=form)

@main_routes.route('/blogs', methods=['GET', 'POST'])
def blogs():
    form = SkillsFilterForm(request.form)
    form.skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]

    if request.method == 'POST' and form.validate():
        selected_skills = form.skills.data
        blogs = Blog.query.filter(Blog.related_skills.any(Skill.id.in_(selected_skills))).all()
    else:
        blogs = Blog.query.all()

    return render_template('blogs.html', blogs=blogs, form=form)

@main_routes.route('/resume')
def resume():
    """
    Render the resume page.
    """
    domain_name = current_app.config.get('DOMAIN_NAME', 'https://zerodaypoke.com')
    pdf_name = current_app.config.get('CV_PDF_NAME', 'dynamic_cv_name.pdf')
    return render_template('resume/main.html', title='Resume', domain_name=domain_name, pdf_name=pdf_name)

@main_routes.route('/exit_admin')
def exit_admin():
    # Perform any additional operations if needed
    return redirect(url_for('main_routes.index'))
