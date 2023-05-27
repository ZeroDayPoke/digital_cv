#!/usr/bin/env python3
"""User Model"""
# Import necessary modules

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .base import BaseModel, db
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, ForeignKey

class Role(BaseModel):
    __tablename__ = 'roles'

    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role {}>'.format(self.name)

# UserRoles association table
user_roles = Table('user_roles', BaseModel.metadata,
    Column('user_id', db.String(60), ForeignKey('users.id')),
    Column('role_id', db.String(60), ForeignKey('roles.id'))
)

class User(UserMixin, BaseModel):
    __tablename__ = 'users'

    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    roles = relationship('Role', secondary=user_roles, backref=db.backref('users', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        """creates new User"""
        super().__init__(*args, **kwargs)
        self.set_password(kwargs.get('password'))

    def __repr__(self):
        """User representation"""
        return f'<User {self.username}>'

    def set_password(self, pwd):
        """encrypts password"""
        self.password_hash = generate_password_hash(pwd)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def has_role(self, role_name):
        return any(role.name == role_name for role in self.roles)
