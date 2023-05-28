#!/usr/bin/env python3
"""Project model"""
# Path: digital_cv/app/models/project.py

from .base import BaseModel, db
from .associations import project_skills

class Project(BaseModel):
    __tablename__ = 'projects'
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    role = db.Column(db.String(120), nullable=True)
    repo_link = db.Column(db.String(500), nullable=True)
    live_link = db.Column(db.String(500), nullable=True)
    related_skills = db.relationship('Skill', secondary=project_skills, back_populates='related_projects')

    def __repr__(self):
        return f"<Project (ID: {self.id}, Name: {self.name})>"
