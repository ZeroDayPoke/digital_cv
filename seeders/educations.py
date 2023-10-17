# ./seeders/seed_educations.py

from app.models import Education, Skill
from app import db

def seed_educations():
    """Seed the educations table with real data"""
    educations = [
        {
            "institution": "Oklahoma State University",
            "location": "Stillwater, OK, USA",
            "field_of_study": "Chemical Engineering",
            "grad_date": "2015",
            "details": "Graduated with a Bachelors of Science in Chemical Engineering.",
            "image_filename": "osu.png",
            "skills": ["Chemical Engineering", "Mathematics"]
        },
        {
            "institution": "Holberton School",
            "location": "Tulsa, OK, USA",
            "field_of_study": "Computer Science and Full Stack Web Development",
            "grad_date": "2024",
            "details": "Currently attending for Computer Science and Full Stack Web Development",
            "image_filename": "holberton.png",
            "skills": ["Python", "JavaScript", "HTML", "CSS"]
        }
    ]

    # Query existing educations to prevent duplicates
    existing_educations = db.session.query(Education.institution, Education.field_of_study).all()
    
    for education_data in educations:
        # Convert each dictionary to a tuple of (institution, field_of_study)
        check_tuple = (education_data['institution'], education_data['field_of_study'])
        
        if check_tuple not in existing_educations:
            # Separate out the 'skills' field for special handling
            skill_names = education_data.pop('skills', [])

            # Create Education object
            education = Education(**education_data)

            # Query for Skill objects that match the names in 'skills'
            related_skills = db.session.query(Skill).filter(Skill.name.in_(skill_names)).all()

            # Associate the queried Skill objects with the education
            education.related_skills = related_skills

            # Add Education object to session
            db.session.add(education)
    
    # Commit the session to save all changes
    db.session.commit()
