#!/usr/bin/env python3
"""Project model"""
# Path: digital_cv/app/models/blog.py

from .base import BaseModel, db
from .associations import blog_skills

class Blog(BaseModel):
    __tablename__ = 'blogs'
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    content_file = db.Column(db.String(500), nullable=True)
    related_skills = db.relationship('Skill', secondary=blog_skills, back_populates='related_blogs')

    def __repr__(self):
        return f"<Blog (ID: {self.id}, Name: {self.name})>"
