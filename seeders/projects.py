# ./seeders/projects.py

from app.models import Project, Skill, User, ProjectCategory, ProjectStatus
from app import db


def seed_projects():
    """Seed the projects table"""
    projects = [
        {
            "name": "Digital CV",
            "category": "Full Stack Web Development",
            "status": ProjectStatus.IN_PROGRESS,
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
            "status": ProjectStatus.IN_PROGRESS,
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
            "status": ProjectStatus.COMPLETED,
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
            "status": ProjectStatus.COMPLETED,
            "category": "Design",
            "description": "first phase of designer language project series",
            "role": "Full-stack developer",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web_front_end/tree/main/designer_research_1",
            "skills": ["Figma"],
            "collaborators": ["rob"]
        },
        {
            "name": "holberton-designer-three",
            "status": ProjectStatus.COMPLETED,
            "category": "Design",
            "description": "third phase of designer language project series",
            "role": "Full-stack developer",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web_front_end/tree/main/designer_research_3",
            "skills": ["Figma"],
            "collaborators": ["rob"]
        },
        {
            "name": "Monty",
            "status": ProjectStatus.COMPLETED,
            "category": "Low level Programming",
            "description": "This repository contains the source code for a Monty bytecode interpreter, a project developed as part of the Holberton School curriculum. The interpreter is written in C and is designed to execute Monty bytecode files. The interpreter reads Monty bytecode files line by line, identifies the opcode in each line, and executes the corresponding function.",
            "image_filename": "monty.png",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-monty",
            "skills": ["C", "Linux"],
            "collaborators": ["linzo"]
        },
        {
            "name": "printf",
            "status": ProjectStatus.COMPLETED,
            "category": "Low level Programming",
            "image_filename": "printf.png",
            "description": "A printf clone. The _printf function writes output to stdout, the standard output stream, according to a specified format. All parts of the _printf function in this repository are there to ensure that the user can print integers, characters, and strings of characters all within one function.",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-printf",
            "skills": ["C", "Linux"],
            "collaborators": ["mason", "jobb"],
        },
        {
            "name": "simple_shell",
            "status": ProjectStatus.COMPLETED,
            "category": "Low level Programming",
            "image_filename": "shell.png",
            "description": "This repository holds all the code necessary for our custom simple shell to run. Our shell currently handles the executables found in the environmental variable PATH, with or without their full paths. Our shell does NOT handle aliases, directory changes, or many other features presently.",
            "role": "hol-bb",
            "skills": ["C", "Linux"],
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-simple_shell",
            "collaborators": ["jules"],
        },
        {
            "name": "HBNB Phase 1",
            "status": ProjectStatus.COMPLETED,
            "category": "Web Development - AirBnB Clone",
            "description": "This is the first part of a six part series of making a simple copy of the AirBnB website. This project will be completed over four months as part of our second trimester for Holberton Tulsa.",
            "image_filename": "hbnb-one.png",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-AirBnB_clone",
            "skills": ["Python", "Linux"],
            "collaborators": ["heather"],
        },
        {
            "name": "HBNB Phase 2",
            "status": ProjectStatus.COMPLETED,
            "category": "Web Development - AirBnB Clone",
            "description": "This repository contains the second version of the AirBnB clone project, which is part of the Holberton School curriculum. In this project, you will learn about the Python programming language, specifically about data models, MySQL, web flask, and more.",
            "image_filename": "hbnb-two.png",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-AirBnB_clone_v2",
            "skills": ["Python", "Linux", "MySQL", "SQLAlchemy", "HTML", "CSS", "Flask"],
            "collaborators": ["colan"],
        },
        {
            "name": "HBNB Phase 3",
            "status": ProjectStatus.COMPLETED,
            "category": "Web Development - AirBnB Clone",
            "description": "ABNBCloneV3 is the third named repository of the Holberton AirBNB Clone projects series. The overarching goal of the series is to learn the tools associated with web development well enough to be able to replicate the popular web platform. The main component of this project is a RESTful API that allows interaction with the main application.",
            "image_filename": "hbnb-three.png",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-AirBnB_clone_v3",
            "skills": ["Python", "Linux", "MySQL", "SQLAlchemy", "HTML", "CSS", "Flask"],
            "collaborators": ["philip", "atay"],
        },
        {
            "name": "HBNB Phase 4",
            "status": ProjectStatus.COMPLETED,
            "category": "Web Development - AirBnB Clone",
            "image_filename": "hbnb-four.png",
            "description": "This project is a clone of the AirBnB website, part of the Holberton HBNB Clone Curriculum for Trimester 2. it's the fourth named iteration of the project. It includes a backend built with Python and Flask, and a frontend built with HTML, CSS, and JavaScript. The project also includes a RESTful API for data manipulation. The main additions in this version of the project are the dynamic web pages, which add significant interactivity.",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-AirBnB_clone_v4",
            "skills": ["Python", "Linux", "MySQL", "SQLAlchemy", "HTML", "CSS", "Flask"],
        },
        {
            "name": "Classification",
            "status": ProjectStatus.COMPLETED,
            "category": "Machine Learning",
            "image_filename": "classification.png",
            "description": "This project involves the implementation and training of deep neural networks for classification tasks. The primary focus is on binary classification using various neural network architectures, including both single neurons and deeper neural network structures. The project explores forward propagation, cost calculation, evaluation, and gradient descent algorithms.",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/classification",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Optimization",
            "status": ProjectStatus.COMPLETED,
            "category": "Machine Learning",
            "image_filename": "optimization.png",
            "description": "This directory contains various Python scripts that implement different optimization algorithms and techniques used in machine learning. These include normalization, shuffling data, mini-batch gradient descent, moving average, momentum optimization, RMSProp, Adam optimization, learning rate decay, and batch normalization.",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/optimization",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Error Analysis",
            "status": ProjectStatus.COMPLETED,
            "category": "Machine Learning",
            "image_filename": "error-analysis.png",
            "description": "This project, part of the Holberton School curriculum, focuses on analyzing errors in machine learning models using various metrics. It includes scripts to calculate sensitivity, precision, specificity, and the F1 score from a confusion matrix.",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/error_analysis",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Keras",
            "status": ProjectStatus.COMPLETED,
            "category": "Machine Learning",
            "image_filename": "keras.png",
            "description": "This project is part of the Holberton School curriculum and focuses on the application of machine learning techniques using the Keras library in TensorFlow. The repository includes various scripts demonstrating different functionalities in Keras, such as building models, training, testing, handling weights and configurations, and more.",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/keras",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Object Detection",
            "status": ProjectStatus.COMPLETED,
            "category": "Machine Learning",
            "image_filename": "object-detection.png",
            "description": "This project implements an object detection system using the YOLO (You Only Look Once) v3 algorithm with TensorFlow. The system processes images to detect objects, applying non-max suppression and filtering techniques. It demonstrates an understanding of concepts like convolutional neural networks, anchor boxes, bounding box regression, and class probability estimation in the context of real-world image processing.",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/object_detection",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Convolutional Neural Nets",
            "status": ProjectStatus.COMPLETED,
            "category": "Machine Learning",
            "description": "This project focuses on implementing Convolutional Neural Networks (CNNs) for image processing. We utilize various techniques such as forward and backward propagation through convolutional and pooling layers, building and training modified LeNet-5 architectures using TensorFlow and Keras.",
            "image_filename": "cnn.png",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/cnn",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Tensorflow",
            "status": ProjectStatus.COMPLETED,
            "category": "Machine Learning",
            "image_filename": "tensorflow.png",
            "description": "This project is focused on understanding and implementing various aspects of neural networks using TensorFlow. It covers creating placeholders, forward propagation, accuracy calculation, loss calculation, and training operations.",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/tensorflow",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Regularization",
            "status": ProjectStatus.COMPLETED,
            "category": "Machine Learning",
            "image_filename": "regularization.png",
            "description": "This project focuses on implementing regularization techniques in machine learning using Python and TensorFlow. The main goal is to understand and apply L2 regularization, dropout, and early stopping to improve model performance and prevent overfitting.",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/regularization",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Deep CNNs",
            "status": ProjectStatus.COMPLETED,
            "category": "Machine Learning",
            "image_filename": "deep-cnns.png",
            "description": "This project is centered around building deep convolutional neural networks (CNNs) using TensorFlow and Keras. It includes the implementation of popular architectures like Inception Network, ResNet-50, and DenseNet-121.",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/supervised_learning/deep_cnns",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Calculus - Holberton",
            "category": "Mathematics",
            "status": ProjectStatus.COMPLETED,
            "image_filename": "calculus.png",
            "description": "This directory contains various Python scripts and text files related to the study of calculus in the context of machine learning.",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/math/calculus",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Linear Algebra - Holberton",
            "status": ProjectStatus.COMPLETED,
            "category": "Mathematics",
            "image_filename": "linear-algebra.png",
            "description": "This section contains several Python scripts that perform various linear algebra operations. Part of Hulberton Tulsa - Machine Learning Specialization Path Curriculum.",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/math/linear_algebra",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Probability - Holberton",
            "status": ProjectStatus.COMPLETED,
            "category": "Mathematics",
            "image_filename": "probability.png",
            "description": "This directory contains Python scripts that implement various probability distributions. The implemented distributions include Poisson, Exponential, Normal, and Binomial classes. Part of Holberton Machine Learning Specialization.",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/math/probability",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Plotting - Holberton",
            "status": ProjectStatus.COMPLETED,
            "category": "Mathematics",
            "image_filename": "plotting.png",
            "description": "This repository includes Python scripts that generate line plots, scatter plots, histograms, bar charts, and more using the matplotlib library. The scripts also make use of the numpy library to generate and manipulate data.",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/math/plotting",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "Convolutions and Pooling - Holberton",
            "status": ProjectStatus.COMPLETED,
            "category": "Mathematics",
            "image_filename": "pooling.png",
            "description": "This project involves the implementation of various convolution and pooling operations on images. It focuses on understanding and applying different types of convolutions and pooling techniques using NumPy.",
            "role": "ML-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-machine_learning/tree/main/math/convolutions_and_pooling",
            "skills": ["Python", "Linux"],
        },
        {
            "name": "CSS Advanced",
            "status": ProjectStatus.COMPLETED,
            "category": "Front End Web Dev",
            "description": "CSS - ADVANCED",
            "role": "Front-end developer",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web-development/tree/main/css_advanced",
            "skills": ["CSS", "HTML"],
        },
        {
            "name": "HTML Advanced",
            "status": ProjectStatus.COMPLETED,
            "category": "Front End Web Dev",
            "description": "HTML - ADVANCED",
            "role": "Front-end developer",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web-development/tree/main/html_advanced",
            "skills": ["CSS", "HTML"],
        },
        {
            "name": "Holberton Headphones",
            "status": ProjectStatus.COMPLETED,
            "category": "Front End Web Dev",
            "description": "A mockup of a headphone store",
            "role": "Front-end developer",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-headphones",
            "skills": ["CSS", "HTML", "Figma"],
        },
        {
            "name": "ES6 Basics",
            "status": ProjectStatus.COMPLETED,
            "category": "Back End Web Dev",
            "image_filename": "es6-basics.png",
            "description": "This project focuses on exploring the basics of ECMAScript 6 (ES6) features and syntax. It includes various tasks demonstrating the use of arrow functions, spread operator, rest parameters, string interpolation, loops, and more.",
            "role": "Web Developer",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web_back_end/tree/main/ES6_basic",
            "skills": ["JavaScript"],
        },
        {
            "name": "ES6 Promises",
            "status": ProjectStatus.COMPLETED,
            "category": "Back End Web Dev",
            "image_filename": "es6-promises.png",
            "description": "This project delves into ES6 Promises in JavaScript, providing a fundamental understanding of asynchronous programming. It includes a variety of tasks that showcase the creation and handling of promises, error handling with try-catch blocks, and the use of async-await syntax.",
            "role": "Web Developer",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web_back_end/tree/main/ES6_promise",
            "skills": ["JavaScript"],
        },
        {
            "name": "ES6 Classes",
            "status": ProjectStatus.COMPLETED,
            "image_filename": "es6-classes.png",
            "category": "Back End Web Dev",
            "description": "This project focuses on demonstrating the use of ES6 classes in JavaScript. It includes various implementations of classes, extending classes, and using class features such as constructor methods, getters, setters, and static methods. The project serves as an educational tool for understanding ES6 class syntax and features in a practical context.",
            "role": "Web Developer",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web_back_end/tree/main/ES6_classes",
            "skills": ["JavaScript"],
        },
        {
            "name": "ES6 Data Manipulation",
            "status": ProjectStatus.COMPLETED,
            "image_filename": "es6-data-manipulation.png",
            "category": "Back End Web Dev",
            "description": "This project is focused on data manipulation using ES6 features in JavaScript. It includes a variety of exercises that demonstrate the use of arrays, sets, maps, and typed arrays, along with common operations like filtering, mapping, and reducing. The project serves as a learning tool for understanding modern JavaScript data manipulation techniques.",
            "role": "Web Developer",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-web_back_end/tree/main/ES6_data_manipulation",
            "skills": ["JavaScript"],
        },
        {
            "name": "Low Level Programming",
            "status": ProjectStatus.COMPLETED,
            "category": "Low level Programming",
            "image_filename": "lowlevel.png",
            "description": "This repository contains projects for Holberton School's low-level programming track. These projects are designed to provide a deep understanding of the C programming language, as well as covering the concepts of Linux programming, data structures, algorithms, and more.",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-low_level_programming",
            "skills": ["C", "Linux"],
        },
        {
            "name": "Zero Day",
            "status": ProjectStatus.COMPLETED,
            "image_filename": "zeroday.png",
            "category": "Low level Programming",
            "description": "This repo was created as part of the Holberton School Tulsa initial projects sprint. It contains answers to specific questions related to the following topics: 0x01 - emacs 0x02 - vi 0x03 - git",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-zero_day",
            "skills": ["C", "Linux"],
        },
        {
            "name": "Higher Level Programming",
            "status": ProjectStatus.COMPLETED,
            "category": "Higher Level Programming",
            "image_filename": "highlevel.png",
            "description": "This repository contains projects for training in the Holberton School higher level programming track. The primary languages used are Python and JavaScript (tho there were a few MySQL projects).",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-higher_level_programming",
            "skills": ["Python", "Linux", "JavaScript", "MySQL", "SQLAlchemy", "HTML", "CSS", "Flask"],
        },
        {
            "name": "Docker - Holberton",
            "status": ProjectStatus.COMPLETED,
            "category": "DevOps",
            "description": "Docker project from curriculum v2 update; completed as tutor, so not sure if this counts as school or work?",
            "role": "DevOps",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-softy-pinko-docker",
            "skills": ["Docker", "Linux"],
        },
        {
            "name": "System Engineering DevOps",
            "status": ProjectStatus.COMPLETED,
            "category": "DevOps",
            "description": "This repository contains various projects and tasks carried out during the System Engineering and DevOps track at Holberton School. The projects cover a wide range of topics including shell basics, shell permissions, web infrastructure design, and more.",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-system_engineering-devops",
            "skills": ["Linux"],
        },
        {
            "name": "Tutoring Live Codes",
            "status": ProjectStatus.COMPLETED,
            "category": "Live Code",
            "image_filename": "livecode-monty.png",
            "description": "Live codes from tutoring sessions",
            "role": "Tutor",
            "repo_link": "https://github.com/ZeroDayPoke/evilcode",
            "skills": ["Python", "JavaScript", "Linux", "HTML", "CSS", "Flask", "SQLAlchemy", "MySQL", "C"],
        },
        {
            "name": "pokePick",
            "status": ProjectStatus.IN_PROGRESS,
            "category": "Data Science",
            "description": "First full web app; currently serves as the inventory management, order management, and order fulfillment system for my business",
            "role": "Full-stack developer",
            "repo_link": "https://github.com/ZeroDayPoke/pokePick",
            "skills": ["Python", "JavaScript", "Linux", "HTML", "CSS", "Flask", "SQLAlchemy", "MySQL"],
        },
        {
            "name": "C# Exploration",
            "status": ProjectStatus.ON_HOLD,
            "category": "C#",
            "description": "C# Exploration",
            "role": "Full-stack developer",
            "repo_link": "https://github.com/ZeroDayPoke/bleeding_edge",
            "skills": ["C#", "Linux", "MySQL"],
        },
        {
            "name": "Museum Prototype",
            "status": ProjectStatus.IN_PROGRESS,
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
            "status": ProjectStatus.COMPLETED,
            "category": "Low level Programming",
            "image_filename": "sorting.png",
            "description": "This project is a collection of various sorting algorithms and their implementation in C programming language. The goal of this project is to understand how these algorithms work and their time complexity.",
            "role": "hol-bb",
            "repo_link": "https://github.com/ZeroDayPoke/holbertonschool-sorting_algorithms",
            "skills": ["C", "Linux"],
        },
        {
            "name": "Binary Trees",
            "status": ProjectStatus.COMPLETED,
            "category": "Low level programming",
            "image_filename": "binary-trees.png",
            "description": "This repository contains the implementation of various operations on Binary Trees as part of the Holberton School curriculum.",
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
            collaborator_usernames = project_data.pop(
                'collaborators', [])  # Pop collaborators

            # Pop the category field and query for it
            category_name = project_data.pop('category', None)
            category = None
            if category_name:
                category = db.session.query(ProjectCategory).filter_by(
                    name=category_name).first()

            # Create Project object
            project = Project(**project_data)

            # Set category if found
            if category:
                project.category_id = category.id

            # Query for Skill objects that match the names in 'skills'
            related_skills = db.session.query(Skill).filter(
                Skill.name.in_(skill_names)).all()

            # Associate the queried Skill objects with the project
            project.related_skills = related_skills

            # Query for User objects that match the usernames in 'collaborators'
            collaborators = db.session.query(User).filter(
                User.username.in_(collaborator_usernames)).all()

            # Associate the queried User objects with the project
            project.collaborators = collaborators  # Assign collaborators

            # Add Project object to session
            db.session.add(project)

    # Commit the session to save all changes
    db.session.commit()
