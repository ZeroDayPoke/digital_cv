#!/usr/bin/env python3

from app.models import Skill, Project, Blog, Tutorial, ProjectCategory

def load_skill_choices(form):
    """
    Populate the choices for skill-related fields in a form.

    Args:
        form (Form): A Flask-WTF form object.

    Returns:
        Form: The updated form object with skill choices loaded.
    """
    form.related_skills.choices = [(skill.id, skill.name) for skill in Skill.query.all()]
    return form


def load_project_choices(form):
    """
    Populate the choices for project-related fields in a form.
    
    Args:
        form (Form): A Flask-WTF form object.
        
    Returns:
        Form: The updated form object with project choices loaded.
    """
    form.project.choices = [(str(project.id), project.name) for project in Project.query.all()]
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

def load_tutorial_choices(form):
    """
    Populate the choices for tutorial-related fields in a form.
    
    Args:
        form (Form): A Flask-WTF form object.
        
    Returns:
        Form: The updated form object with tutorial choices loaded.
    """
    form.tutorial.choices = [(str(tutorial.id), tutorial.name) for tutorial in Tutorial.query.all()]
    return form

def load_category_choices(form):
    """
    Populate the choices for project category fields in a form.

    Args:
        form (FlaskForm): A Flask-WTF form object.

    Returns:
        FlaskForm: The updated form object with category choices loaded.
    """
    form.category.choices = [(str(category.id), category.name) for category in ProjectCategory.query.all()]
    return form
