#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from . import at_least_one_selection, MultiSelectDropdownField

class AddTutorialForm(FlaskForm):
    """
    A form to add a new tutorial to the database.

    Attributes:
    - name (StringField): The name of the tutorial.
    - description (TextAreaField): The description of the tutorial.
    - content_file (StringField): The file containing the tutorial content.
    - related_skills (MultiSelectDropdownField): The skills related to the tutorial.
    - image (FileField): An image for the tutorial.
    - submit (SubmitField): The button to submit the form.
    """
    name = StringField('Tutorial Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    content_file = StringField('Content File')
    related_skills = MultiSelectDropdownField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_selection]
    )
    image = FileField('Skill Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    submit = SubmitField('Submit')

class DeleteTutorialForm(FlaskForm):
    """
    A form to delete a tutorial from the database.

    Attributes:
    -----------
    tutorial : SelectField
        A dropdown list of available tutorials to delete.
    submit : SubmitField
        A button to submit the form and delete the selected tutorial.
    """
    tutorial = SelectField('Tutorial to Delete', coerce=str)
    submit = SubmitField('Delete Tutorial')

class UpdateTutorialForm(FlaskForm):
    """
    A form to update a tutorial.

    Attributes:
    -----------
    tutorial : SelectField
        A dropdown list of tutorials to choose from.
    name : StringField
        A field to enter the updated tutorial name.
    description : TextAreaField
        A field to enter the updated tutorial description.
    content_file : StringField
        A field to enter the content file.
    related_skills : MultiSelectDropdownField
        A list of related skills to choose from.
    submit : SubmitField
        A button to submit the form.
    """
    tutorial = SelectField('Tutorial to Update', coerce=str)
    name = StringField('Updated Tutorial Name', validators=[DataRequired()])
    description = TextAreaField('Updated Description')
    content_file = StringField('Content File')
    related_skills = MultiSelectDropdownField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_selection]
    )
    submit = SubmitField('Update Tutorial')
