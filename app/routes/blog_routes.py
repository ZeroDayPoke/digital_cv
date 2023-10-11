#!/usr/bin/env python3
"""
blog routes for the Flask application
"""
# Path: app/routes/blog_routes.py

from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import login_required, current_user
from ..models import db, Blog, Skill
from ..forms import AddBlogForm, UpdateBlogForm, DeleteBlogForm

blog_routes = Blueprint('blog_routes', __name__, url_prefix='')


def load_skill_choices(form):
    """
    Populate the choices for skill-related fields in a form.

    Args:
        form (Form): A Flask-WTF form object.

    Returns:
        Form: The updated form object with skill choices loaded.
    """
    form.related_skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]
    return form

def load_blog_choices(form):
    """
    Populate the choices for blog-related fields in a form.

    Args:
        form (Form): A Flask-WTF form object.

    Returns:
        Form: The updated form object with blog choices loaded.
    """
    form.blog.choices = [(str(blog.id), blog.name) for blog in Blog.query.all()]
    return form

@blog_routes.route('/interface/add_blog', methods=['GET', 'POST'])
@login_required
def add_blog():
    """
    Add a new blog.
    
    Initializes the AddBlogForm and populates the choices.
    On successful validation, a new blog entry is created.
    """
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.blogs'))
    
    form = load_skill_choices(AddBlogForm())
    if form.validate_on_submit():
        new_blog = Blog(
            name=form.name.data,
            description=form.description.data,
            content_file=form.content_file.data,
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
    """
    Update an existing blog.

    Initializes the UpdateBlogForm and populates the choices.
    On successful validation, the selected blog entry is updated.
    """
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('blog_routes.blogs'))

    form = load_blog_choices(load_skill_choices(UpdateBlogForm()))
    if form.validate_on_submit():
        blog = Blog.query.get(form.blog.data)
        blog.name = form.name.data
        blog.description = form.description.data
        blog.content_file = form.content_file.data
        blog.related_skills = Skill.query.filter(
            Skill.id.in_(form.related_skills.data)).all()
        db.session.commit()
        flash('Your blog has been updated!', 'success')
        return redirect(url_for('admin_routes.interface'))
    return redirect(url_for('admin_routes.interface'))


@blog_routes.route('/interface/delete_blog', methods=['GET', 'POST'])
@login_required
def delete_blog():
    """
    Delete an existing blog.

    Initializes the DeleteBlogForm and populates the choices.
    On successful validation, the selected blog entry is deleted.
    """
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('blog_routes.blogs'))

    form = load_blog_choices(DeleteBlogForm())

    if form.validate_on_submit():
        blog = Blog.query.get(form.blog.data)
        db.session.delete(blog)
        db.session.commit()
        flash('Your blog has been deleted!', 'success')
        return redirect(url_for('admin_routes.interface'))
    return redirect(url_for('admin_routes.interface'))

@blog_routes.route('/blog/<blog_id>', methods=['GET'])
def blog_detail(blog_id):
    """
    Renders the blog detail page for the specified blog ID.

    Args:
        blog_id (int): The ID of the blog to display.

    Returns:
        str: The rendered HTML for the blog detail page.
    """
    blog = Blog.query.get(blog_id)
    if blog is None:
        flash('Blog not found', 'error')
        return redirect(url_for('main_routes.index'))
    return render_template('blog_detail.html', blog=blog)
