from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, HiddenField, FieldList, FormField, BooleanField, SelectMultipleField
from wtforms.widgets import Input
from wtforms.validators import DataRequired, NumberRange, Optional, InputRequired
from flask_wtf.file import FileField, FileAllowed
from . import at_least_one_checkbox, MultiCheckboxField
from ..models import SkillLevel, SkillCategory, db, Skill
from wtforms.widgets import html_params
from wtforms_alchemy import model_form_factory
from markupsafe import Markup

BaseModelForm = model_form_factory(FlaskForm)

class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

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
    level = SelectField('Skill Level',
                        choices=[(level.name, level.value) for level in SkillLevel],
                        validators=[DataRequired()])
    category = SelectField('Skill Category',
                           choices=[(category.name, category.value) for category in SkillCategory],
                           validators=[DataRequired()])
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

class RangeInput:
    """
    Custom widget for rendering a range input.
    """
    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('name', field.name)
        kwargs.setdefault('type', 'range')
        kwargs.setdefault('step', '1')
        kwargs.setdefault('min', '1')
        kwargs.setdefault('max', '3')
        kwargs['value'] = field.data if field.data is not None else kwargs.pop('default', '1')
        html = '<input %s>' % html_params(**kwargs)
        return Markup(html)

class SliderField(IntegerField):
    widget = RangeInput()

class ImageUploadForm(FlaskForm):
    image_filename = HiddenField('Image Filename')
    image = FileField('Skill Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    submit = SubmitField('Upload Image')

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

class UpdateSkillsForm(FlaskForm):
    skills = FieldList(FormField(SkillForm), min_entries=1)
    submit = SubmitField('Update Skills')

    def populate_skills(self, skills):
        while len(self.skills) > 0:
            self.skills.pop_entry()
        
        for skill in skills:
            skill_form_data = {
                'skill_id': skill.id,
                'name': skill.name,
                'level': skill.level.value if skill.level else 1,
                'is_featured': skill.is_featured,
                'featured_order': skill.featured_order if skill.is_featured else None,
                'category': skill.category.name if skill.category else None,
            }
            self.skills.append_entry(skill_form_data)
