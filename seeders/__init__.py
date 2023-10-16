# ./seeders/__init__.py

from .roles import seed_roles
from .users import seed_users
from .skills import seed_skills
from .tutorials import seed_tutorials
from .blogs import seed_blogs
from .educations import seed_educations

def seed_all():
    """Seed all tables"""
    seed_roles()
    seed_users()
    seed_skills()
    seed_tutorials()
    seed_blogs()
    seed_educations()
