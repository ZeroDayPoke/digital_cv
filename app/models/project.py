#!/usr/bin/env python3
"""Project model"""
# Path: digital_cv/app/models/project.py

from .base import BaseModel, db
from enum import Enum
from sqlalchemy import UniqueConstraint
from .associations import project_skills, project_users


class ProjectStatus(Enum):
    PLANNING = "Planning"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    ON_HOLD = "On Hold"


class Project(BaseModel):
    __tablename__ = 'projects'
    role = db.Column(db.String(120), nullable=True)
    repo_link = db.Column(db.String(500), nullable=True)
    live_link = db.Column(db.String(500), nullable=True)
    misc_link = db.Column(db.String(500), nullable=True)
    misc_name = db.Column(db.String(120), nullable=True)
    status = db.Column(db.Enum(ProjectStatus), nullable=False,
                       default=ProjectStatus.PLANNING)
    category_id = db.Column(db.String(60), db.ForeignKey(
        'project_categories.id'), nullable=True)
    category = db.relationship('ProjectCategory', back_populates='projects')
    collaborators = db.relationship(
        'User', secondary=project_users, back_populates='projects')
    related_skills = db.relationship(
        'Skill', secondary=project_skills, back_populates='related_projects')
    is_featured = db.Column(db.Boolean, default=False, nullable=False)
    featured_order = db.Column(db.Integer, nullable=True)

    __table_args__ = (UniqueConstraint(
        'featured_order', name='_featured_order_uc'),)

    def __repr__(self):
        return f"<Project (ID: {self.id}, Name: {self.name}, Featured: {self.is_featured})>"
