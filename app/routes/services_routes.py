#!/usr/bin/env python3
"""
services_routes.py - services routes for the Flask application
"""

from wtforms import BooleanField, FloatField, StringField, SelectField
from flask import render_template, request, Blueprint, jsonify
from ..models import Service
from ..forms.form_utils import setup_range_filter
from ..forms.service_forms import ServiceFilterForm, create_dynamic_service_form

services_routes = Blueprint('services_routes', __name__, url_prefix='')

@services_routes.route('/services', methods=['GET'])
def services():
    DynamicServiceForm = create_dynamic_service_form(excluded_fields=['note', 'description'])
    form = DynamicServiceForm(request.args)
    form.set_sort_choices(fields=['price'])

    if request.args.get('ajax'):
        filters = {
            'boolean': [],
            'range': [],
            'string': [],
            'sort': []
        }

        range_fields = set()

        for field_name, field in form.__dict__.items():
            if '_min' in field_name or '_max' in field_name:
                base_field_name = field_name.rsplit('_', 1)[0]
                range_fields.add(base_field_name)

        for base_field_name in range_fields:
            min_val, max_val = setup_range_filter(form, base_field_name)
            filters['range'].append((base_field_name, min_val, max_val))

        for field_name, field in form.__dict__.items():
            if isinstance(field, BooleanField):
                if field.data is not None and field.data is not False:
                    filters['boolean'].append((field_name, field.data))
            elif isinstance(field, StringField):
                if field.data:
                    filters['string'].append((field_name, field.data))
            elif isinstance(field, SelectField) and field_name not in ['sort_by', 'order']:
                if field.data:
                    filters['string'].append((field_name, field.data))

        if form.sort_by.data:
            filters['sort'].append((form.sort_by.data, form.order.data))

        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        pagination = Service.get_filtered(filters, page, per_page)
        services = pagination.items
        return jsonify({'services': [service.to_dict() for service in services]})

    return render_template('services/main.html', title='Services', form=form)


@services_routes.route('/services/filters', methods=['GET'])
def get_service_filters():
    categories = Service.query.with_entities(Service.category).distinct().all()
    durations = Service.query.with_entities(Service.duration).distinct().all()
    return jsonify({
        'categories': [category[0] for category in categories if category[0]],
        'durations': [duration[0] for duration in durations if duration[0]]
    })
