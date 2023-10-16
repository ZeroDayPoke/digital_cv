# ./seeders/skills.py

from app.models import Skill
from app import db

def seed_skills():
    """Seed the skills table"""
    skills = [
        {"name": "Python", "image_filename": ""},
        {"name": "Flask", "image_filename": ""},
    ]
    
    # Query existing skills to prevent duplicates
    existing_skills = [s.name for s in db.session.query(Skill.name).all()]
    
    for skill_data in skills:
        if skill_data["name"] not in existing_skills:
            skill = Skill(**skill_data)
            db.session.add(skill)
    
    db.session.commit()
