# ./seeders/roles.py

from app.models import Role
from app import db

def seed_roles():
    """Seed the roles table"""
    roles = ["ADMIN", "USER", "GUEST"]
    existing_roles = [r.name for r in Role.query.all()]
    for role_name in roles:
        if role_name not in existing_roles:
            role = Role(name=role_name)
            db.session.add(role)
    db.session.commit()
