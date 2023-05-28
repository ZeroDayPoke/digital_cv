#!/usr/bin/env python3
"""Forms for the Flask application"""
# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from wtforms.fields import SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from uuid import UUID

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [str(UUID(x)) for x in valuelist]
        else:
            self.data = []

    def process_data(self, value):
        if value:
            self.data = [str(x) for x in value]
        else:
            self.data = []

def at_least_one_checkbox(form, field):
    if not any(field.data):
        raise ValidationError("At least one checkbox should be checked.")

class ProjectForm(FlaskForm):
    name = StringField('Project Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    role = StringField('Role')
    related_skills = MultiCheckboxField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_checkbox]
    )
    submit = SubmitField('Submit')

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class SigninForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class SkillsFilterForm(FlaskForm):
    skills = MultiCheckboxField('Skills', choices=[])  # Choices will be filled dynamically in the view
    filter = SubmitField('Filter')

class SkillForm(FlaskForm):
    name = StringField('Skill Name', validators=[DataRequired()])
    submit = SubmitField('Add Skill')

class DeleteSkillForm(FlaskForm):
    skill = SelectField('Skill to Delete', coerce=str)
    submit = SubmitField('Delete Skill')

class UpdateProjectForm(FlaskForm):
    project = SelectField('Project to Update', coerce=str)
    name = StringField('Updated Project Name', validators=[DataRequired()])
    description = TextAreaField('Updated Description')
    role = StringField('Updated Role')
    related_skills = MultiCheckboxField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_checkbox]
    )
    submit = SubmitField('Update Project')

class DeleteProjectForm(FlaskForm):
    project = SelectField('Project to Delete', coerce=str)
    submit = SubmitField('Delete Project')
