# ./seeders/users.py

from decouple import config
from app.models import User, Role
from app import db

def seed_users():
    """Seed the users table with default admin, user and guest accounts."""
    admin_username = config('DEFAULT_ADMIN_USERNAME', default='dev')
    admin_password = config('DEFAULT_ADMIN_PASSWORD', default='dev')
    admin_email = config('DEFAULT_ADMIN_EMAIL', default='dev@dev.dev')

    # Query existing usernames and emails to prevent duplicates
    existing_usernames = [u.username for u in db.session.query(User.username).all()]
    existing_emails = [u.email for u in db.session.query(User.email).all()]

    users = [
        {"username": admin_username, "email": admin_email, "password": admin_password, "role": "ADMIN"},
        {"username": "mason", "email": "mason@zerodaypoke.com", "password": "mason", "role": "USER", "github_username": "spindouken"},
        {"username": "rob", "email": "rob@zerodaypoke.com", "password": "rob", "role": "USER", "github_username": "Nomad-Rob"},
        {"username": "jules", "email": "jules@zerodaypoke.com", "password": "jules", "role": "USER", "github_username": "Julia-5534"},
        {"username": "twood", "email": "twood@zerodaypoke.com", "password": "twood", "role": "USER", "github_username": "WoodsonTD"},
        {"username": "jobb", "email": "jobb@zerodaypoke.com", "password": "jobb", "role": "USER", "github_username": "jobabyyy"}
    ]

    for user_data in users:
        if user_data["username"] not in existing_usernames and user_data["email"] not in existing_emails:
            role = Role.query.filter_by(name=user_data.pop("role")).first()
            user = User(**user_data)
            user.roles.append(role)
            db.session.add(user)

    db.session.commit()
