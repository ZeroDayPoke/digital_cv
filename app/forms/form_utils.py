#!/usr/bin/env python3

from flask_wtf import FlaskForm
from markupsafe import Markup
from wtforms.widgets import html_params, ListWidget
from wtforms.validators import ValidationError, Optional
from wtforms.fields import SelectMultipleField, StringField
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, IntegerField, HiddenField, SelectMultipleField, StringField, SelectField


class BaseFilterForm(FlaskForm):
    name = StringField('Search', validators=[Optional()])
    sort_by = SelectField('Sort By', validators=[Optional()])
    order = SelectField('Order', choices=[('asc', 'Ascending'), ('desc', 'Descending')], validators=[Optional()])

    def set_sort_choices(self, fields):
        """
        Dynamically set the choices for the sort_by field based on provided fields.
        :param fields: A list of field names (str) to include in sort choices.
        """
        self.sort_by.choices = [(field, field.title()) for field in fields]


class MultiSelectDropdownField(SelectMultipleField):
    """
    A custom form field that allows for multiple selections from a dropdown list.

    :param label: The label for the field.
    :param validators: A list of validators to apply to the field.
    :param kwargs: Additional keyword arguments to pass to the parent class.
    """
    widget = ListWidget(prefix_label=False)

    def __init__(self, label=None, validators=None, **kwargs):
        super(MultiSelectDropdownField, self).__init__(
            label, validators, **kwargs)


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
        kwargs['value'] = field.data if field.data is not None else kwargs.pop(
            'default', '1')
        html = '<input %s>' % html_params(**kwargs)
        return Markup(html)


class SliderField(IntegerField):
    """
    A custom form field that renders as a slider input.

    Inherits from `IntegerField` and uses a `RangeInput` widget.
    """
    widget = RangeInput()


class ImageUploadForm(FlaskForm):
    image = FileField('Image', validators=[
                      FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    image_description = StringField('Image Description', default='')
    filepath = StringField('Filepath', default='')
    model = StringField('Model', default='')
    filename = HiddenField('Filename', default='')
    submit = SubmitField('Upload Image')

    def populate_from_image(self, image):
        self.image_description.data = image.description
        self.model = image.owner_type
        self.filename.data = image.filename
        self.filepath = 'images/' + image.owner_type + '/' + image.filename

class ImageFieldManager:
    @staticmethod
    def add_image_field(form):
        """Add a new image field to the form."""
        image_form = ImageUploadForm()
        form.images.append_entry(image_form)

    @staticmethod
    def populate_images(form, images):
        """Populate form with existing images."""
        for image in images:
            image_form = ImageUploadForm()
            image_form.populate_from_image(image)
            form.images.append_entry(image_form)

def setup_range_filter(form, field_name, default_min=0, default_max=999999999):
    """
    Sets up range filters for the given field in the form.

    Args:
        form: The form instance containing the fields.
        field_name (str): The base name of the range filter field.
        default_min: The default minimum value.
        default_max: The default maximum value.

    Returns:
        tuple: A tuple containing the min and max values for the range filter.
    """
    min_field = getattr(form, f"{field_name}_min", None)
    max_field = getattr(form, f"{field_name}_max", None)

    min_val = min_field.data if min_field and min_field.data is not None else default_min
    max_val = max_field.data if max_field and max_field.data is not None else default_max

    return (min_val, max_val)
