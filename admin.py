# admin.py

from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for
from flask_login import current_user


class AdminModelView(ModelView):
    """
    A view for admin users to manage models.

    This view requires the user to be authenticated and have the 'ADMIN' role.
    If the user is not authenticated, they will be redirected to the login page.
    """

    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role('ADMIN')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth_routes.login'))


class ProjectAdminView(AdminModelView):
    """
    View for managing projects in the admin panel.

    Attributes:
    - column_list (list): List of columns to display in the admin panel.
    - form_columns (list): List of columns to display in the add/edit form.
    """
    column_list = ['name', 'description', 'role', 'repo_link', 'live_link', 'misc_link', 'misc_name',
                   'status', 'collaborators', 'image_filename', 'related_skills', 'created_at', 'updated_at']
    form_columns = ['name', 'description', 'role', 'repo_link', 'live_link', 'misc_link',
                    'misc_name', 'status', 'collaborators', 'image_filename', 'related_skills']

    column_formatters = {
        'collaborators': lambda v, c, m, p: ", ".join([collaborator.username for collaborator in m.collaborators]),
        'related_skills': lambda v, c, m, p: ", ".join([skill.name for skill in m.related_skills]),
    }


class SkillAdminView(AdminModelView):
    """
    View for managing skills in the admin panel.

    Attributes:
    - column_list (list): List of columns to display in the admin panel.
    - form_columns (list): List of columns to display in the add/edit form.
    """

    column_list = ['name', 'level', 'category', 'image_filename', 'created_at', 'updated_at',
                   'related_blogs', 'related_tutorials', 'related_educations', 'related_projects']
    form_columns = ['name', 'level', 'category', 'image_filename',
                    'related_tutorials', 'related_educations', 'related_projects', 'related_blogs']

    column_formatters = {
        'related_projects': lambda v, c, m, p: ", ".join([project.name for project in m.related_projects]),
        'related_blogs': lambda v, c, m, p: ", ".join([blog.name for blog in m.related_blogs]),
        'related_tutorials': lambda v, c, m, p: ", ".join([tutorial.name for tutorial in m.related_tutorials]),
        'related_educations': lambda v, c, m, p: ", ".join([education.institution for education in m.related_educations]),
    }


class BlogAdminView(AdminModelView):
    """
    View for managing blogs in the admin panel.

    Attributes:
    - column_list (list): List of columns to display in the admin panel.
    - form_columns (list): List of columns to display in the add/edit form.
    """
    column_list = ['name', 'description', 'content_file', 'tags',
                   'image_filename', 'related_skills', 'created_at', 'updated_at']
    form_columns = ['name', 'description', 'content_file',
                    'tags', 'image_filename', 'related_skills']
    column_formatters = {
        'related_skills': lambda v, c, m, p: ", ".join([skill.name for skill in m.related_skills]),
    }


class TutorialAdminView(AdminModelView):
    """
    View for managing tutorials in the admin panel.

    Attributes:
    - column_list (list): List of columns to display in the admin panel.
    - form_columns (list): List of columns to display in the add/edit form.
    """
    column_list = ['name', 'description', 'content_file', 'tags',
                   'image_filename', 'related_skills', 'created_at', 'updated_at']
    form_columns = ['name', 'description', 'content_file',
                    'tags', 'image_filename', 'related_skills']
    column_formatters = {
        'related_skills': lambda v, c, m, p: ", ".join([skill.name for skill in m.related_skills]),
    }


class EducationAdminView(AdminModelView):
    """
    View for managing education records in the admin panel.

    Attributes:
    - column_list (list): List of columns to display in the admin panel.
    - form_columns (list): List of columns to display in the add/edit form.
    """
    column_list = ['institution', 'location', 'field_of_study', 'grad_date',
                   'details', 'image_filename', 'related_skills', 'created_at', 'updated_at']
    form_columns = ['institution', 'location', 'field_of_study',
                    'grad_date', 'details', 'image_filename', 'related_skills']
    column_formatters = {
        'related_skills': lambda v, c, m, p: ", ".join([skill.name for skill in m.related_skills]),
    }


class UserAdminView(AdminModelView):
    """
    View for managing users in the admin panel, focused on the 'verified' attribute.

    Attributes:
    - column_list (list): List of columns to display in the admin panel.
    - form_columns (list): List of columns to display in the add/edit form.
    """
    column_list = ['username', 'email', 'verified']
    form_columns = ['verified']


class ExperienceAdminView(AdminModelView):
    column_list = ['company', 'location', 'position', 'start_date', 'end_date', 'is_current',
                   'description', 'experience_type', 'image_filename', 'created_at', 'updated_at']
    form_columns = ['company', 'location', 'position', 'start_date', 'end_date',
                    'is_current', 'description', 'experience_type', 'image_filename']


class MessageAdminView(AdminModelView):
    column_list = ['sender_id', 'message_body',
                   'is_read', 'created_at', 'updated_at']
    form_columns = ['sender_id', 'message_body', 'is_read']


class ProjectCategoryAdminView(AdminModelView):
    """
    View for managing project categories in the admin panel.

    Attributes:
    - column_list (list): List of columns to display in the admin panel.
    - form_columns (list): List of columns to display in the add/edit form.
    """
    column_list = ['name', 'description',
                   'created_at', 'updated_at', 'projects']
    form_columns = ['name', 'description']

    column_formatters = {
        'projects': lambda v, c, m, p: ", ".join([project.name for project in m.projects]),
    }

class PetAdminView(AdminModelView):
    """
    View for managing pets in the admin panel.

    Attributes:
    - column_list (list): List of columns to display in the admin panel.
    - form_columns (list): List of columns to display in the add/edit form.
    """
    column_list = ['name', 'id', 'breed', 'description', 'images', 'is_featured', 'created_at', 'updated_at']
    form_columns = ['name', 'breed', 'description', 'images', 'is_featured']
    
    column_formatters = {
        'images': lambda v, c, m, p: ', '.join([f"{img['filename']} ({img['description']})" for img in m.images]) if m.images else 'No Images'
    }

class AwardAdminView(AdminModelView):
    """
    View for managing awards in the admin panel.

    Attributes:
    - column_list (list): List of columns to display in the admin panel.
    - form_columns (list): List of columns to display in the add/edit form.
    """
    column_list = ['name', 'issuer', 'created_at', 'updated_at']
    form_columns = ['name', 'issuer']
