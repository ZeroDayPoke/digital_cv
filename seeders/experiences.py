# ./seeders/experience.py

from app.models import Experience
from app import db
from datetime import datetime

def seed_experiences():

    experience_data = {
        "name": "Tutoring",
        "company": "Tulsa Community Foundation",
        "location": "Tulsa",
        "position": "Tutor",
        "start_date": datetime(2023, 1, 1),
        "end_date": datetime(2023, 6, 30),
        "is_current": False,
        "description": "Tutoring role at Holberton School Tulsa.",
        "experience_type": "Part-time",
    }

    # Check if the experience already exists
    existing_experience = db.session.query(Experience).filter_by(company=experience_data["company"], position=experience_data["position"]).first()

    # If not, add it to the session
    if not existing_experience:
        experience = Experience(**experience_data)
        db.session.add(experience)

    # Commit to the database
    db.session.commit()
