# ./seeders/project_categories.py

from app.models import ProjectCategory
from app import db

def seed_project_categories():
    """Seed the project_categories table"""
    categories = [
        {"name": "Full Stack Web Development", "description": "Full stack web development projects."},
        {"name": "Data Science", "description": "Projects related to data science."},
        {"name": "Design", "description": "Projects related to design."},
        {"name": "Machine Learning", "description": "Projects related to machine learning."},
        {"name": "Live Code", "description": "Projects related to live codings."},
        {"name": "DevOps", "description": "Projects related to DevOps."},
        {"name": "Mathematics", "description": "Projects related to mathematics."},
        {"name": "Low Level Programming", "description": "Projects related to low level programming."},
        {"name": "Web Development - AirBnB Clone", "description": "AirBnB clone projects."},
        {"name": "Web Development", "description": "General web development category."},
    ]

    # Query existing categories to prevent duplicates
    existing_categories = db.session.query(ProjectCategory.name).all()
    existing_categories = [item[0] for item in existing_categories]

    for category_data in categories:
        if category_data['name'] not in existing_categories:
            category = ProjectCategory(**category_data)
            db.session.add(category)

    db.session.commit()
