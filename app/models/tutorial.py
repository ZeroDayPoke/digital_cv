#!/usr/bin/env python3
"""Tutorial model"""
# Path: digital_cv/app/models/tutorial.py

from .base import BaseModel, db
from .associations import tutorial_skills

class Tutorial(BaseModel):
    __tablename__ = 'tutorials'
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    content_file = db.Column(db.String(500), nullable=True)
    related_skills = db.relationship('Skill', secondary=tutorial_skills, back_populates='related_tutorials')

    def __repr__(self):
        return f"<Blog (ID: {self.id}, Name: {self.name})>"
