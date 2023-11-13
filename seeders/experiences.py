# ./seeders/experience.py

from app.models import Experience
from app import db
from datetime import datetime


def seed_experiences():
    experiences = [
        {
            "name": "Tutoring",
            "company": "Tulsa Community Foundation",
            "location": "Tulsa OK USA",
            "position": "Tutor",
            "start_date": datetime(2023, 1, 1),
            "end_date": datetime(2023, 6, 30),
            "is_current": False,
            "description": "Tutoring role at Holberton School Tulsa.",
            "experience_type": "Part-time",
            "image_filename": "tcf.png"
        },
        {
            "name": "Vintage Collectible Sales",
            "company": "Diamond Paws",
            "location": "Tulsa OK USA",
            "position": "Salesperson",
            "start_date": datetime(2020, 1, 1),
            "is_current": True,
            "description": "Pivoted from the beginning of covid... still at it...",
            "experience_type": "Full-time",
            "image_filename": "diamond_paws.png"
        }
    ]

    existing_experiences = db.session.query(
        Experience.company, Experience.position).all()

    for experience_data in experiences:
        check_tuple = (experience_data['company'], experience_data['position'])

        if check_tuple not in existing_experiences:
            experience = Experience(**experience_data)
            db.session.add(experience)

    db.session.commit()
