#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired
from . import at_least_one_checkbox, MultiCheckboxField

# Project Forms
class AddProjectForm(FlaskForm):
    """
    A form to add a new project to the digital CV.

    Attributes:
    -----------
    name : StringField
        The name of the project.
    description : TextAreaField
        A description of the project.
    role : StringField
        The role of the user in the project.
    repo_link : StringField
        The link to the project's repository.
    live_link : StringField
        The link to the live version of the project.
    related_skills : MultiCheckboxField
        The skills related to the project.
    image : FileField
        An image for the project.
    submit : SubmitField
        A button to submit the form.
    """
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
    image = FileField('Project Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    submit = SubmitField('Submit')

class UpdateProjectForm(FlaskForm):
    """
    A form for updating a project in the user's digital CV.

    Attributes:
    -----------
    project : SelectField
        A dropdown menu of the user's existing projects to choose from.
    name : StringField
        A field for the updated name of the project.
    description : TextAreaField
        A field for the updated description of the project.
    role : StringField
        A field for the updated role of the user in the project.
    repo_link : StringField
        A field for the updated repository link of the project.
    live_link : StringField
        A field for the updated live project link of the project.
    related_skills : MultiCheckboxField
        A field for selecting the skills related to the updated project.
    image : FileField
        A field for the updated image of the project.
    submit : SubmitField
        A button to submit the updated project information.
    """
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
    image = FileField('Project Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    submit = SubmitField('Update Project')

class DeleteProjectForm(FlaskForm):
    """
    A form to delete a project from the user's digital CV.

    Attributes:
    -----------
    project : SelectField
        A dropdown menu to select the project to be deleted.
    submit : SubmitField
        A button to submit the form and delete the selected project.
    """
    project = SelectField('Project to Delete', coerce=str)
    submit = SubmitField('Delete Project')
