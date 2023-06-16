#!/usr/bin/env python3
"""
admin_routes.py - admin routes for the Flask application
"""
# Path: app/routes/admin_routes.py

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from ..models import db, Project, Skill, Blog
from ..forms import AddProjectForm, UpdateProjectForm, DeleteProjectForm, AddSkillForm, DeleteSkillForm
from ..forms import DeleteBlogForm, UpdateBlogForm, AddBlogForm

admin_routes = Blueprint('admin_routes', __name__, url_prefix='')


@admin_routes.route('/interface', methods=['GET'])
@login_required
def interface():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.projects'))
    add_project_form = AddProjectForm()
    update_project_form = UpdateProjectForm()
    delete_project_form = DeleteProjectForm()

    add_skill_form = AddSkillForm()
    delete_skill_form = DeleteSkillForm()

    add_blog_form = AddBlogForm()
    update_blog_form = UpdateBlogForm()
    delete_blog_form = DeleteBlogForm()

    add_blog_form.related_skills.choices = [
        (str(skill.id), skill.name) for skill in Skill.query.all()]
    add_project_form.related_skills.choices = [
        (str(skill.id), skill.name) for skill in Skill.query.all()]
    update_project_form.project.choices = [
        (str(project.id), project.name) for project in Project.query.all()]
    update_project_form.related_skills.choices = [
        (str(skill.id), skill.name) for skill in Skill.query.all()]
    delete_project_form.project.choices = [
        (str(project.id), project.name) for project in Project.query.all()]
    delete_skill_form.skill.choices = [
        (str(skill.id), skill.name) for skill in Skill.query.all()]
    delete_blog_form.blog.choices = [
        (str(blog.id), blog.name) for blog in Blog.query.all()]
    return render_template('interface.html', title='Interface',
                           add_skill_form=add_skill_form,
                           delete_skill_form=delete_skill_form,
                           add_project_form=add_project_form,
                           update_project_form=update_project_form,
                           delete_project_form=delete_project_form,
                           add_blog_form=add_blog_form,
                           update_blog_form=update_blog_form,
                           delete_blog_form=delete_blog_form)
