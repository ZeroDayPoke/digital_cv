#!/usr/bin/env python3

from .base import BaseModel, db

class Image(BaseModel):
    __tablename__ = 'images'

    owner_id = db.Column(db.String(60), nullable=False)
    owner_type = db.Column(db.String(50), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    filename = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<Image (ID: {self.id}, Owner ID: {self.owner_id}, Owner Type: {self.owner_type}, Description: {self.description})>"

    @property
    def file_path(self):
        """Returns the full file path for the image."""
        return f"app/static/images/{self.owner_type}/{self.filename}"
