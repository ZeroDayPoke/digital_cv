# ./seeders/pets.py

from app.models import Pet, Image
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
                {"filename": "fluffy1.jpg", "description": "test1"},
                {"filename": "fluffy2.jpg", "description": "test2"},
                {"filename": "fluffy3.jpg", "description": "test3"}
            ]
        }
    ]

    for pet_data in pets:
        pet = Pet.query.filter_by(name=pet_data['name'], breed=pet_data['breed']).first()
        if not pet:
            pet = Pet(name=pet_data['name'], breed=pet_data['breed'],
                      description=pet_data['description'], is_featured=pet_data['is_featured'])
            db.session.add(pet)
            db.session.flush()

            for image_data in pet_data['images']:
                image = Image(owner_id=pet.id, owner_type='pets', filename=image_data['filename'], description=image_data['description'])
                db.session.add(image)

    db.session.commit()
