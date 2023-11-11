#!/usr/bin/env python3
"""
blog routes for the Flask application
"""
# Path: app/routes/blog_routes.py

from flask import Blueprint, redirect, url_for, flash, render_template, request
from flask_login import login_required, current_user
from ..models import db, Blog, Skill
from ..forms import AddBlogForm, UpdateBlogForm, DeleteBlogForm, SkillsFilterForm
from ..utils.file_upload_helper import handle_file_upload
from app.routes.route_utils import load_skill_choices, load_blog_choices

blog_routes = Blueprint('blog_routes', __name__, url_prefix='')


@blog_routes.route('/interface/add_blog', methods=['GET', 'POST'])
@login_required
def add_blog():
    """
    Route for adding a new blog post.

    If the current user is not an admin, they will be redirected to the blogs page.
    Otherwise, the user will be presented with a form to add a new blog post.
    If the form is submitted and valid, a new blog post will be created and added to the database.
    If an image is uploaded, it will be saved to the 'blogs' directory.
    """
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('main_routes.blogs'))

    form = load_skill_choices(AddBlogForm())
    
    if form.validate_on_submit():
        new_blog = Blog(
            name=form.name.data,
            description=form.description.data,
            content_file=form.content_file.data,
            related_skills=Skill.query.filter(Skill.id.in_(form.related_skills.data)).all()
        )

        image_filename = handle_file_upload("blogs")
        if image_filename:
            new_blog.image_filename = image_filename

        db.session.add(new_blog)
        db.session.commit()
        flash('Your blog has been added!', 'success')
        return redirect(url_for('admin_routes.interface'))
    return redirect(url_for('admin_routes.interface'))


@blog_routes.route('/interface/update_blog', methods=['GET', 'POST'])
@login_required
def update_blog():
    """
    Route for updating a blog post.

    If the current user is not an admin, they will be redirected to the blogs page.
    Otherwise, the update blog form will be loaded with the current blog's information.
    If the form is submitted and valid, the blog post will be updated in the database.
    If the blog post is not found, an error message will be flashed.
    After the blog post is updated, the user will be redirected to the admin interface page.

    Returns:
        A redirect to the admin interface page.
    """
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('blog_routes.blogs'))

    form = load_blog_choices(load_skill_choices(UpdateBlogForm()))

    if form.validate_on_submit():
        blog_to_update = Blog.query.get(form.blog.data)
        if blog_to_update:
            blog_to_update.name = form.name.data
            blog_to_update.description = form.description.data
            blog_to_update.content_file = form.content_file.data
            blog_to_update.related_skills = Skill.query.filter(Skill.id.in_(form.related_skills.data)).all()

            image_filename = handle_file_upload("blogs")
            if image_filename:
                blog_to_update.image_filename = image_filename

            db.session.commit()
            flash('Your blog has been updated!', 'success')
        else:
            flash('Error: Blog not found.', 'danger')
    return redirect(url_for('admin_routes.interface'))


@blog_routes.route('/interface/delete_blog', methods=['GET', 'POST'])
@login_required
def delete_blog():
    """
    Route for deleting a blog post.

    If the current user is not an admin, they will be redirected to the blogs page.
    Otherwise, a form with a list of available blog posts will be displayed.
    If the form is submitted and valid, the selected blog post will be deleted from the database.
    If the blog post is not found, an error message will be displayed.
    After the blog post is deleted, the user will be redirected to the admin interface page.

    Returns:
        A redirect response to the admin interface page.
    """
    if not current_user.has_role('ADMIN'):
        return redirect(url_for('blog_routes.blogs'))

    form = load_blog_choices(DeleteBlogForm())

    if form.validate_on_submit():
        blog_to_delete = Blog.query.get(form.blog.data)
        if blog_to_delete:
            db.session.delete(blog_to_delete)
            db.session.commit()
            flash('Your blog has been deleted!', 'success')
        else:
            flash('Error: Blog not found.', 'danger')
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

@blog_routes.route('/blogs', methods=['GET', 'POST'])
def blogs():
    form = SkillsFilterForm(request.form)
    form.skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]

    if request.method == 'POST' and form.validate():
        selected_skills = form.skills.data
        blogs = Blog.query.filter(Blog.related_skills.any(Skill.id.in_(selected_skills))).all()
    else:
        blogs = Blog.query.all()

    return render_template('blogs/blogs.html', blogs=blogs, form=form)
