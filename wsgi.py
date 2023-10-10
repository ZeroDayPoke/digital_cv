#!/usr/bin/env python3
"""
wsgi.py

This is the entry point for the WSGI server.

Located in /digital_cv/wsgi.py
"""

import sys
sys.dont_write_bytecode = True

from flask_migrate import Migrate
from app import create_app, db

app = create_app(config_name='production')

# Create a Migrate instance
migrate = Migrate(app, db)

with app.app_context():
    from sqlalchemy import MetaData

    metadata = MetaData()
    metadata.reflect(bind=db.engine)

    if not metadata.tables:
        db.create_all()
        print("Created tables")
        from seeder import seed_all
        seed_all()
    else:
        print("Tables already exist")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000', threaded=True)
