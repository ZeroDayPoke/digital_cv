# ./seeders/projects.py

from app.models import Project
from app import db

def seed_projects():
    """Seed the projects table"""
    projects = [
        {
            "name": "Digital CV", 
            "description": "A digital CV project made with Flask.", 
            "role": "Full-stack developer", 
            "repo_link": "https://github.com/ZeroDayPoke/digital_cv", 
            "live_link": "https://zerodaypoke.com", 
            "image_filename": "notfound2.png"
        },
        {
            "name": "Better Flask", 
            "description": "A Flask project with a better structure.", 
            "role": "Full-stack developer", 
            "repo_link": "",
            "live_link": "",
            "image_filename": "notfound2.png"
        },
    ]
    
    # Query existing projects to prevent duplicates
    existing_projects = db.session.query(Project.name, Project.repo_link).all()
    
    for project_data in projects:
        # Convert each dictionary to a tuple of (name, repo_link)
        check_tuple = (project_data['name'], project_data['repo_link'])
        
        if check_tuple not in existing_projects:
            project = Project(**project_data)
            db.session.add(project)
    
    db.session.commit()
