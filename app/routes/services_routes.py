#!/usr/bin/env python3
"""
services_routes.py - services routes for the Flask application
"""

from flask import render_template, request, Blueprint, current_app, redirect, url_for, jsonify, flash
from flask_login import login_required, current_user

from .route_utils.decorators import admin_required
from ..models import Project, Skill, Blog, Message, db

services_routes = Blueprint('services_routes', __name__, url_prefix='')

@services_routes.route('/services', methods=['GET'])
def services():
    return render_template('services/main.html', title='Services')
