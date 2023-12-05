# ./app/models/service.py

from .mixins import FilterSortMixin
from .base import BaseModel, db
from sqlalchemy.dialects.postgresql import JSON

class Service(FilterSortMixin, BaseModel):
    __tablename__ = 'services'
    details = db.Column(JSON, nullable=True)
    price = db.Column(db.Float, nullable=True)
    currency = db.Column(db.String(3), nullable=True)
    is_available = db.Column(db.Boolean, default=True)
    category = db.Column(db.String(100), nullable=True)
    duration = db.Column(db.String(100), nullable=True)
    target_audiences = db.Column(JSON, nullable=True)
    promo = db.Column(JSON, nullable=True)
    note = db.Column(db.String(200), nullable=True)
    early_eligible = db.Column(db.Boolean, default=True)
    experimental = db.Column(db.Boolean, default=False)

    def to_dict(self):
        """
        Convert Service object into a dictionary format.
        """
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'currency': self.currency,
            'category': self.category,
            'is_available': self.is_available,
            'early_eligible': self.early_eligible,
            'experimental': self.experimental,
            'image_url': f"static/images/services/{self.image_filename}",
            'details': self.details,
            'duration': self.duration,
        }

    @classmethod
    def get_price_range(cls):
        min_price = db.session.query(db.func.min(cls.price)).scalar()
        max_price = db.session.query(db.func.max(cls.price)).scalar()
        return min_price, max_price
