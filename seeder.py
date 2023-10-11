#!/usr/bin/env python3
"""
seeder.py

This module contains functions for seeding the database with initial data.
"""
import os
from decouple import config
from app import create_app, db
from app.models import User, Role, Skill, Project, Blog, Tutorial

app = create_app(os.getenv("FLASK_ENV") or "default")

def seed_roles():
    """Seed the roles table"""
    with app.app_context():
        roles = ["ADMIN", "USER", "GUEST"]
        for role_name in roles:
            role = Role(name=role_name)
            db.session.add(role)
        db.session.commit()

def seed_users():
    """
    Seed the users table with default admin, user and guest accounts.
    """
    with app.app_context():
        admin_username = config('DEFAULT_ADMIN_USERNAME', default='admin')
        admin_password = config('DEFAULT_ADMIN_PASSWORD', default='admin')
        admin_email = config('DEFAULT_ADMIN_EMAIL', default='admin@admin.admin')
        users = [
            {"username": admin_username, "email": admin_email, "password": admin_password, "role": "ADMIN"},
            {"username": "user", "email": "user@zerodaypoke.com", "password": "user", "role": "USER"},
            {"username": "guest", "email": "guest@zerodaypoke.com", "password": "guest", "role": "GUEST"},
        ]
        for user_data in users:
            role = Role.query.filter_by(name=user_data.pop("role")).first()
            user = User(**user_data)
            user.roles.append(role)
            db.session.add(user)
        db.session.commit()

def seed_skills():
    """Seed the skills table"""
    with app.app_context():
        skills = [
            {"name": "Python", "image_filename": ""},
            {"name": "Flask", "image_filename": ""},
            {"name": "SQLAlchemy", "image_filename": ""},
            {"name": "HTML", "image_filename": ""},
            {"name": "CSS", "image_filename": ""},
            {"name": "JavaScript", "image_filename": ""}
        ]
        existing_skills = [s.name for s in Skill.query.all()]
        for skill_data in skills:
            if skill_data["name"] not in existing_skills:
                skill = Skill(**skill_data)
                db.session.add(skill)

        db.session.commit()

def seed_projects():
    """Seed the projects table"""
    with app.app_context():
        projects = [{"name": "Digital CV", "description": "A digital CV project made with Flask.", "role": "Full-stack developer", "repo_link": "https://github.com/ZeroDayPoke/digital_cv", "live_link": "https://zerodaypoke.com", "image_filename": "notfound2.png"}]
        for project_data in projects:
            project = Project(**project_data)
            db.session.add(project)
        db.session.commit()

def seed_blogs():
    """Seed the blogs table"""
    with app.app_context():
        blogs = [
            {"name": "My Journey to Programming", "description": "A blog post about how I got into programming.", "content_file": "journey", "image_filename": "notfound1.png"},
        ]
        for blog_data in blogs:
            blog = Blog(**blog_data)
            db.session.add(blog)
        db.session.commit()

def seed_tutorials():
    """Seed the tutorials table"""
    with app.app_context():
        tutorials = [
            {"name": "Flask Tutorial", "description": "A tutorial on Flask.", "content_file": "tutorial", "image_filename": "notfound4.png"},
        ]
        for tutorial_data in tutorials:
            tutorial = Tutorial(**tutorial_data)
            db.session.add(tutorial)
        db.session.commit()

def seed_all():
    """Seed all tables"""
    seed_roles()
    seed_users()
    seed_skills()
    seed_projects()
    seed_blogs()
    seed_tutorials()

if __name__ == "__main__":
    seed_all()
