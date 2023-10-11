# Auth Forms

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
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
