# ./seeders/skills.py

from app.models import Skill, SkillLevel
from app import db

def seed_skills():
    skills = [
        {"name": "Python", "image_filename": "python.png", "level": SkillLevel.INTERMEDIATE, "category": "Language"},
        {"name": "Flask", "image_filename": "flask.png", "level": SkillLevel.INTERMEDIATE, "category": "Framework"},
        {"name": "SQLAlchemy", "image_filename": "sqlalchemy.png", "level": SkillLevel.INTERMEDIATE, "category": "ORM"},
        {"name": "MySQL", "image_filename": "mysql.png", "level": SkillLevel.INTERMEDIATE, "category": "Database"},
        {"name": "React", "image_filename": "react.png", "level": SkillLevel.INTERMEDIATE, "category": "Framework"},
        {"name": "Bootstrap", "image_filename": "bootstrap.png", "level": SkillLevel.INTERMEDIATE, "category": "Library"},
        {"name": "C", "image_filename": "c.png", "level": SkillLevel.INTERMEDIATE, "category": "Language"},
        {"name": "Node.js", "image_filename": "node.png", "level": SkillLevel.INTERMEDIATE, "category": "Runtime"},
        {"name": "nginx", "image_filename": "nginx.png", "level": SkillLevel.INTERMEDIATE, "category": "Web Server"},
        {"name": "Docker", "image_filename": "docker.png", "level": SkillLevel.INTERMEDIATE, "category": "Containerization"},
        {"name": "Git", "image_filename": "git.png", "level": SkillLevel.INTERMEDIATE, "category": "Version Control"},
        {"name": "Express", "image_filename": "express.png", "level": SkillLevel.INTERMEDIATE, "category": "Framework"},
        {"name": "JavaScript", "image_filename": "javascript.png", "level": SkillLevel.INTERMEDIATE, "category": "Language"},
        {"name": "Chemical Engineering", "image_filename": "cheme.png", "level": SkillLevel.INTERMEDIATE, "category": "Field"},
        {"name": "Mathematics", "image_filename": "maths.png", "level": SkillLevel.INTERMEDIATE, "category": "Field"},
        {"name": "HTML", "image_filename": "html.png", "level": SkillLevel.INTERMEDIATE, "category": "Markup Language"},
        {"name": "CSS", "image_filename": "css.png", "level": SkillLevel.INTERMEDIATE, "category": "Style Language"},
        {"name": "Figma", "image_filename": "figma.png", "level": SkillLevel.INTERMEDIATE, "category": "Design Tool"},
        {"name": "Machine Learning", "image_filename": "ml.png", "level": SkillLevel.INTERMEDIATE, "category": "Field"},
        {"name": "Bash Scripting", "image_filename": "bash.png", "level": SkillLevel.INTERMEDIATE, "category": "Scripting"},
        {"name": "Typescript", "image_filename": "ts.png", "level": SkillLevel.INTERMEDIATE, "category": "Language"},
        {"name": "dotnet SDK", "image_filename": "dotnet.png", "level": SkillLevel.INTERMEDIATE, "category": "Framework"},
        {"name": "C#", "image_filename": "csharp.png", "level": SkillLevel.INTERMEDIATE, "category": "Language"},
        {"name": "sequelize", "image_filename": "sequelize.png", "level": SkillLevel.INTERMEDIATE, "category": "ORM"},
        {"name": "sales", "image_filename": "sales.png", "level": SkillLevel.INTERMEDIATE, "category": "Field"},
    ]

    # Query existing skills to prevent duplicates
    existing_skills = [s.name for s in db.session.query(Skill.name).all()]
    
    for skill_data in skills:
        if skill_data["name"] not in existing_skills:
            skill = Skill(**skill_data)
            db.session.add(skill)
    
    db.session.commit()
