#!/usr/bin/env python3
"""Project model"""
# Path: digital_cv/app/models/project.py

from .base import BaseModel, db
from .associations import project_skills

class Project(BaseModel):
    """
    A class representing a project.

    Attributes:
    -----------
    id : str
        The unique identifier of the project.
    name : str
        The name of the project.
    description : str
        The description of the project.
    role : str
        The role of the user in the project.
    repo_link : str
        The link to the project's repository.
    live_link : str
        The link to the live version of the project.
    misc_link : str
        The link to any other relevant information about the project.
    misc_name : str
        The name of the misc_link (to be displayed).
    related_skills : list of Skill objects
        The list of skills related to the project.
    """

    __tablename__ = 'projects'
    description = db.Column(db.String(500), nullable=True)
    role = db.Column(db.String(120), nullable=True)
    repo_link = db.Column(db.String(500), nullable=True)
    live_link = db.Column(db.String(500), nullable=True)
    misc_link = db.Column(db.String(500), nullable=True)
    misc_name = db.Column(db.String(120), nullable=True)
    related_skills = db.relationship('Skill', secondary=project_skills, back_populates='related_projects')

    def __repr__(self):
        return f"<Project (ID: {self.id}, Name: {self.name})>"
