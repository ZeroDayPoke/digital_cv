# ./seeder.py

from seeders import seed_roles, seed_users, seed_skills, seed_tutorials, seed_blogs, seed_educations
import os
from app import create_app

def seed_all():
    """
    Seed all tables in the database with initial data.

    This function calls all the individual seed functions for each table in the database:
    - roles
    - users
    - skills
    - tutorials
    - blogs
    - educations
    """
    seed_roles()
    seed_users()
    seed_skills()
    seed_tutorials()
    seed_blogs()
    seed_educations()

app = create_app(os.getenv("FLASK_ENV") or "default")

with app.app_context():
    seed_all()
