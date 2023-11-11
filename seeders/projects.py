# ./seeders/projects.py

from app.models import Project, Skill, User, ProjectCategory
from app import db

def seed_projects():
    """Seed the projects table"""
    projects = [
        {
            "name": "Digital CV",
            "category": "Full Stack Web Development",
            "description": "A digital CV project made with... well everything", 
            "role": "Full-stack developer", 
            "repo_link": "https://github.com/ZeroDayPoke/digital_cv", 
            "live_link": "https://zerodaypoke.com", 
            "image_filename": "digital_cv.png",
            "skills": ["Flask", "Python", "JavaScript", "CSS", "HTML", "Git", "nginx", "Docker", "SQLAlchemy", "node.js", "MySQL", "Expresss", "Bootstrap", "GCP"],
            "collaborators": ["mason"],
            "is_featured": True,
            "featured_order": 2
        },
        {
            "name": "Strain.GG Clouds",
            "category": "Full Stack Web Development",
            "description": "hack sprint project",
            "role": "Full-stack developer", 
            "repo_link": "https://github.com/ZeroDayPoke/strain.gg_clouds",
            "live_link": "https://strain.gg",
            "image_filename": "notfound2.png",
            "skills": ["Flask", "Python", "JavaScript", "GCP", "Docker", "nginx", "SQLAlchemy", "MySQL", "Bootstrap", "CSS", "HTML", "node.js", "Expresss", "React", "Sequelize"],
            "collaborators": ["jobb", "twood"],
            "is_featured": True,
            "featured_order": 3
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
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web_front_end/tree/main/designer_research_1",
            "skills": ["Figma"],
            "collaborators": ["rob"]
        },
        {
            "name": "holberton-designer-three",
            "category": "Design",
            "description": "third phase of designer language project series",
            "role": "Full-stack developer",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web_front_end/tree/main/designer_research_3",
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
            "category": "Web Development - AirBnB Clone",
            "description": "First phase of the AirBnB clone",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-AirBnB_clone",
            "skills": ["Python", "Linux"],
            "collaborators": ["heather"],
        },
        {
            "name": "HBNB Phase 2",
            "category": "Web Development - AirBnB Clone",
            "description": "Second phase of the AirBnB clone",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-AirBnB_clone_v2",
            "skills": ["Python", "Linux", "MySQL", "SQLAlchemy", "HTML", "CSS", "Flask"],
            "collaborators": ["colan"],
        },
        {
            "name": "HBNB Phase 3",
            "category": "Web Development - AirBnB Clone",
            "description": "Third phase of the AirBnB clone",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-AirBnB_clone_v3",
            "skills": ["Python", "Linux", "MySQL", "SQLAlchemy", "HTML", "CSS", "Flask"],
            "collaborators": ["philip", "atay"],
        },
        {
            "name": "HBNB Phase 4",
            "category": "Web Development - AirBnB Clone",
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
        },
        {
            "name": "Deep CNNs",
            "category": "Machine Learning",
            "description": "ML - DEEP CNNs",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/deep_cnns",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Calculus - Holberton",
            "category": "Mathematics",
            "description": "MATH - CALCULUS",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/math/calculus",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Linear Algebra - Holberton",
            "category": "Mathematics",
            "description": "MATH - LINEAR ALGEBRA",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/math/linear_algebra",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Probability - Holberton",
            "category": "Mathematics",
            "description": "MATH - PROBABILITY",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/math/probability",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Plotting - Holberton",
            "category": "Mathematics",
            "description": "MATH - PLOTTING",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/math/plotting",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Convolutions and Pooling - Holberton",
            "category": "Mathematics",
            "description": "MATH - CONVOLUTIONS AND POOLING",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/math/convolutions_and_pooling",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "CSS Advanced",
            "category": "Front End Web Dev",
            "description": "CSS - ADVANCED",
            "role": "Front-end developer",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web-development/tree/main/css_advanced",
            "skills": ["CSS", "HTML"],
        },
        {
            "name": "HTML Advanced",
            "category": "Front End Web Dev",
            "description": "HTML - ADVANCED",
            "role": "Front-end developer",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web-development/tree/main/html_advanced",
            "skills": ["CSS", "HTML"],
        },
        {
            "name": "Holberton Headphones",
            "category": "Front End Web Dev",
            "description": "A mockup of a headphone store",
            "role": "Front-end developer",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-headphones",
            "skills": ["CSS", "HTML", "Figma"],
        },
        {
            "name": "ES6 Basics",
            "category": "Back End Web Dev",
            "description": "ES6 - BASICS",
            "role": "Web Developer",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web_back_end/tree/main/ES6_basic",
            "skills": ["JavaScript"],
        },
        {
            "name": "ES6 Promises",
            "category": "Back End Web Dev",
            "description": "ES6 - PROMISES",
            "role": "Web Developer",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web_back_end/tree/main/ES6_promise",
            "skills": ["JavaScript"],
        },
        {
            "name": "ES6 Classes",
            "category": "Back End Web Dev",
            "description": "ES6 - CLASSES",
            "role": "Web Developer",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web_back_end/tree/main/ES6_classes",
            "skills": ["JavaScript"],
        },
        {
            "name": "ES6 Data Manipulation",
            "category": "Back End Web Dev",
            "description": "ES6 - DATA MANIPULATION",
            "role": "Web Developer",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web_back_end/tree/main/ES6_data_manipulation",
            "skills": ["JavaScript"],
        },
        {
            "name": "Low Level Programming",
            "category": "Low level Programming",
            "description": "Consolidated smaller low level programming projects",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-low_level_programming",
            "skills": ["C", "Linux"],
        },
        {
            "name": "Zero Day",
            "category": "Low level Programming",
            "description": "A collection of zero day projects",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-zero_day",
            "skills": ["C", "Linux"],
        },
        {
            "name": "Higher Level Programming",
            "category": "Higher level Programming",
            "description": "Consolidated smaller higher level programming projects",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-higher_level_programming",
            "skills": ["Python", "Linux", "JavaScript", "MySQL", "SQLAlchemy", "HTML", "CSS", "Flask"],
        },
        {
            "name": "Docker - Holberton",
            "category": "DevOps",
            "description": "Docker project from curriculum v2 update; completed as tutor, so not sure if this counts as school or work?",
            "role": "DevOps",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-softy-pinko-docker",
            "skills": ["Docker", "Linux"],
        },
        {
            "name": "System Engineering DevOps",
            "category": "DevOps",
            "description": "Consolidated smaller system engineering and devops projects",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-system_engineering-devops",
            "skills": ["Linux"],
        },
        {
            "name": "Tutoring Live Codes",
            "category": "Live Code",
            "description": "Live codes from tutoring sessions",
            "role": "Tutor",
            "repo_link": "https://github.com/ZeroDayPoke/evilcode",
            "skills": ["Python", "JavaScript", "Linux", "HTML", "CSS", "Flask", "SQLAlchemy", "MySQL", "C"],
        },
        {
            "name": "pokePick",
            "category": "Data Science",
            "description": "First full web app; currently serves as the inventory management, order management, and order fulfillment system for my business",
            "role": "Full-stack developer",
            "repo_link": "https://github.com/ZeroDayPoke/pokePick",
            "skills": ["Python", "JavaScript", "Linux", "HTML", "CSS", "Flask", "SQLAlchemy", "MySQL"],
        },
        {
            "name": "C# Exploration",
            "category": "C#",
            "description": "C# Exploration",
            "role": "Full-stack developer",
            "repo_link": "https://github.com/ZeroDayPoke/bleeding_edge",
            "skills": ["C#", "Linux", "MySQL"],
        },
        {
            "name": "Museum Prototype",
            "category": "Full Stack Web Development",
            "description": "Museum Prototype",
            "role": "Full-stack developer",
            "repo_link": "https://github.com/ZeroDayPoke/mooseum",
            "skills": ["Javascript", "HTML", "CSS", "Sequelize", "React", "MySQL", "Node.js", "Express", "GCP", "Docker", "nginx"],
            "is_featured": True,
            "featured_order": 1
        },
        {
            "name": "Sorting Algorithms",
            "category": "Low level Programming",
            "description": "Sorting Algorithms",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-sorting_algorithms",
            "skills": ["C", "Linux"],
        },
        {
            "name": "Binary Trees",
            "category": "Low level programming",
            "description": "Binary Trees",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-binary_trees",
            "skills": ["C", "Linux"],
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
