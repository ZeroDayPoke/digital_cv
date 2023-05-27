#!/usr/bin/env python3
"""
run.py

This is the entry point for the Flask application. 

Located in /digital_cv/run.py
"""

from os import environ
from app import create_app, db
from flask_migrate import Migrate

app = create_app()

# Create a Migrate instance
migrate = Migrate(app, db)

def run_app():
    """ Main Function """
    host = environ.get('ZDP_HOST')
    port = environ.get('ZDP_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5555'
    app.run(host=host, port=port, threaded=True)

if __name__ == "__main__":
    run_app()
