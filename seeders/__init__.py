# ./seeders/__init__.py

from .roles import seed_roles
from .users import seed_users
from .skills import seed_skills
from .tutorials import seed_tutorials
from .blogs import seed_blogs
from .educations import seed_educations
from .projects import seed_projects
from .experiences import seed_experiences

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
    seed_projects()
    seed_experiences()
