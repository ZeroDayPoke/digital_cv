#!/usr/bin/env python3
"""BaseModel"""
# Path: digital_cv/app/models/base.py

from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from datetime import datetime

db = SQLAlchemy()


class BaseModel(db.Model):
    """
    Base model class for all models in the application.

    Attributes:
        id (str): The unique identifier for the model.
        name (str): The name of the model.
        description (str): The description of the model.
        created_at (datetime): The timestamp when the model was created.
        updated_at (datetime): The timestamp when the model was last updated.
        image_filename (str): The filename of the main image associated with the model.
        image_filename_two (str): The filename of the second image associated with the model.
        image_filename_three (str): The filename of the third image associated with the model.
        image_filename_four (str): The filename of the fourth image associated with the model.
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
