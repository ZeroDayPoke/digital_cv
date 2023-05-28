#!/usr/bin/env python3
"""Forms for the Flask application"""
# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from wtforms.fields import SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from uuid import UUID

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [str(UUID(x)) for x in valuelist]
        else:
            self.data = []

    def process_data(self, value):
        if value:
            self.data = [str(x) for x in value]
        else:
            self.data = []

def at_least_one_checkbox(form, field):
    if not any(field.data):
        raise ValidationError("At least one checkbox should be checked.")

class ProjectForm(FlaskForm):
    name = StringField('Project Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    role = StringField('Role')
    related_skills = MultiCheckboxField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_checkbox]
    )
    submit = SubmitField('Submit')
