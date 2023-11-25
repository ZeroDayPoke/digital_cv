# ./app/models/service.py

from .base import BaseModel, db
from sqlalchemy.dialects.postgresql import JSON

class Service(BaseModel):
    __tablename__ = 'services'
    
    # Details about the service
    details = db.Column(JSON, nullable=True)

    # Pricing information
    price = db.Column(db.Float, nullable=True)
    currency = db.Column(db.String(3), nullable=True)

    # Availability of the service
    is_available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<Service (ID: {self.id}, Title: {self.title})>"
