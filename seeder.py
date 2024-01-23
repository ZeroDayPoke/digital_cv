# ./seeder.py

import os
from seeders import seed_all
from app import create_app

app = create_app(os.getenv("FLASK_APP_ENV") or "default")

with app.app_context():
    seed_all()
