# ./seeders/skills.py

from app.models import Skill
from app import db

def seed_skills():
    """Seed the skills table"""
    skills = [
        {"name": "Python", "image_filename": "python.png"},
        {"name": "Flask", "image_filename": "flask.png"},
        {"name": "SQLAlchemy", "image_filename": "sqlalchemy.png"},
        {"name": "MySQL", "image_filename": "mysql.png"},
        {"name": "React", "image_filename": "react.png"},
        {"name": "Bootstrap", "image_filename": "bootstrap.png"},
        {"name": "C", "image_filename": "c.png"},
        {"name": "Node.js", "image_filename": "node.png"},
    ]
    
    # Query existing skills to prevent duplicates
    existing_skills = [s.name for s in db.session.query(Skill.name).all()]
    
    for skill_data in skills:
        if skill_data["name"] not in existing_skills:
            skill = Skill(**skill_data)
            db.session.add(skill)
    
    db.session.commit()
