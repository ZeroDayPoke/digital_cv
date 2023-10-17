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
    column_list = ['name', 'image_filename', 'description', 'related_skills']
    form_columns = ['name', 'image_filename', 'description', 'related_skills']

class SkillAdminView(AdminModelView):
    """
    View for managing skills in the admin panel.
    
    Attributes:
    - column_list (list): List of columns to display in the admin panel.
    - form_columns (list): List of columns to display in the add/edit form.
    """
    column_list = ['name', 'image_filename', 'related_projects', 'related_blogs', 'related_tutorials']
    form_columns = ['name', 'image_filename', 'related_projects', 'related_blogs', 'related_tutorials']

class BlogAdminView(AdminModelView):
    """
    View for managing blogs in the admin panel.
    
    Attributes:
    - column_list (list): List of columns to display in the admin panel.
    - form_columns (list): List of columns to display in the add/edit form.
    """
    column_list = ['name', 'image_filename', 'description', 'content_file', 'related_skills']
    form_columns = ['name', 'image_filename', 'description', 'content_file', 'related_skills']

class TutorialAdminView(AdminModelView):
    """
    View for managing tutorials in the admin panel.
    
    Attributes:
    - column_list (list): List of columns to display in the admin panel.
    - form_columns (list): List of columns to display in the add/edit form.
    """
    column_list = ['name', 'description', 'related_skills']
    form_columns = ['name', 'description', 'related_skills']

class EducationAdminView(AdminModelView):
    """
    View for managing education records in the admin panel.
    
    Attributes:
    - column_list (list): List of columns to display in the admin panel.
    - form_columns (list): List of columns to display in the add/edit form.
    """
    column_list = ['institution', 'location', 'field_of_study', 'grad_date', 'details', 'related_skills', 'image_filename']
    form_columns = ['institution', 'location', 'field_of_study', 'grad_date', 'details', 'related_skills', 'image_filename']

class UserAdminView(AdminModelView):
    """
    View for managing users in the admin panel, focused on the 'verified' attribute.
    
    Attributes:
    - column_list (list): List of columns to display in the admin panel.
    - form_columns (list): List of columns to display in the add/edit form.
    """
    column_list = ['username', 'email', 'verified']
    form_columns = ['verified']
