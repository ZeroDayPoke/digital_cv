#!/usr/bin/env python3
"""Education model"""
# Path: digital_cv/app/models/education.py

from .base import BaseModel, db
from .associations import education_skills

class Education(BaseModel):
    __tablename__ = 'educations'

    institution = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    field_of_study = db.Column(db.String(120), nullable=False)
    grad_date = db.Column(db.String(20), nullable=True, default='attending')
    details = db.Column(db.String(500), nullable=True)
    related_skills = db.relationship('Skill', secondary=education_skills, back_populates='related_educations')

    def __repr__(self):
        return f"<Education (ID: {self.id}, Institution: {self.institution}, Field of Study: {self.field_of_study})>"
