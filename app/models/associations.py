#!/usr/bin/env python3
"""Associations"""
# Path: digital_cv/app/models/associations.py

from .base import db

project_skills = db.Table(
    'project_skills',
    db.Column('project_id', db.String(60), db.ForeignKey('projects.id'), primary_key=True),
    db.Column('skill_id', db.String(60), db.ForeignKey('skills.id'), primary_key=True)
)

user_roles = db.Table(
    'user_roles',
    db.Column('user_id', db.String(60), db.ForeignKey('users.id')),
    db.Column('role_id', db.String(60), db.ForeignKey('roles.id'))
)
