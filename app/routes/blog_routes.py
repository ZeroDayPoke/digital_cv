#!/usr/bin/env python3
"""
blog routes for the Flask application
"""
# Path: app/routes/blog_routes.py

from flask import Blueprint, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import db, Blog, Skill
from ..forms import BlogForm, UpdateBlogForm, DeleteBlogForm

blog_routes = Blueprint('blog_routes', __name__, url_prefix='')


@blog_routes.route('/interface/add_blog', methods=['GET', 'POST'])
@login_required
def add_blog():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.blogs'))
    form = BlogForm()
    form.related_skills.choices = [
        (str(skill.id), skill.name) for skill in Skill.query.all()]
    if form.validate_on_submit():
        new_blog = Blog(
            name=form.name.data,
            description=form.description.data,
            related_skills=Skill.query.filter(
                Skill.id.in_(form.related_skills.data)).all()
        )
        db.session.add(new_blog)
        db.session.commit()
        flash('Your blog has been added!', 'success')
        return redirect(url_for('admin_routes.interface'))
    return redirect(url_for('admin_routes.interface'))


@blog_routes.route('/interface/update_blog', methods=['GET', 'POST'])
@login_required
def update_blog():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('blog_routes.blogs'))
    form = UpdateBlogForm()
    form.blog.choices = [(str(blog.id), blog.name)
                         for blog in Blog.query.all()]
    form.related_skills.choices = [
        (str(skill.id), skill.name) for skill in Skill.query.all()]
    if form.validate_on_submit():
        blog = Blog.query.get(form.blog.data)
        blog.name = form.name.data
        blog.description = form.description.data
        blog.related_skills = Skill.query.filter(
            Skill.id.in_(form.related_skills.data)).all()
        db.session.commit()
        flash('Your blog has been updated!', 'success')
        return redirect(url_for('admin_routes.interface'))
    return redirect(url_for('admin_routes.interface'))


@blog_routes.route('/interface/delete_blog', methods=['GET', 'POST'])
@login_required
def delete_blog():
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('blog_routes.blogs'))
    form = DeleteBlogForm()
    form.blog.choices = [(str(blog.id), blog.name)
                         for blog in Blog.query.all()]
    if form.validate_on_submit():
        blog = Blog.query.get(form.blog.data)
        db.session.delete(blog)
        db.session.commit()
        flash('Your blog has been deleted!', 'success')
        return redirect(url_for('admin_routes.interface'))
    return redirect(url_for('admin_routes.interface'))
