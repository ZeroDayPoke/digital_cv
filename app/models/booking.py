# ./app/models/booking.py

from .base import BaseModel, db
from datetime import datetime

class Booking(BaseModel):
    __tablename__ = 'bookings'

    service_id = db.Column(db.String(60), db.ForeignKey('services.id'), nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(60), nullable=False, default='pending')

    service = db.relationship('Service', backref='bookings')
    user = db.relationship('User', backref='bookings')

    def __repr__(self):
        return f"<Booking (ID: {self.id}, Service ID: {self.service_id}, User ID: {self.user_id})>"
