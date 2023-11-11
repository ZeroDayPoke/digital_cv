#!/usr/bin/env python3

from flask_wtf import FlaskForm
from markupsafe import Markup
from wtforms.widgets import html_params, ListWidget, Select
from wtforms.validators import ValidationError
from wtforms.fields import SelectMultipleField
from flask_wtf.file import FileField, FileAllowed
from uuid import UUID
from wtforms import SubmitField, IntegerField, HiddenField, SelectMultipleField

class MultiSelectDropdownField(SelectMultipleField):
    """
    A custom form field that allows multiple selections from a dropdown.

    :param SelectMultipleField: The base class for the field.
    :type SelectMultipleField: class
    """
    widget = ListWidget(prefix_label=False)

    def __init__(self, label=None, validators=None, **kwargs):
        super(MultiSelectDropdownField, self).__init__(label, validators, **kwargs)

def at_least_one_selection(form, field):
    """
    Validates that at least one option is selected in a multi-select dropdown.

    Args:
        form: The form object.
        field: The field to be validated.

    Raises:
        ValidationError: If no option is selected.
    """
    if not field.data or len(field.data) == 0:
        raise ValidationError("At least one option must be selected.")

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
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    submit = SubmitField('Upload Image')
