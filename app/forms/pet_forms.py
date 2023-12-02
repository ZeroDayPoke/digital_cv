#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, HiddenField
from wtforms.fields import FieldList, FormField
from wtforms.validators import DataRequired
from .form_utils import ImageUploadForm


class PetForm(FlaskForm):
    pet_id = HiddenField('Pet ID')
    name = StringField('Name', validators=[DataRequired()])
    breed = StringField('Breed', validators=[DataRequired()])
    description = TextAreaField('Description')
    images = FieldList(FormField(ImageUploadForm), min_entries=0)
    is_featured = BooleanField('Featured')
    submit = SubmitField('Update Pet')

    def add_image_field(self):
        """Add a new image field to the form."""
        image_form = ImageUploadForm()
        self.images.append_entry(image_form)

    def populate_images(self, images):
        for image in images:
            image_form = ImageUploadForm()
            image_form.populate_from_image(image)
            self.images.append_entry(image_form)
