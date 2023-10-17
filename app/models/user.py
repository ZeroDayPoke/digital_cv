#!/usr/bin/env python3
"""User Model"""
# Import necessary modules

from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .base import BaseModel, db
from sqlalchemy.orm import relationship
from .associations import user_roles

class Role(BaseModel):
    """
    A class representing the roles of users in the system.

    Attributes:
    -----------
    name : str
        The name of the role.
    """

    __tablename__ = 'roles'

    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role {}>'.format(self.name)

class User(UserMixin, BaseModel):
    """
    User model class that inherits from UserMixin and BaseModel.
    """
    __tablename__ = 'users'

    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    roles = relationship('Role', secondary=user_roles, backref=db.backref('users', lazy='dynamic'))
    verification_token = db.Column(db.String(40))
    verified = db.Column(db.Boolean, default=False)
    token_generated_at = db.Column(db.DateTime, default=datetime.utcnow)
    messages = db.relationship('Message', backref='sender', lazy='dynamic')

    def __init__(self, *args, **kwargs):
        """
        Initializes a new User object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        password = kwargs.pop('password', None)
        super().__init__(*args, **kwargs)
        if password:
            self.set_password(password)

    def __repr__(self):
        """
        Returns a string representation of the User object.

        Returns:
            str: A string representation of the User object.
        """
        return f'<User {self.username}>'

    def set_password(self, pwd):
        """
        Encrypts the given password and sets the password hash.

        Args:
            pwd (str): The password to encrypt.
        """
        self.password_hash = generate_password_hash(pwd)

    @property
    def password(self):
        """
        Raises an AttributeError since password is a write-only field.

        Raises:
            AttributeError: Always raised since password is a write-only field.
        """
        raise AttributeError('password: write-only field')

    def check_password(self, password):
        """
        Checks if the given password matches the stored password hash.

        Args:
            password (str): The password to check.

        Returns:
            bool: True if the password matches the stored password hash, False otherwise.
        """
        return check_password_hash(self.password_hash, password)

    def has_role(self, role_name):
        """
        Checks if the user has the given role.

        Args:
            role_name (str): The name of the role to check.

        Returns:
            bool: True if the user has the given role, False otherwise.
        """
        return any(role.name == role_name for role in self.roles)

    def token_expired(self):
        """
        Checks if the user's token has expired.

        Returns:
            bool: True if the user's token has expired, False otherwise.
        """
        expiration_time = self.token_generated_at + timedelta(hours=24)
        return datetime.utcnow() > expiration_time
