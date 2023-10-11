#!/usr/bin/env python3
"""Skill model"""
# Path: digital_cv/app/models/skill.py

from .base import BaseModel, db
from .associations import project_skills, blog_skills, tutorial_skills

class Skill(BaseModel):
    """
    A class representing a skill.

    Attributes:
    -----------
    name : str
        The name of the skill.
    related_projects : list
        A list of related projects.
    related_blogs : list
        A list of related blogs.
    related_tutorials : list
        A list of related tutorials.
    """
    __tablename__ = 'skills'
    name = db.Column(db.String(120), nullable=False)
    related_projects = db.relationship('Project', secondary=project_skills, back_populates='related_skills')
    related_blogs = db.relationship('Blog', secondary=blog_skills, back_populates='related_skills')
    related_tutorials = db.relationship('Tutorial', secondary=tutorial_skills, back_populates='related_skills')

    def __repr__(self):
        return f"<Skill (ID: {self.id}, Name: {self.name})>"
