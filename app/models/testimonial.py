# ./app/models/testimonial.py

from .base import BaseModel, db

class Testimonial(BaseModel):
    __tablename__ = 'testimonials'

    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    service_id = db.Column(db.String(60), db.ForeignKey('services.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

    user = db.relationship('User', backref='testimonials')
    service = db.relationship('Service', backref='testimonials')

    def __repr__(self):
        return f"<Testimonial (ID: {self.id}, User ID: {self.user_id})>"
