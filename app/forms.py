#!/usr/bin/env python3
"""Forms for the Flask application"""
# app/forms.py

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, SelectField, FileField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from wtforms.fields import SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from uuid import UUID


# Custom form fields
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


# Auth Forms
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


# Project Forms
class AddProjectForm(FlaskForm):
    name = StringField('Project Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    role = StringField('Role')
    repo_link = StringField('Repository Link')
    live_link = StringField('Live Project Link')
    related_skills = MultiCheckboxField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_checkbox]
    )
    submit = SubmitField('Submit')

class UpdateProjectForm(FlaskForm):
    project = SelectField('Project to Update', coerce=str)
    name = StringField('Updated Project Name', validators=[DataRequired()])
    description = TextAreaField('Updated Description')
    role = StringField('Updated Role')
    repo_link = StringField('Updated Repository Link')
    live_link = StringField('Updated Live Project Link')
    related_skills = MultiCheckboxField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_checkbox]
    )
    submit = SubmitField('Update Project')

class DeleteProjectForm(FlaskForm):
    project = SelectField('Project to Delete', coerce=str)
    submit = SubmitField('Delete Project')


# Skill Forms
class SkillsFilterForm(FlaskForm):
    skills = MultiCheckboxField('Skills', choices=[])
    filter = SubmitField('Filter')

class AddSkillForm(FlaskForm):
    name = StringField('Skill Name', validators=[DataRequired()])
    image = FileField('Skill Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    submit = SubmitField('Add Skill')

class DeleteSkillForm(FlaskForm):
    related_skills = SelectField('Skill to Delete', coerce=str)
    submit = SubmitField('Delete Skill')


# Blog forms
class AddBlogForm(FlaskForm):
    name = StringField('Blog Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    content_file = StringField('Content File')
    related_skills = MultiCheckboxField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_checkbox]
    )
    submit = SubmitField('Submit')

class DeleteBlogForm(FlaskForm):
    blog = SelectField('Blog to Delete', coerce=str)
    submit = SubmitField('Delete Blog')

class UpdateBlogForm(FlaskForm):
    blog = SelectField('Blog to Update', coerce=str)
    name = StringField('Updated Blog Name', validators=[DataRequired()])
    description = TextAreaField('Updated Description')
    content_file = StringField('Content File')
    related_skills = MultiCheckboxField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_checkbox]
    )
    submit = SubmitField('Update Blog')

class AddTutorialForm(FlaskForm):
    name = StringField('Tutorial Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    content_file = StringField('Content File')
    related_skills = MultiCheckboxField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_checkbox]
    )
    submit = SubmitField('Submit')

class DeleteTutorialForm(FlaskForm):
    tutorial = SelectField('Tutorial to Delete', coerce=str)
    submit = SubmitField('Delete Tutorial')

class UpdateTutorialForm(FlaskForm):
    tutorial = SelectField('Tutorial to Update', coerce=str)
    name = StringField('Updated Tutorial Name', validators=[DataRequired()])
    description = TextAreaField('Updated Description')
    content_file = StringField('Content File')
    related_skills = MultiCheckboxField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_checkbox]
    )
    submit = SubmitField('Update Tutorial')
