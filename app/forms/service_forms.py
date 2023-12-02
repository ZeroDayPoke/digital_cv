#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FloatField, BooleanField, SelectField
from wtforms.validators import DataRequired, Optional, NumberRange
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FloatField, BooleanField, SelectField
from wtforms.validators import DataRequired, Optional, NumberRange
from .form_utils import MultiSelectDropdownField, ImageUploadForm
import json

class AddServiceForm(FlaskForm):
    name = StringField('Service Title', validators=[DataRequired()])
    details = TextAreaField('Details', validators=[Optional()])
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

class UpdateServiceForm(AddServiceForm):
    service_id = SelectField('Service', coerce=str, validators=[DataRequired()])
    submit = SubmitField('Update Service')

class DeleteServiceForm(FlaskForm):
    service_id = SelectField('Service to Delete', coerce=str, validators=[DataRequired()])
    submit = SubmitField('Delete Service')
