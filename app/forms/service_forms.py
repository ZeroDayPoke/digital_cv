# app/forms/service_forms.py

import json
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField, TextAreaField, SubmitField, FieldList, FormField
from wtforms.validators import Optional, NumberRange, DataRequired
from .form_utils import BaseFilterForm, ImageUploadForm, ImageFieldManager
from ..models.service import Service
from ..models import db

class AddServiceForm(FlaskForm):
    name = StringField('Service Title', validators=[DataRequired()])
    details = TextAreaField('Details', validators=[Optional()])
    images = FieldList(FormField(ImageUploadForm), min_entries=0)
    price = FloatField('Price', validators=[NumberRange(min=0)])
    currency = StringField('Currency', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    duration = StringField('Duration', validators=[Optional()])
    is_available = BooleanField('Is Available')
    target_audiences = TextAreaField('Target Audiences', validators=[Optional()])
    promo = TextAreaField('Promotional Details', validators=[Optional()])
    note = TextAreaField('Additional Notes', validators=[Optional()])
    early_eligible = BooleanField('Early Eligible')
    experimental = BooleanField('Experimental')
    submit = SubmitField('Add Service')

    def parse_json_fields(self):
        """Parse fields that are expected to be JSON in the model."""
        try:
            if self.details.data:
                self.details.data = json.loads(self.details.data)
            if self.target_audiences.data:
                self.target_audiences.data = json.loads(self.target_audiences.data)
            if self.promo.data:
                self.promo.data = json.loads(self.promo.data)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in one of the fields.")

    def add_image_field(self):
        ImageFieldManager.add_image_field(self)

    def populate_images(self, images):
        ImageFieldManager.populate_images(self, images)

class UpdateServiceForm(AddServiceForm):
    service_id = SelectField('Service', coerce=str, validators=[DataRequired()])
    submit = SubmitField('Update Service')

class DeleteServiceForm(FlaskForm):
    service_id = SelectField('Service to Delete', coerce=str, validators=[DataRequired()])
    submit = SubmitField('Delete Service')


class ServiceFilterForm(BaseFilterForm):
    def __init__(self, *args, **kwargs):
        super(ServiceFilterForm, self).__init__(*args, **kwargs)

        field_type_map = {
            'String': StringField,
            'Float': FloatField,
            'Boolean': BooleanField
        }

        for column in Service.__table__.columns:
            field_type = type(column.type).__name__
            if field_type in ['JSON', 'DateTime']:
                continue

            form_field_type = field_type_map.get(field_type)
            if form_field_type:
                field_instance = FormField(form_field_type(column.name, validators=[Optional()]))
                setattr(self, column.name, field_instance)


def create_dynamic_service_form(excluded_fields=None):
    class DynamicServiceForm(BaseFilterForm):
        pass

    if excluded_fields is None:
        excluded_fields = []

    field_type_map = {
        'String': StringField,
        'Float': FloatField,
        'Boolean': BooleanField
    }

    excluded_fields += ['id', 'created_at', 'updated_at', 'image_filename', 'image_filename_two', 'image_filename_three', 'image_filename_four']
    select_fields = ['category', 'currency', 'duration']
    range_fields = ['price']

    for column in Service.__table__.columns:
        if column.name in excluded_fields:
            continue

        if column.name in select_fields:
            distinct_values = db.session.query(getattr(Service, column.name)).distinct().all()
            choices = [('', 'All')] + [(value[0], value[0]) for value in distinct_values if value[0]]
            setattr(DynamicServiceForm, column.name, SelectField(column.name, choices=choices, validators=[Optional()]))
        elif column.name in range_fields:
            setattr(DynamicServiceForm, f"{column.name}_min", FloatField(f"{column.name.capitalize()} Min", validators=[Optional()]))
            setattr(DynamicServiceForm, f"{column.name}_max", FloatField(f"{column.name.capitalize()} Max", validators=[Optional()]))
        else:
            field_type = type(column.type).__name__
            if field_type in ['JSON', 'DateTime']:
                continue
            form_field_type = field_type_map.get(field_type)
            if form_field_type:
                setattr(DynamicServiceForm, column.name, form_field_type(column.name, validators=[Optional()]))

    return DynamicServiceForm
