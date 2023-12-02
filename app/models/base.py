#!/usr/bin/env python3
"""BaseModel"""
# Path: digital_cv/app/models/base.py

from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from datetime import datetime

db = SQLAlchemy()


class BaseModel(db.Model):
    """
    Base model for all database models.

    Attributes:
        id (str): Primary key of the model.
        image_filename (str): Name of the image file.
        created_at (datetime): Date and time when the model was created.
        updated_at (datetime): Date and time when the model was last updated.
    """
    __abstract__ = True
    id = db.Column(db.String(60), primary_key=True,
                   default=lambda: str(uuid4()), nullable=False)
    name = db.Column(db.String(120), nullable=True)
    description = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow, onupdate=datetime.utcnow)
    image_filename = db.Column(db.String(128), nullable=True)
    image_filename_two = db.Column(db.String(128), nullable=True)
    image_filename_three = db.Column(db.String(128), nullable=True)
    image_filename_four = db.Column(db.String(128), nullable=True)

    def get_images(self):
        """
        Retrieve all images associated with this instance.

        Returns:
            list of Image: A list of Image objects associated with the instance.
        """
        from .image import Image
        return Image.query.filter_by(owner_id=self.id, owner_type=self.__tablename__).all()

    def __repr__(self):
        return f"<{self.__class__.__name__} (ID: {self.id})>"

    def construct_file_path(self, filename):
        """
        Construct the file path for an image based on the model name and filename.

        Args:
            filename (str): The name of the file.

        Returns:
            str: The constructed file path.
        """
        model_name = self.__class__.__name__.lower()
        return f"./app/static/images/{model_name}s/{filename}"
