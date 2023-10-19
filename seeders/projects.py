# ./seeders/projects.py

from app.models import Project, Skill
from app import db

def seed_projects():
    """Seed the projects table"""
    projects = [
        {
            "name": "Digital CV", 
            "description": "A digital CV project made with... well everything", 
            "role": "Full-stack developer", 
            "repo_link": "https://github.com/ZeroDayPoke/digital_cv", 
            "live_link": "https://zerodaypoke.com", 
            "image_filename": "digital_cv.png",
            "skills": ["Flask", "Python", "JavaScript", "CSS", "HTML", "Git", "nginx", "Docker", "SQLAlchemy", "node.js", "MySQL", "Expresss", "Bootstrap"]
        },
        {
            "name": "Strain.GG Clouds", 
            "description": "hack sprint project",
            "role": "Full-stack developer", 
            "repo_link": "https://https://github.com/ZeroDayPoke/strain.gg_clouds",
            "live_link": "https://strain.gg",
            "image_filename": "notfound2.png",
            "skills": ["Flask", "Python", "JavaScript"]
        },
        {
            "name": "holberton-designer-two",
            "description": "second phase of designer language project series",
            "role": "Full-stack developer", 
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web_front_end/tree/main/designer_research",
            "live_link": "https://docs.google.com/document/d/195bomF7w6ZZoa1gO6grQRx5MF7JNvM-J2y48fV555Qs/edit?usp=sharing",
            "image_filename": "holberton-designer-two.png",
            "skills": ["Figma"],
            "misc_link": "https://www.figma.com/file/aM3UyUZTMKUMWXocCOdYIx/Concept?type=design&node-id=0%3A1&mode=design&t=uWh0rNdxmB4TwYqM-1",
            "misc_name": "fima link"
        }
    ]
    
    # Query existing projects to prevent duplicates
    existing_projects = db.session.query(Project.name, Project.repo_link).all()

    for project_data in projects:
        # Convert each dictionary to a tuple of (name, repo_link)
        check_tuple = (project_data['name'], project_data['repo_link'])

        if check_tuple not in existing_projects:
            # Separate out the 'skills' field for special handling
            skill_names = project_data.pop('skills', [])

            # Create Project object
            project = Project(**project_data)

            # Query for Skill objects that match the names in 'skills'
            related_skills = db.session.query(Skill).filter(Skill.name.in_(skill_names)).all()

            # Associate the queried Skill objects with the project
            project.related_skills = related_skills

            # Add Project object to session
            db.session.add(project)

    # Commit the session to save all changes
    db.session.commit()
