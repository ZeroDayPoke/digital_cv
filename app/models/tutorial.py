#!/usr/bin/env python3
"""Tutorial model"""
# Path: digital_cv/app/models/tutorial.py

from .base import BaseModel, db
from .associations import tutorial_skills

class Tutorial(BaseModel):
    """
    A class representing a tutorial.

    Attributes:
    -----------
    name : str
        The name of the tutorial.
    description : str
        A description of the tutorial.
    content_file : str
        The file containing the content of the tutorial.
    related_skills : list of Skill objects
        A list of skills related to the tutorial.
    """
    __tablename__ = 'tutorials'
    description = db.Column(db.String(500), nullable=True)
    content_file = db.Column(db.String(500), nullable=True)
    related_skills = db.relationship('Skill', secondary=tutorial_skills, back_populates='related_tutorials')

    def __repr__(self):
        return f"<Blog (ID: {self.id}, Name: {self.name})>"
