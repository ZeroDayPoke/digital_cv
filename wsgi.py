#!/usr/bin/env python3
"""
wsgi.py

This is the entry point for the WSGI server.

Located in /digital_cv/wsgi.py

This script creates a Flask app instance and runs it using a WSGI server.
It also creates a Migrate instance for database migrations and initializes the database tables.
"""

import os
import sys
sys.dont_write_bytecode = True

from flask_migrate import Migrate
from app import create_app, db

app = create_app(config_name=os.getenv('FLASK_APP_ENV'))

# Create a Migrate instance
migrate = Migrate(app, db)

with app.app_context():
    # Reflect existing tables
    from sqlalchemy import MetaData
    metadata = MetaData()
    metadata.reflect(bind=db.engine)

    # Create tables if they do not exist
    if not metadata.tables:
        db.create_all()

    # Seed database tables
    from seeder import seed_all
    seed_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000', threaded=True)
