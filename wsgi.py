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

app = create_app()

# Create a Migrate instance
migrate = Migrate(app, db)

with app.app_context():
    total = db.create_all()
    if total:
        print(f"Created {total} tables")
        from seeder import seed_all
    else:
        print("No tables created")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000', threaded=True)
