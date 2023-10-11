#!/usr/bin/env python3
"""Forms for the Flask application"""
# app/forms.py

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, SelectField, FileField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from wtforms.fields import SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from uuid import UUID


# Custom form fields
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


# Auth Forms
class SignupForm(FlaskForm):
    """
    A form for user sign up.

    Attributes:
    - username (StringField): a field for the user's desired username.
    - email (StringField): a field for the user's email address.
    - password (PasswordField): a field for the user's desired password.
    - confirm_password (PasswordField): a field for the user to confirm their password.
    - submit (SubmitField): a button to submit the form.
    """
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class SigninForm(FlaskForm):
    """
    A form for user sign in.

    Attributes:
    - email (StringField): an input field for user email
    - password (PasswordField): an input field for user password
    - submit (SubmitField): a button to submit the form
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


# Project Forms
class AddProjectForm(FlaskForm):
    """
    A form to add a new project to the digital CV.

    Attributes:
    -----------
    name : StringField
        The name of the project.
    description : TextAreaField
        A description of the project.
    role : StringField
        The role of the user in the project.
    repo_link : StringField
        The link to the project's repository.
    live_link : StringField
        The link to the live version of the project.
    related_skills : MultiCheckboxField
        The skills related to the project.
    submit : SubmitField
        A button to submit the form.
    """
    name = StringField('Project Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    role = StringField('Role')
    repo_link = StringField('Repository Link')
    live_link = StringField('Live Project Link')
    related_skills = MultiCheckboxField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_checkbox]
    )
    submit = SubmitField('Submit')

class UpdateProjectForm(FlaskForm):
    """
    A form for updating a project in the user's digital CV.

    Attributes:
    -----------
    project : SelectField
        A dropdown menu of the user's existing projects to choose from.
    name : StringField
        A field for the updated name of the project.
    description : TextAreaField
        A field for the updated description of the project.
    role : StringField
        A field for the updated role of the user in the project.
    repo_link : StringField
        A field for the updated repository link of the project.
    live_link : StringField
        A field for the updated live project link of the project.
    related_skills : MultiCheckboxField
        A field for selecting the skills related to the updated project.
    submit : SubmitField
        A button to submit the updated project information.
    """
    project = SelectField('Project to Update', coerce=str)
    name = StringField('Updated Project Name', validators=[DataRequired()])
    description = TextAreaField('Updated Description')
    role = StringField('Updated Role')
    repo_link = StringField('Updated Repository Link')
    live_link = StringField('Updated Live Project Link')
    related_skills = MultiCheckboxField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_checkbox]
    )
    submit = SubmitField('Update Project')

class DeleteProjectForm(FlaskForm):
    """
    A form to delete a project from the user's digital CV.

    Attributes:
    -----------
    project : SelectField
        A dropdown menu to select the project to be deleted.
    submit : SubmitField
        A button to submit the form and delete the selected project.
    """
    project = SelectField('Project to Delete', coerce=str)
    submit = SubmitField('Delete Project')


# Skill Forms
class SkillsFilterForm(FlaskForm):
    """
    A form for filtering skills.

    Attributes:
    - skills: A MultiCheckboxField for selecting skills.
    - filter: A SubmitField for submitting the form.
    """
    skills = MultiCheckboxField('Skills', choices=[])
    filter = SubmitField('Filter')

class AddSkillForm(FlaskForm):
    """
    A form to add a new skill to the user's digital CV.

    Attributes:
    - name (StringField): a required field for the name of the skill.
    - image (FileField): an optional field for an image representing the skill.
    - submit (SubmitField): a button to submit the form.
    """
    name = StringField('Skill Name', validators=[DataRequired()])
    image = FileField('Skill Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    submit = SubmitField('Add Skill')

class DeleteSkillForm(FlaskForm):
    related_skills = SelectField('Skill to Delete', coerce=str)
    submit = SubmitField('Delete Skill')


# Blog forms
class AddBlogForm(FlaskForm):
    """
    A form for adding a new blog post.

    Attributes:
    - name (StringField): The name of the blog post.
    - description (TextAreaField): A brief description of the blog post.
    - content_file (StringField): The file path to the content of the blog post.
    - related_skills (MultiCheckboxField): A list of related skills for the blog post.
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

class AddTutorialForm(FlaskForm):
    """
    A form to add a new tutorial to the database.

    Attributes:
    - name (StringField): The name of the tutorial.
    - description (TextAreaField): The description of the tutorial.
    - content_file (StringField): The file containing the tutorial content.
    - related_skills (MultiCheckboxField): The skills related to the tutorial.
    - submit (SubmitField): The button to submit the form.
    """
    name = StringField('Tutorial Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    content_file = StringField('Content File')
    related_skills = MultiCheckboxField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_checkbox]
    )
    submit = SubmitField('Submit')

class DeleteTutorialForm(FlaskForm):
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
    related_skills : MultiCheckboxField
        A list of related skills to choose from.
    submit : SubmitField
        A button to submit the form.
    """
    tutorial = SelectField('Tutorial to Update', coerce=str)
    name = StringField('Updated Tutorial Name', validators=[DataRequired()])
    description = TextAreaField('Updated Description')
    content_file = StringField('Content File')
    related_skills = MultiCheckboxField(
        'Related Skills',
        choices=[],
        validators=[at_least_one_checkbox]
    )
    submit = SubmitField('Update Tutorial')
