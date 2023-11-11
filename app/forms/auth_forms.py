#!/usr/bin/env python3

# Auth Forms

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo

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
    username = StringField(
        'Username', 
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "Username"
        }
    )
    email = StringField(
        'Email', 
        validators=[DataRequired(), Email()],
        render_kw={
            "class": "form-control",
            "placeholder": "Email"
        }
    )
    password = PasswordField(
        'Password', 
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "Password",
            "autocomplete": "password"
        }
    )
    confirm_password = PasswordField(
        'Confirm Password', 
        validators=[DataRequired(), EqualTo('password')],
        render_kw={
            "class": "form-control",
            "placeholder": "Confirm Password",
            "autocomplete": "confirm password"
        }
    )
    submit = SubmitField(
        'Sign Up',
        render_kw={
            "class": "btn btn-primary"
        }
    )

class SigninForm(FlaskForm):
    """
    A form for user sign in.

    Attributes:
    - email (StringField): an input field for user email
    - password (PasswordField): an input field for user password
    - submit (SubmitField): a button to submit the form
    """
    email = StringField(
        'Email', 
        validators=[DataRequired(), Email()],
        render_kw={
            "class": "form-control", 
            "placeholder": "Email"
        }
    )
    password = PasswordField(
        'Password', 
        validators=[DataRequired()],
        render_kw={
            "class": "form-control", 
            "placeholder": "Password",
            "autocomplete": "password"
        }
    )
    submit = SubmitField(
        'Sign In',
        render_kw={
            "class": "btn btn-primary"
        }
    )

class UploadCVForm(FlaskForm):
    """
    A form for uploading a CV in PDF format.

    Attributes:
    - cv (FileField): The field for uploading the CV file.
    """
    cv = FileField(
        'Upload CV (PDF only)', 
        validators=[
            FileRequired(),
            FileAllowed(['pdf'], 'PDFs only!')
        ],
        render_kw={
            "class": "form-control-file"
        }
    )
    submit = SubmitField(
        'Upload',
        render_kw={
            "class": "btn btn-primary"
        }
    )

class MessageAdminForm(FlaskForm):
    """
    A form for messaging the admin.

    Attributes:
    - message_body (TextAreaField): The field for entering the message.
    - submit (SubmitField): A button to submit the form.
    """
    message_body = TextAreaField(
        'Message',
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "rows": 5,
            "placeholder": "Type your message here..."
        }
    )
    submit = SubmitField(
        'Send Message',
        render_kw={
            "class": "btn btn-primary"
        }
    )

class ChangePasswordForm(FlaskForm):
    """
    A form for changing user password.
    
    Attributes:
    - current_password (PasswordField): an input field for the current password
    - new_password (PasswordField): an input field for the new password
    - confirm_password (PasswordField): an input field for confirming the new password
    - submit (SubmitField): a button to submit the form
    """
    current_password = PasswordField(
        'Current Password', 
        validators=[DataRequired()],
        render_kw={
            "class": "form-control", 
            "placeholder": "Current Password"
        }
    )
    new_password = PasswordField(
        'New Password', 
        validators=[DataRequired()],
        render_kw={
            "class": "form-control", 
            "placeholder": "New Password"
        }
    )
    confirm_password = PasswordField(
        'Confirm New Password', 
        validators=[DataRequired(), EqualTo('new_password')],
        render_kw={
            "class": "form-control", 
            "placeholder": "Confirm New Password"
        }
    )
    submit = SubmitField(
        'Change Password',
        render_kw={
            "class": "btn btn-primary"
        }
    )
