# ./seeders/project_categories.py

from app.models import ProjectCategory
from app import db

def seed_project_categories():
    """Seed the project_categories table"""
    categories = [
        {"name": "Web Development", "description": "Projects related to web development."},
        {"name": "Data Science", "description": "Projects related to data science."},
        {"name": "Design", "description": "Projects related to design."},
        {"name": "Machine Learning", "description": "Projects related to machine learning."},
        {"name": "DevOps", "description": "Projects related to DevOps."},
        {"name": "Low Level Programming", "description": "Projects related to low level programming."},
    ]

    # Query existing categories to prevent duplicates
    existing_categories = db.session.query(ProjectCategory.name).all()
    existing_categories = [item[0] for item in existing_categories]

    for category_data in categories:
        if category_data['name'] not in existing_categories:
            category = ProjectCategory(**category_data)
            db.session.add(category)

    db.session.commit()
