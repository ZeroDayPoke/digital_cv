#!/usr/bin/env python3

# ./app/forms/skill_forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.widgets import Input
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from . import at_least_one_checkbox, MultiCheckboxField
from ..models.skill import Skill

# Skill Forms

class RangeInput(Input):
    input_type = 'range'

    def __call__(self, field, **kwargs):
        kwargs.setdefault('step', '1')
        kwargs.setdefault('min', '1')
        kwargs.setdefault('max', '3')
        return super().__call__(field, **kwargs)

class SliderField(IntegerField):
    widget = RangeInput()

class SkillsFilterForm(FlaskForm):
    """
    A form for filtering skills.
    """
    skills = MultiCheckboxField('Skills', choices=[])
    filter = SubmitField('Filter')

class AddSkillForm(FlaskForm):
    """
    A form to add a new skill to the user's digital CV.
    """
    name = StringField('Skill Name', validators=[DataRequired()])
    image = FileField('Skill Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    submit = SubmitField('Add Skill')

class DeleteSkillForm(FlaskForm):
    """
    A form used to delete a skill from a user's profile.
    """
    related_skills = MultiCheckboxField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_checkbox]
    )
    submit = SubmitField('Delete Skill')

class UpdateSkillForm(FlaskForm):
    """
    A form to update an existing skill.
    """
    related_skills = MultiCheckboxField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_checkbox]
    )
    skill_level = SliderField(
        'Skill Level', 
        validators=[DataRequired()]
    )
    image = FileField(
        'Skill Image',
        validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])]
    )
    submit = SubmitField('Update Skill')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.related_skills.choices = [
            (str(skill.id), skill.name) for skill in Skill.query.all()
        ]
