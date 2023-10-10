#!/usr/bin/env python3
"""
run.py

This is the entry point for the Flask application. 

Located in /digital_cv/run.py
"""

from os import environ
from app import create_app, db
from flask_migrate import Migrate

app = create_app(config_name=environ.get('FLASK_ENV') or 'development')

# Create a Migrate instance
migrate = Migrate(app, db)

def run_app():
    """ Main Function """
    host = environ.get('ZDP_HOST')
    port = environ.get('ZDP_PORT')
    if not host:
        host = '127.0.0.1'
    if not port:
        port = '5200'
    app.run(host=host, port=port, threaded=True, debug=True)

if __name__ == "__main__":
    run_app()
