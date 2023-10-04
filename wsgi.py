#!/usr/bin/env python3
"""
wsgi.py

This is the entry point for the WSGI server.

Located in /digital_cv/wsgi.py
"""

from .app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8000', threaded=True)
