#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, HiddenField, BooleanField
from wtforms.validators import DataRequired, NumberRange, Optional, InputRequired
from . import at_least_one_selection, MultiSelectDropdownField
from ..models import SkillLevel, SkillCategory, db, Skill
from wtforms_alchemy import model_form_factory
from .form_utils import ImageUploadForm, SliderField

class BaseSkillForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    category = SelectField('Skill Category', coerce=str, validators=[DataRequired()])
    is_featured = BooleanField('Featured')
    featured_order = SelectField('Featured Order', coerce=int, validators=[Optional(), NumberRange(min=1, max=12)])
    
    def __init__(self, *args, **kwargs):
        super(BaseSkillForm, self).__init__(*args, **kwargs)
        self.category.choices = [(category.name, category.value) for category in SkillCategory]

BaseModelForm = model_form_factory(FlaskForm)

class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

class SkillsFilterForm(FlaskForm):
    """
    A form for filtering skills.
    """
    skills = MultiSelectDropdownField('Skills', choices=[])
    filter = SubmitField('Filter')

class AddSkillForm(BaseSkillForm, ImageUploadForm):
    level = SliderField('Skill Level', validators=[NumberRange(min=1, max=3)], default=1)
    submit = SubmitField('Add Skill')

    def __init__(self, *args, **kwargs):
        super(AddSkillForm, self).__init__(*args, **kwargs)
        self.level.choices = [(level.value, level.name) for level in SkillLevel]

class DeleteSkillForm(FlaskForm):
    related_skills = MultiSelectDropdownField('Related Skills', validators=[at_least_one_selection])
    submit = SubmitField('Delete Skill')

    def __init__(self, *args, **kwargs):
        super(DeleteSkillForm, self).__init__(*args, **kwargs)
        self.related_skills.choices = [(str(skill.id), skill.name) for skill in Skill.query.all()]

class SkillForm(ImageUploadForm):
    skill_id = HiddenField('Skill ID')
    name = StringField('Name', validators=[DataRequired()])
    level = SliderField('Level', validators=[NumberRange(min=1, max=3)], default=1)
    category = SelectField('Category', coerce=str, choices=[], validators=[DataRequired()])
    is_featured = BooleanField('Featured')
    featured_order = SelectField('Featured Order', coerce=int, choices=[], validators=[Optional(), NumberRange(min=1, max=12)])
    submit = SubmitField('Update Skill')

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        self.level.choices = [(choice.value, choice.name) for choice in SkillLevel]
        self.category.choices = [(choice.value, choice.name) for choice in SkillCategory]
        self.featured_order.choices = [(i, str(i)) for i in range(1, 13)]

class AssociateSkillForm(FlaskForm):
    """
    A form for associating a skill with different entities like projects, blogs, etc.
    """
    skill_id = HiddenField('Skill ID')
    entity_type = SelectField('Associate To', choices=[('project', 'Project'), ('blog', 'Blog'), ('tutorial', 'Tutorial'), ('education', 'Education')], validators=[DataRequired()])
    entity_instance = SelectField('Instance', coerce=str, validators=[InputRequired()])
    submit = SubmitField('Associate')

class UpdateSkillForm(BaseSkillForm, ImageUploadForm):
    skill_id = HiddenField('Skill ID')
    level = SliderField('Level', validators=[NumberRange(min=1, max=3)], default=1)
    submit = SubmitField('Update Skill')

    def __init__(self, *args, **kwargs):
        super(UpdateSkillForm, self).__init__(*args, **kwargs)
        self.level.choices = [(choice.value, choice.name) for choice in SkillLevel]
        self.category.choices = [(choice.value, choice.name) for choice in SkillCategory]
        self.featured_order.choices = [(i, str(i)) for i in range(1, 13)]
