# admin.py

from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for
from flask_login import current_user

class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role('ADMIN')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth_routes.login'))

class ProjectAdminView(AdminModelView):
    column_list = ['name', 'image_filename', 'description', 'related_skills']
    form_columns = ['name', 'image_filename', 'description', 'related_skills']

class SkillAdminView(AdminModelView):
    column_list = ['name', 'image_filename', 'related_projects', 'related_blogs', 'related_tutorials']
    form_columns = ['name', 'image_filename', 'related_projects', 'related_blogs', 'related_tutorials']

class BlogAdminView(AdminModelView):
    column_list = ['name', 'image_filename', 'description', 'content_file', 'related_skills']
    form_columns = ['name', 'image_filename', 'description', 'content_file', 'related_skills']

class TutorialAdminView(AdminModelView):
    column_list = ['name', 'description', 'related_skills']
    form_columns = ['name', 'description', 'related_skills']
