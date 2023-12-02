# app/models/pet.py

from .base import BaseModel, db

class Pet(BaseModel):
    __tablename__ = 'pets'
    
    breed = db.Column(db.String(120), nullable=True)
    is_featured = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Pet (ID: {self.id}, Name: {self.name}, Breed: {self.breed})>"
