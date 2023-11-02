#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Optional
from . import at_least_one_checkbox, MultiCheckboxField
from ..routes.route_utils import load_skill_choices, load_category_choices, load_project_choices

# Project Forms

class AddProjectForm(FlaskForm):
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
    related_skills = MultiCheckboxField('Related Skills', choices=[], validators=[at_least_one_checkbox])
    image = FileField('Project Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'svg'])])
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(AddProjectForm, self).__init__(*args, **kwargs)
        self = load_skill_choices(self)
        self = load_category_choices(self)

class UpdateProjectForm(FlaskForm):
    project = SelectField('Project to Update', coerce=str, validators=[DataRequired()])
    name = StringField('Updated Project Name', validators=[DataRequired()])
    description = TextAreaField('Updated Description', validators=[Optional()])
    role = StringField('Updated Role', validators=[Optional()])
    repo_link = StringField('Updated Repository Link', validators=[Optional()])
    live_link = StringField('Updated Live Project Link', validators=[Optional()])
    status = SelectField('Status', coerce=str, choices=[
        ('Planning', 'Planning'), 
        ('In Progress', 'In Progress'), 
        ('Completed', 'Completed'), 
        ('On Hold', 'On Hold')
    ], validators=[DataRequired()])
    category = SelectField('Category', coerce=str, validators=[Optional()])
    related_skills = MultiCheckboxField('Related Skills', choices=[], validators=[at_least_one_checkbox])
    image = FileField('Project Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'svg'])])
    submit = SubmitField('Update Project')

    def __init__(self, *args, **kwargs):
        super(UpdateProjectForm, self).__init__(*args, **kwargs)
        self = load_skill_choices(self)
        self = load_category_choices(self)

class DeleteProjectForm(FlaskForm):
    project = SelectField('Project to Delete', coerce=str, validators=[DataRequired()])
    submit = SubmitField('Delete Project')

    def __init__(self, *args, **kwargs):
        super(DeleteProjectForm, self).__init__(*args, **kwargs)
        self = load_project_choices(self)
