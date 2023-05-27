#!/usr/bin/env python3
"""
main.py - main routes for the Flask application
"""
# app/routes/main.py

from flask import Blueprint, render_template

main_routes = Blueprint('main_routes', __name__, url_prefix='')

@main_routes.route('/')
def index():
    return render_template('index.html')
