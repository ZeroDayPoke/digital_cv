# ./seeders/tutorials.py

from app.models import Tutorial
from app import db

def seed_tutorials():
    """Seed the tutorials table"""
    tutorials = [
        {"name": "Flask Tutorial", "description": "A tutorial on Flask.", "content_file": "tutorial", "image_filename": "notfound4.png"},
    ]
    
    # Query existing tutorials to prevent duplicates
    existing_tutorials = [t.name for t in db.session.query(Tutorial.name).all()]
    
    for tutorial_data in tutorials:
        if tutorial_data["name"] not in existing_tutorials:
            tutorial = Tutorial(**tutorial_data)
            db.session.add(tutorial)
    
    db.session.commit()
