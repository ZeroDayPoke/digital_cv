#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from . import at_least_one_checkbox, MultiCheckboxField

# Skill Forms

class SkillsFilterForm(FlaskForm):
    """
    A form for filtering skills.

    Attributes:
    - skills: A MultiCheckboxField for selecting skills.
    - filter: A SubmitField for submitting the form.
    """
    skills = MultiCheckboxField('Skills', choices=[])
    filter = SubmitField('Filter')

class AddSkillForm(FlaskForm):
    """
    A form to add a new skill to the user's digital CV.

    Attributes:
    - name (StringField): a required field for the name of the skill.
    - image (FileField): an optional field for an image representing the skill.
    - submit (SubmitField): a button to submit the form.
    """
    name = StringField('Skill Name', validators=[DataRequired()])
    image = FileField('Skill Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    submit = SubmitField('Add Skill')

class DeleteSkillForm(FlaskForm):
    """
    A form used to delete a skill from a user's profile.

    Attributes:
    -----------
    related_skills : SelectField
        A dropdown list of skills related to the user's profile.
    submit : SubmitField
        A button to submit the form.
    """
    related_skills = SelectField('Skill to Delete', coerce=str)
    submit = SubmitField('Delete Skill')
