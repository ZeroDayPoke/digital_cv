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
    """Seed the users table"""
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
        skills = ["Python", "Flask", "SQLAlchemy", "HTML", "CSS", "JavaScript"]
        for skill_name in skills:
            skill = Skill(name=skill_name)
            db.session.add(skill)
        db.session.commit()

def seed_projects():
    """Seed the projects table"""
    with app.app_context():
        projects = [
            {"name": "Digital CV", "description": "A digital CV project made with Flask.", "role": "Full-stack developer", "repo_link": "https://github.com/ZeroDayPoke/digital_cv", "live_link": "https://zerodaypoke.com"},
        ]
        for project_data in projects:
            project = Project(**project_data)
            db.session.add(project)
        db.session.commit()

def seed_blogs():
    """Seed the blogs table"""
    with app.app_context():
        blogs = [
            {"name": "My Journey to Programming", "description": "A blog post about how I got into programming.", "content_file": "journey.html"},
        ]
        for blog_data in blogs:
            blog = Blog(**blog_data)
            db.session.add(blog)
        db.session.commit()

def seed_tutorials():
    """Seed the tutorials table"""
    with app.app_context():
        tutorials = [
            {"name": "Flask Tutorial", "description": "A tutorial on Flask.", "content_file": "tutorial.html"},
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
