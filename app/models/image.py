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
    def full_file_path(self):
        """Returns the full file path for the image."""
        return self.construct_file_path(self.image_filename)
