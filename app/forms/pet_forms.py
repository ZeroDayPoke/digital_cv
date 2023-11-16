#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, HiddenField
from wtforms.fields import FieldList, FormField
from wtforms.validators import DataRequired
from .form_utils import ImageUploadForm


class PetImageForm(FlaskForm):
    """
    A sub-form for handling each pet image and its description.
    """
    filename = StringField('Image Filename', validators=[DataRequired()])
    img_description = StringField('Image Description')


class PetForm(FlaskForm):
    pet_id = HiddenField('Pet ID')
    name = StringField('Name', validators=[DataRequired()])
    breed = StringField('Breed', validators=[DataRequired()])
    description = TextAreaField('Description')
    images = FieldList(FormField(PetImageForm), min_entries=1)
    is_featured = BooleanField('Featured')
    submit = SubmitField('Update Pet')


class ImagePetForm(PetForm, ImageUploadForm):
    submit = SubmitField('Submit Pet')
