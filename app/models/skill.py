#!/usr/bin/env python3
"""Skill model"""
# Path: digital_cv/app/models/skill.py

from .base import BaseModel, db
from .associations import project_skills, blog_skills, tutorial_skills, education_skills
from sqlalchemy import UniqueConstraint
from enum import Enum

class SkillCategory(Enum):
    LANGUAGE = "Language"
    FRAMEWORK = "Framework"
    ORM = "ORM"
    DATABASE = "Database"
    LIBRARY = "Library"
    RUNTIME = "Runtime"
    VERSION_CONTROL = "Version Control"
    INFRASTRUCTURE = "Infrastucture"
    DESIGN_TOOL = "Design Tool"
    FIELD = "Field"
    DEVOPS = "DevOps"

class SkillLevel(Enum):
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3

class Skill(BaseModel):
    __tablename__ = 'skills'
    level = db.Column(db.Enum(SkillLevel), nullable=True)
    category = db.Column(db.Enum(SkillCategory), nullable=True)
    is_featured = db.Column(db.Boolean, default=False, nullable=False)
    featured_order = db.Column(db.Integer, nullable=True)
    related_projects = db.relationship('Project', secondary=project_skills, back_populates='related_skills')
    related_blogs = db.relationship('Blog', secondary=blog_skills, back_populates='related_skills')
    related_tutorials = db.relationship('Tutorial', secondary=tutorial_skills, back_populates='related_skills')
    related_educations = db.relationship('Education', secondary=education_skills, back_populates='related_skills')

    __table_args__ = (UniqueConstraint('featured_order', name='_featured_order_uc'),)

    def __repr__(self):
        return f"<Skill (ID: {self.id}, Name: {self.name}, Featured: {self.is_featured})>"

    def association_count(self):
        return len(self.related_projects) + len(self.related_blogs) + len(self.related_tutorials) + len(self.related_educations)
