# ./seeders/__init__.py

from .roles import seed_roles
from .users import seed_users
from .skills import seed_skills
from .tutorials import seed_tutorials
from .blogs import seed_blogs
from .educations import seed_educations
from .project_categories import seed_project_categories
from .projects import seed_projects
from .experiences import seed_experiences
from .pets import seed_pets
from .awards import seed_awards


def seed_all():
    seed_roles()
    seed_users()
    seed_skills()
    seed_project_categories()
    seed_tutorials()
    seed_blogs()
    seed_educations()
    seed_projects()
    seed_experiences()
    seed_pets()
    seed_awards()
