#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, HiddenField, BooleanField
from wtforms.validators import DataRequired, NumberRange, Optional, InputRequired
from . import at_least_one_selection, MultiSelectDropdownField
from ..models import SkillLevel, SkillCategory, Skill
from .form_utils import ImageUploadForm, SliderField


class SkillForm(FlaskForm):
    skill_id = HiddenField('Skill ID')
    name = StringField('Name', validators=[DataRequired()])
    level = SliderField('Level', validators=[
                        NumberRange(min=1, max=3)], default=1)
    category = SelectField('Category', coerce=str,
                           choices=[], validators=[DataRequired()])
    is_featured = BooleanField('Featured')
    featured_order = SelectField('Featured Order', coerce=int, choices=[], validators=[
                                 Optional(), NumberRange(min=1, max=12)])
    submit = SubmitField('Update Skill')

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        self.category.choices = [(choice.value, choice.name)
                                 for choice in SkillCategory]
        self.featured_order.choices = [(i, str(i)) for i in range(1, 13)]


class SkillsFilterForm(FlaskForm):
    """
    A form for filtering skills.
    """
    skills = MultiSelectDropdownField('Skills', choices=[])
    filter = SubmitField('Filt`er')


class AssociateSkillForm(FlaskForm):
    """
    A form for associating a skill with different entities like projects, blogs, etc.
    """
    skill_id = HiddenField('Skill ID')
    entity_type = SelectField('Associate To', choices=[('project', 'Project'), ('blog', 'Blog'), (
        'tutorial', 'Tutorial'), ('education', 'Education')], validators=[DataRequired()])
    entity_instance = SelectField(
        'Instance', coerce=str, validators=[InputRequired()])
    submit = SubmitField('Associate')


class ImageSkillForm(SkillForm, ImageUploadForm):
    submit = SubmitField('Submit Skill')
