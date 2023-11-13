#!/usr/bin/env python3
"""Project model"""
# Path: digital_cv/app/models/blog.py

from .base import BaseModel, db
from .associations import blog_skills


class Blog(BaseModel):
    """
    A class representing a blog post.

    Attributes:
    -----------
    id : str
        The unique identifier of the blog post.
    name : str
        The name of the blog post.
    description : str
        The description of the blog post.
    content_file : str
        The path to the file containing the content of the blog post.
    related_skills : list of Skill objects
        The list of skills related to the blog post.

    Methods:
    --------
    __repr__() -> str
        Returns a string representation of the Blog object.
    """
    __tablename__ = 'blogs'
    description = db.Column(db.String(500), nullable=True)
    content_file = db.Column(db.String(500), nullable=True)
    tags = db.Column(db.String(120), nullable=True)
    related_skills = db.relationship(
        'Skill', secondary=blog_skills, back_populates='related_blogs')

    def __repr__(self):
        return f"<Blog (ID: {self.id}, Name: {self.name})>"
