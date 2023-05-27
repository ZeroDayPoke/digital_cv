#!/usr/bin/env python3
"""
run.py

This is the entry point for the Flask application. 

Located in /digital_cv/run.py
"""

from app import create_app, db
from flask_migrate import Migrate

app = create_app()

# Create a Migrate instance
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
