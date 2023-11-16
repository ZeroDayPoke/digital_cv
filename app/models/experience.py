#!/usr/bin/env python3

# ./app/models/experience.py

from .base import BaseModel, db
from datetime import datetime


class Experience(BaseModel):
    __tablename__ = 'experiences'

    company = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    position = db.Column(db.String(120), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=True)
    is_current = db.Column(db.Boolean, default=False)
    experience_type = db.Column(db.String(60), nullable=True)

    def __repr__(self):
        return f"<Experience (ID: {self.id}, Company: {self.company}, Position: {self.position})>"

    @property
    def duration(self):
        if self.end_date:
            return self.end_date - self.start_date
        else:
            return datetime.utcnow() - self.start_date
