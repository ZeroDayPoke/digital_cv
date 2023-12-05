# app/routes/services_routes.py

from flask import render_template, request, Blueprint, jsonify
from ..models import Service
from ..forms.form_utils import create_dynamic_filter_form
from .route_utils import generate_filters

services_routes = Blueprint('services_routes', __name__, url_prefix='')

@services_routes.route('/services', methods=['GET'])
def services():
    # Create a dynamic form based on the Service model
    DynamicServiceForm = create_dynamic_filter_form(
        Service,
        excluded_fields=['note', 'description'],
        select_fields=['category', 'currency', 'duration'],
        range_fields=['price']
    )

    form = DynamicServiceForm(request.args)
    form.set_sort_choices(fields=['price'])

    if request.args.get('ajax'):
        # Generate filters from the form
        filters = generate_filters(form, range_fields={'price'})

        # Get pagination information
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)

        # Apply filters and paginate
        pagination = Service.get_filtered(filters, page, per_page)
        services = pagination.items

        # Return JSON response
        return jsonify({'services': [service.to_dict() for service in services]})

    # Render the template with the form
    return render_template('services/main.html', title='Services', form=form)
