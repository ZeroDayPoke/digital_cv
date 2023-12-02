#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, BooleanField, ValidationError, HiddenField, SelectMultipleField
from wtforms.validators import DataRequired, Optional, NumberRange
from ..models import Project, ProjectCategory, ProjectStatus, Skill
from ..routes.route_utils import load_skill_choices, load_category_choices, load_project_choices
from .form_utils import ImageUploadForm


class BaseProjectForm(FlaskForm):
    name = StringField('Project Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    role = StringField('Role', validators=[Optional()])
    repo_link = StringField('Repository Link', validators=[Optional()])
    live_link = StringField('Live Project Link', validators=[Optional()])
    status = SelectField('Status', coerce=str, choices=[
        ('Planning', 'Planning'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('On Hold', 'On Hold')
    ], validators=[DataRequired()])
    category = SelectField('Category', coerce=str, validators=[Optional()])
    related_skills = SelectMultipleField(
        'Related Skills', choices=[], coerce=str)
    is_featured = BooleanField('Featured')
    featured_order = SelectField('Featured Order', coerce=int, validators=[
                                 Optional(), NumberRange(min=1, max=12)])

    def __init__(self, *args, **kwargs):
        super(BaseProjectForm, self).__init__(*args, **kwargs)
        self.featured_order.choices = [(i, str(i)) for i in range(1, 13)]
        self = load_skill_choices(self)
        self = load_category_choices(self)

    def validate_is_featured(self, field):
        if field.data:
            featured_count = Project.query.filter_by(is_featured=True).count()
            if featured_count >= 3:
                raise ValidationError(
                    'Only 3 projects can be featured at a time.')


class AddProjectForm(BaseProjectForm, ImageUploadForm):
    submit = SubmitField('Submit')


class UpdateProjectForm(BaseProjectForm, ImageUploadForm):
    project_id = HiddenField('Project ID')
    submit = SubmitField('Update Project')

    def __init__(self, *args, **kwargs):
        super(UpdateProjectForm, self).__init__(*args, **kwargs)
        self.category.choices = [(category.id, category.name)
                                 for category in ProjectCategory.query.all()]
        self.featured_order.choices = [(i, str(i)) for i in range(1, 4)]
        self.status.choices = [(status.value, status.name)
                               for status in ProjectStatus]
        self.related_skills.choices = [
            (skill.id, skill.name) for skill in Skill.query.all()]

    def validate_is_featured(self, field):
        super(UpdateProjectForm, self).validate_is_featured(field)
        if field.data:
            current_project = Project.query.get(self.project_id.data)
            featured_count = Project.query.filter_by(is_featured=True).count()
            if current_project and current_project.is_featured:
                featured_count -= 1

            if featured_count >= 3:
                raise ValidationError(
                    'Only 3 projects can be featured at a time.')


class DeleteProjectForm(FlaskForm):
    project = SelectField('Project to Delete', coerce=str,
                          validators=[DataRequired()])
    submit = SubmitField('Delete Project')

    def __init__(self, *args, **kwargs):
        super(DeleteProjectForm, self).__init__(*args, **kwargs)
        self = load_project_choices(self)
