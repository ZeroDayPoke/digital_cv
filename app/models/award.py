#!/usr/bin/env python3

from .base import BaseModel, db

class Award(BaseModel):
    __tablename__ = 'awards'
    issuer = db.Column(db.String(120), nullable=True)
