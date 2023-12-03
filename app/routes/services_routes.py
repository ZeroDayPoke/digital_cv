#!/usr/bin/env python3
"""
services_routes.py - services routes for the Flask application
"""

from flask import render_template, request, Blueprint, current_app, redirect, url_for, jsonify, flash
from flask_login import login_required, current_user

from .route_utils.decorators import admin_required
from ..models import Project, Skill, Blog, Message, db, Service

services_routes = Blueprint('services_routes', __name__, url_prefix='')

@services_routes.route('/services', methods=['GET'])
def services():
    if request.args.get('ajax'):
        filters = {
            'boolean': [],
            'range': [],
            'string': [],
            'sort': []
        }

        if request.args.get('is_available') is not None:
            filters['boolean'].append(('is_available', request.args.get('is_available', type=bool)))

        if request.args.get('early_eligible') is not None:
            filters['boolean'].append(('early_eligible', request.args.get('early_eligible', type=bool)))

        if request.args.get('min_price') or request.args.get('max_price'):
            filters['range'].append(('price', request.args.get('min_price', type=float, default=None), request.args.get('max_price', type=float, default=None)))

        if request.args.get('category'):
            filters['string'].append(('category', request.args.get('category')))

        if request.args.get('sort_order'):
            filters['sort'].append(('price', request.args.get('sort_order')))

        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        pagination = Service.get_filtered(filters, page, per_page)
        services = pagination.items
        return jsonify({'services': [service.to_dict() for service in services]})
    
    return render_template('services/main.html', title='Services')
