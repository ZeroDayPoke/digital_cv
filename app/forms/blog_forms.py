#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from . import at_least_one_checkbox, MultiCheckboxField

class AddBlogForm(FlaskForm):
    """
    A form for adding a new blog post.

    Attributes:
    - name (StringField): The name of the blog post.
    - description (TextAreaField): A brief description of the blog post.
    - content_file (StringField): The file path to the content of the blog post.
    - related_skills (MultiCheckboxField): A list of related skills for the blog post.
    - image (FileField): An image for the blog post.
    - submit (SubmitField): A button to submit the form.
    """
    name = StringField('Blog Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    content_file = StringField('Content File')
    related_skills = MultiCheckboxField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_checkbox]
    )
    image = FileField('Skill Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    submit = SubmitField('Submit')

class DeleteBlogForm(FlaskForm):
    """
    A form for deleting a blog post.

    Attributes:
        blog (SelectField): A dropdown menu of available blog posts to delete.
        submit (SubmitField): A button to submit the form and delete the selected blog post.
    """
    blog = SelectField('Blog to Delete', coerce=str)
    submit = SubmitField('Delete Blog')

class UpdateBlogForm(FlaskForm):
    """
    A form used to update a blog post.

    Attributes:
    -----------
    blog : SelectField
        A field to select the blog post to update.
    name : StringField
        A field to update the name of the blog post.
    description : TextAreaField
        A field to update the description of the blog post.
    content_file : StringField
        A field to update the content file of the blog post.
    related_skills : MultiCheckboxField
        A field to select the related skills of the blog post.
    submit : SubmitField
        A field to submit the updated blog post.
    """
    blog = SelectField('Blog to Update', coerce=str)
    name = StringField('Updated Blog Name', validators=[DataRequired()])
    description = TextAreaField('Updated Description')
    content_file = StringField('Content File')
    related_skills = MultiCheckboxField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_checkbox]
    )
    submit = SubmitField('Update Blog')
