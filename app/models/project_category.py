# Path: digital_cv/app/models/project_category.py

from .base import BaseModel, db

class ProjectCategory(BaseModel):
    """
    A class representing a project category.

    Attributes:
        Inherits all attributes from BaseModel
    """
    __tablename__ = 'project_categories'
    description = db.Column(db.String(500), nullable=True)
    projects = db.relationship('Project', back_populates='category')

    def __repr__(self):
        return f"<ProjectCategory (ID: {self.id}, Name: {self.name})>"
