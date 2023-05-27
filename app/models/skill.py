#!/usr/bin/env python3
"""Skill model"""
# Path: digital_cv/app/models/skill.py

from .base import BaseModel, db
from .associations import project_skills

class Skill(BaseModel):
    __tablename__ = 'skills'
    name = db.Column(db.String(120), nullable=False)
    related_projects = db.relationship('Project', secondary=project_skills, back_populates='related_skills')

    def __repr__(self):
        return f"<Skill (ID: {self.id}, Name: {self.name})>"
