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
    image_filename = db.Column(db.String(128), nullable=True)
    image_filename_two = db.Column(db.String(128), nullable=True)
    image_filename_three = db.Column(db.String(128), nullable=True)
    image_filename_four = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow, onupdate=datetime.utcnow)
