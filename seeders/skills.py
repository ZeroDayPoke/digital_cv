# ./seeders/skills.py

from app.models import Skill, SkillLevel, SkillCategory
from app import db

def seed_skills():
    skills = [
        # Languages
        {"name": "JavaScript", "image_filename": "javascript.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.LANGUAGE, "is_featured": True, "featured_order": 1},
        {"name": "Python", "image_filename": "python.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.LANGUAGE, "is_featured": True, "featured_order": 2},
        {"name": "C", "image_filename": "c.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.LANGUAGE},
        {"name": "TypeScript", "image_filename": "ts.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.LANGUAGE},
        {"name": "C#", "image_filename": "csharp.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.LANGUAGE},
        
        # Frameworks
        {"name": "Flask", "image_filename": "flask.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.FRAMEWORK, "is_featured": True, "featured_order": 3},
        {"name": "React", "image_filename": "react.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.FRAMEWORK, "is_featured": True, "featured_order": 6},
        {"name": "Express", "image_filename": "express.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.FRAMEWORK, "is_featured": True, "featured_order": 12},
        {"name": ".NET SDK", "image_filename": "dotnet.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.FRAMEWORK},

        # ORMs
        {"name": "SQLAlchemy", "image_filename": "sqlalchemy.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.ORM, "is_featured": True, "featured_order": 4},
        {"name": "Sequelize", "image_filename": "sequelize.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.ORM},

        # Database
        {"name": "MySQL", "image_filename": "mysql.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.DATABASE, "is_featured": True, "featured_order": 5},

        # Libraries
        {"name": "Bootstrap", "image_filename": "bootstrap.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.LIBRARY, "is_featured": True, "featured_order": 7},

        # Runtime
        {"name": "Node.js", "image_filename": "node.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.RUNTIME, "is_featured": True, "featured_order": 8},

        # Web Server
        {"name": "Nginx", "image_filename": "nginx.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.WEB_SERVER, "is_featured": True, "featured_order": 9},

        # Containerization
        {"name": "Docker", "image_filename": "docker.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.CONTAINERIZATION, "is_featured": True, "featured_order": 10},

        # Version Control
        {"name": "Git", "image_filename": "git.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.VERSION_CONTROL, "is_featured": True, "featured_order": 11},

        # Markup Language
        {"name": "HTML", "image_filename": "html.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.MARKUP_LANGUAGE},

        # Style Language
        {"name": "CSS", "image_filename": "css.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.STYLE_LANGUAGE},

        # Design Tool
        {"name": "Figma", "image_filename": "figma.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.DESIGN_TOOL},

        # Fields
        {"name": "Chemical Engineering", "image_filename": "cheme.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.FIELD},
        {"name": "Mathematics", "image_filename": "maths.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.FIELD},
        {"name": "Machine Learning", "image_filename": "ml.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.FIELD},
        {"name": "Sales", "image_filename": "sales.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.FIELD},

        # Scripting
        {"name": "Bash Scripting", "image_filename": "bash.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.SCRIPTING},

        # OS
        {"name": "Linux", "image_filename": "linux.png", "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.OS},
    ]

    # Query existing skills to prevent duplicates
    existing_skills = [s.name for s in db.session.query(Skill.name).all()]
    
    for skill_data in skills:
        if skill_data["name"] not in existing_skills:
            skill = Skill(**skill_data)
            db.session.add(skill)
    
    db.session.commit()

# Call the function at the end or where needed to seed the data
seed_skills()
