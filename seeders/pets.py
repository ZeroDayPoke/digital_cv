# ./seeders/pets.py

from app.models import Pet
from app import db

def seed_pets():
    """Seed the pets table with data"""
    pets = [
        {
            "name": "Fluffy",
            "breed": "Maine Coon",
            "description": "Amazing",
            "is_featured": True,
            "images": [
                {"filename": "fluffy1.jpg", "description": "fluffy is awesome"},
                {"filename": "fluffy2.jpg", "description": "so awesome"},
                {"filename": "fluffy3.jpg", "description": "truly da best"}
                 
            ]
        }
    ]

    # Query existing pets to prevent duplicates
    existing_pets = db.session.query(Pet.name, Pet.breed).all()

    for pet_data in pets:
        # Convert each dictionary to a tuple of (name, breed)
        check_tuple = (pet_data['name'], pet_data['breed'])

        if check_tuple not in existing_pets:
            # Create Pet object
            pet = Pet(**pet_data)

            # Add Pet object to session
            db.session.add(pet)

    # Commit the session to save all changes
    db.session.commit()
