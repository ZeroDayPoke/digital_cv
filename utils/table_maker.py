#!/usr/bin/env python3
"""
Table maker for the digital_cv database.

Located in /digital_cv/utils/table_maker.py
"""

from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()
