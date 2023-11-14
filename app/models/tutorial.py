#!/usr/bin/env python3
"""Tutorial model"""
# Path: digital_cv/app/models/tutorial.py

from .base import BaseModel, db
from .associations import tutorial_skills
from bs4 import BeautifulSoup

class Tutorial(BaseModel):
    __tablename__ = 'tutorials'
    description = db.Column(db.String(500), nullable=True)
    content_file = db.Column(db.String(500), nullable=True)
    content_html = db.Column(db.Text, nullable=False)
    title = db.Column(db.String(120), nullable=False)
    tags = db.Column(db.String(120), nullable=True)
    related_skills = db.relationship(
        'Skill', secondary=tutorial_skills, back_populates='related_tutorials')

    def __repr__(self):
        return f"<Tutorial (ID: {self.id}, Name: {self.name})>"

    def get_sections(self):
        """
        Parses the stored HTML content to extract sections for generating the table of contents.

        Returns:
            list: A list of dictionaries containing the section title and anchor.
        """
        soup = BeautifulSoup(self.content_html, 'html.parser')
        sections = []

        for h2 in soup.find_all('h2'):
            title = h2.get_text()
            anchor = h2.attrs.get('id', '')
            sections.append({
                'title': title,
                'anchor': anchor
            })

        return sections
