# ./seeders/skills.py

from app.models import Skill, SkillLevel, SkillCategory
from app import db


def seed_skills():
    skills = [
        # Languages
        {"name": "JavaScript", "image_filename": "javascript.png", "level": SkillLevel.INTERMEDIATE,
            "category": SkillCategory.LANGUAGE, "is_featured": True, "featured_order": 1},
        {"name": "Python", "image_filename": "python.png", "level": SkillLevel.ADVANCED,
            "category": SkillCategory.LANGUAGE, "is_featured": True, "featured_order": 2},
        {"name": "C", "image_filename": "c.png",
            "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.LANGUAGE},
        {"name": "TypeScript", "image_filename": "ts.png",
            "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.LANGUAGE},
        {"name": "C#", "image_filename": "csharp.png",
            "level": SkillLevel.BEGINNER, "category": SkillCategory.LANGUAGE},
        {"name": "HTML", "image_filename": "html.png",
            "level": SkillLevel.ADVANCED, "category": SkillCategory.LANGUAGE},
        {"name": "CSS", "image_filename": "css.png",
            "level": SkillLevel.BEGINNER, "category": SkillCategory.LANGUAGE},
        {"name": "Bash Scripting", "image_filename": "bash.png",
            "level": SkillLevel.ADVANCED, "category": SkillCategory.LANGUAGE},

        # Frameworks
        {"name": "Flask", "image_filename": "flask.png", "level": SkillLevel.ADVANCED,
            "category": SkillCategory.FRAMEWORK, "is_featured": True, "featured_order": 3},
        {"name": "React", "image_filename": "react.png", "level": SkillLevel.INTERMEDIATE,
            "category": SkillCategory.FRAMEWORK, "is_featured": True, "featured_order": 6},
        {"name": "Express", "image_filename": "express.png", "level": SkillLevel.INTERMEDIATE,
            "category": SkillCategory.FRAMEWORK, "is_featured": True, "featured_order": 12},
        {"name": ".NET SDK", "image_filename": "dotnet.png",
            "level": SkillLevel.BEGINNER, "category": SkillCategory.FRAMEWORK},

        # ORMs
        {"name": "SQLAlchemy", "image_filename": "sqlalchemy.png", "level": SkillLevel.INTERMEDIATE,
            "category": SkillCategory.ORM, "is_featured": True, "featured_order": 4},
        {"name": "Sequelize", "image_filename": "sequelize.png",
            "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.ORM},

        # Database
        {"name": "MySQL", "image_filename": "mysql.png", "level": SkillLevel.ADVANCED,
            "category": SkillCategory.DATABASE, "is_featured": True, "featured_order": 5},

        # Libraries
        {"name": "Bootstrap", "image_filename": "bootstrap.png", "level": SkillLevel.INTERMEDIATE,
            "category": SkillCategory.LIBRARY, "is_featured": True, "featured_order": 7},
        {"name": "jQuery", "image_filename": "jq.png", "level": SkillLevel.INTERMEDIATE,
            "category": SkillCategory.LIBRARY, "is_featured": False},

        # Runtime
        {"name": "Node.js", "image_filename": "node.png", "level": SkillLevel.ADVANCED,
            "category": SkillCategory.RUNTIME, "is_featured": True, "featured_order": 8},

        # Version Control
        {"name": "Git", "image_filename": "git.png", "level": SkillLevel.INTERMEDIATE,
            "category": SkillCategory.VERSION_CONTROL, "is_featured": True, "featured_order": 11},

        # DevOps
        {"name": "GCP", "image_filename": "gcp.png",
            "level": SkillLevel.BEGINNER, "category": SkillCategory.DEVOPS},
        {"name": "Postman", "image_filename": "post.png", "level": SkillLevel.INTERMEDIATE,
            "category": SkillCategory.DEVOPS, "is_featured": False},
        {"name": "Visual Studio Code", "image_filename": "vsc.png", "level": SkillLevel.ADVANCED,
            "category": SkillCategory.DEVOPS, "is_featured": False},

        # Design Tools
        {"name": "Figma", "image_filename": "figma.png",
            "level": SkillLevel.BEGINNER, "category": SkillCategory.DESIGN_TOOL},


        # Fields
        {"name": "Chemical Engineering", "image_filename": "cheme.png",
            "level": SkillLevel.ADVANCED, "category": SkillCategory.FIELD},
        {"name": "Mathematics", "image_filename": "maths.png",
            "level": SkillLevel.ADVANCED, "category": SkillCategory.FIELD},
        {"name": "Machine Learning", "image_filename": "ml.png",
            "level": SkillLevel.BEGINNER, "category": SkillCategory.FIELD},
        {"name": "Sales", "image_filename": "sales.png",
            "level": SkillLevel.INTERMEDIATE, "category": SkillCategory.FIELD},

        # Infrastructure
        {"name": "Linux", "image_filename": "linux.png",
            "level": SkillLevel.ADVANCED, "category": SkillCategory.INFRASTRUCTURE},
        {"name": "Nginx", "image_filename": "nginx.png", "level": SkillLevel.INTERMEDIATE,
            "category": SkillCategory.INFRASTRUCTURE, "is_featured": True, "featured_order": 9},
        {"name": "Docker", "image_filename": "docker.png", "level": SkillLevel.INTERMEDIATE,
            "category": SkillCategory.INFRASTRUCTURE, "is_featured": True, "featured_order": 10},
    ]

    existing_skills = [s.name for s in db.session.query(Skill.name).all()]

    for skill_data in skills:
        if skill_data["name"] not in existing_skills:
            skill = Skill(**skill_data)
            db.session.add(skill)

    db.session.commit()
