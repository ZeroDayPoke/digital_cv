# ./seeders/seed_educations.py

from app.models import Education
from app import db

def seed_educations():
    """Seed the educations table with real data"""
    educations = [
        {
            "institution": "Oklahoma State University",
            "location": "Stillwater, OK, USA",
            "field_of_study": "Chemical Engineering",
            "grad_date": "2015",
            "details": "Graduated with a Bachelors of Science in Chemical Engineering."
        },
        {
            "institution": "Holberton School",
            "location": "Tulsa, OK, USA",
            "field_of_study": "Computer Science and Full Stack Web Development",
            "grad_date": "2024",
            "details": "Currently attending for Computer Science and Full Stack Web Development"
        }
    ]
    
    # Query existing educations to prevent duplicates
    existing_educations = db.session.query(Education.institution, Education.field_of_study).all()
    
    for education_data in educations:
        # Convert each dictionary to a tuple of (institution, field_of_study)
        check_tuple = (education_data['institution'], education_data['field_of_study'])
        
        if check_tuple not in existing_educations:
            education = Education(**education_data)
            db.session.add(education)
    
    db.session.commit()
