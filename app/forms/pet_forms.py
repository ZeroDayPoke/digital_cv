#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, HiddenField
from wtforms.fields import FieldList, FormField
from wtforms.validators import DataRequired
from .form_utils import ImageUploadForm, ImageFieldManager


class PetForm(FlaskForm):
    pet_id = HiddenField('Pet ID')
    name = StringField('Name', validators=[DataRequired()])
    breed = StringField('Breed', validators=[DataRequired()])
    description = TextAreaField('Description')
    images = FieldList(FormField(ImageUploadForm), min_entries=0)
    is_featured = BooleanField('Featured')
    submit = SubmitField('Update Pet')

    def add_image_field(self):
        ImageFieldManager.add_image_field(self)

    def populate_images(self, images):
        ImageFieldManager.populate_images(self, images)
