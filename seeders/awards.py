# ./seeders/awards.py

from app.models import Award
from app import db

def seed_awards():
    """Seed the awards table with data"""
    awards = [
        {
            "name": "Scott Noble Deisgn Competition Winner",
            "issuer": "Oklahoma State University",
        },
        {
            "name": "Student of the Month",
            "issuer": "Holberton Tulsa",
        }
    ]

    # Query existing awards to prevent duplicates
    existing_awards = db.session.query(Award.name, Award.issuer).all()

    for award_data in awards:
        # Convert each dictionary to a tuple of (name, issuer)
        check_tuple = (award_data['name'], award_data['issuer'])

        if check_tuple not in existing_awards:
            # Create Award object
            award = Award(**award_data)

            # Add Award object to session
            db.session.add(award)

    # Commit the session to save all changes
    db.session.commit()
