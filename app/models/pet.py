# app/models/pet.py

from .base import BaseModel, db
from sqlalchemy.dialects.postgresql import JSON

class Pet(BaseModel):
    __tablename__ = 'pets'
    
    breed = db.Column(db.String(120), nullable=True)
    description = db.Column(db.String(500), nullable=True)
    images = db.Column(JSON, nullable=True)
    is_featured = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Pet (ID: {self.id}, Name: {self.name}, Breed: {self.breed})>"
