#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired
from . import at_least_one_selection, MultiSelectDropdownField
from flask_ckeditor import CKEditorField


class DeleteTutorialForm(FlaskForm):
    tutorial = SelectField('Tutorial to Delete', coerce=str)
    submit = SubmitField('Delete Tutorial')


class TutorialForm(FlaskForm):
    name = StringField('Tutorial Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    content_file = StringField('Content File')
    title = StringField('Title', validators=[DataRequired()])
    content_html = CKEditorField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')
    related_skills = MultiSelectDropdownField(
        'Related Skills',
        choices=[],
    )
