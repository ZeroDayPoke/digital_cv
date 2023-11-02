# ./seeders/projects.py

from app.models import Project, Skill, User, ProjectCategory
from app import db

def seed_projects():
    """Seed the projects table"""
    projects = [
        {
            "name": "Digital CV",
            "category": "Web Development",
            "description": "A digital CV project made with... well everything", 
            "role": "Full-stack developer", 
            "repo_link": "https://github.com/ZeroDayPoke/digital_cv", 
            "live_link": "https://zerodaypoke.com", 
            "image_filename": "digital_cv.png",
            "skills": ["Flask", "Python", "JavaScript", "CSS", "HTML", "Git", "nginx", "Docker", "SQLAlchemy", "node.js", "MySQL", "Expresss", "Bootstrap"],
            "collaborators": ["mason"]
        },
        {
            "name": "Strain.GG Clouds",
            "category": "Web Development",
            "description": "hack sprint project",
            "role": "Full-stack developer", 
            "repo_link": "https://github.com/ZeroDayPoke/strain.gg_clouds",
            "live_link": "https://strain.gg",
            "image_filename": "notfound2.png",
            "skills": ["Flask", "Python", "JavaScript"],
            "collaborators": ["jobb", "twood"]
        },
        {
            "name": "holberton-designer-two",
            "category": "Design",
            "description": "second phase of designer language project series",
            "role": "Full-stack developer", 
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web_front_end/tree/main/designer_research",
            "live_link": "https://docs.google.com/document/d/195bomF7w6ZZoa1gO6grQRx5MF7JNvM-J2y48fV555Qs/edit?usp=sharing",
            "image_filename": "holberton-designer-two.png",
            "skills": ["Figma"],
            "misc_link": "https://www.figma.com/file/aM3UyUZTMKUMWXocCOdYIx/Concept?type=design&node-id=0%3A1&mode=design&t=uWh0rNdxmB4TwYqM-1",
            "misc_name": "figma link",
            "collaborators": ["rob"]
        },
        {
            "name": "holberton-designer-one",
            "category": "Design",
            "description": "first phase of designer language project series",
            "role": "Full-stack developer",
            "repo_link": "",
            "skills": ["Figma"],
            "collaborators": ["rob"]
        },
        {
            "name": "holberton-designer-three",
            "category": "Design",
            "description": "third phase of designer language project series",
            "role": "Full-stack developer",
            "repo_link": "",
            "skills": ["Figma"],
            "collaborators": ["rob"]
        },
        {
            "name": "Monty",
            "category": "Low level Programming",
            "description": "A monty bytecode interpreter",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-monty",
            "skills": ["C", "Linux"],
            "collaborators": ["linzo"]
        },
        {
            "name": "printf",
            "category": "Low level Programming",
            "description": "A printf clone",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-printf",
            "skills": ["C", "Linux"],
            "collaborators": ["mason", "jobb"],
        },
        {
            "name": "simple_shell",
            "category": "Low level Programming",
            "description": "A simple shell",
            "role": "hol-bb",
            "skills": ["C", "Linux"],
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-simple_shell",
            "collaborators": ["jules"],
        },
        {
            "name": "HBNB Phase 1",
            "category": "Web Development",
            "description": "First phase of the AirBnB clone",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-AirBnB_clone",
            "skills": ["Python", "Linux"],
            "collaborators": ["heather"],
        },
        {
            "name": "HBNB Phase 2",
            "category": "Web Development",
            "description": "Second phase of the AirBnB clone",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-AirBnB_clone_v2",
            "skills": ["Python", "Linux", "MySQL", "SQLAlchemy", "HTML", "CSS", "Flask"],
            "collaborators": ["colan"],
        },
        {
            "name": "HBNB Phase 3",
            "category": "Web Development",
            "description": "Third phase of the AirBnB clone",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-AirBnB_clone_v3",
            "skills": ["Python", "Linux", "MySQL", "SQLAlchemy", "HTML", "CSS", "Flask"],
            "collaborators": ["philip", "atay"],
        },
        {
            "name": "HBNB Phase 4",
            "category": "Web Development",
            "description": "Fourth phase of the AirBnB clone",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-AirBnB_clone_v4",
            "skills": ["Python", "Linux", "MySQL", "SQLAlchemy", "HTML", "CSS", "Flask"],
        },
        {
            "name": "Classification",
            "category": "Machine Learning",
            "description": "ML - CLASSIFICATION",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/classification",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Optimization",
            "category": "Machine Learning",
            "description": "ML - OPTIMIZATION",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/optimization",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Error Analysis",
            "category": "Machine Learning",
            "description": "ML - ERROR ANALYSIS",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/error_analysis",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Keras",
            "category": "Machine Learning",
            "description": "ML - KERAS",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/keras",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Object Detection",
            "category": "Machine Learning",
            "description": "ML - OBJECT DETECTION",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/object_detection",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Convolutional Neural Nets",
            "category": "Machine Learning",
            "description": "ML - CNN",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/cnn",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Tensorflow",
            "category": "Machine Learning",
            "description": "ML - TENSORFLOW",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/tensorflow",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Regularization",
            "category": "Machine Learning",
            "description": "ML - REGULARIZATION",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/regularization",
            "skills": ["Python", "Linux"],
        }
    ]

    # Query existing projects to prevent duplicates
    existing_projects = db.session.query(Project.name, Project.repo_link).all()

    for project_data in projects:
        # Convert each dictionary to a tuple of (name, repo_link)
        check_tuple = (project_data['name'], project_data['repo_link'])

        if check_tuple not in existing_projects:
            # Separate out the 'skills' and 'collaborators' fields for special handling
            skill_names = project_data.pop('skills', [])
            collaborator_usernames = project_data.pop('collaborators', [])  # Pop collaborators

            # Pop the category field and query for it
            category_name = project_data.pop('category', None)
            category = None
            if category_name:
                category = db.session.query(ProjectCategory).filter_by(name=category_name).first()

            # Create Project object
            project = Project(**project_data)

            # Set category if found
            if category:
                project.category_id = category.id

            # Query for Skill objects that match the names in 'skills'
            related_skills = db.session.query(Skill).filter(Skill.name.in_(skill_names)).all()

            # Associate the queried Skill objects with the project
            project.related_skills = related_skills

            # Query for User objects that match the usernames in 'collaborators'
            collaborators = db.session.query(User).filter(User.username.in_(collaborator_usernames)).all()

            # Associate the queried User objects with the project
            project.collaborators = collaborators  # Assign collaborators

            # Add Project object to session
            db.session.add(project)

    # Commit the session to save all changes
    db.session.commit()
