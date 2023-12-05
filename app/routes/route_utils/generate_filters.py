# utils/filter_utils.py

from wtforms import BooleanField, StringField, SelectField


def generate_filters(form, range_fields=None):
    """
    Generate filters based on the provided form and range fields.

    Args:
        form (Form): The form object containing the fields.
        range_fields (set, optional): Set of range field names. Defaults to None.

    Returns:
        dict: A dictionary containing the generated filters categorized by type.
            The dictionary has the following structure:
            {
                'boolean': [(field_name, field_value), ...],
                'range': [(field_name, min_value, max_value), ...],
                'string': [(field_name, field_value), ...],
                'sort': [(sort_by_field, order_field)]
            }
    """

    filters = {
        'boolean': [],
        'range': [],
        'string': [],
        'sort': []
    }

    if range_fields is None:
        range_fields = set()

    # Identify range fields
    for field_name, field in form.__dict__.items():
        if '_min' in field_name or '_max' in field_name:
            base_field_name = field_name.rsplit('_', 1)[0]
            range_fields.add(base_field_name)

    # Process range fields
    for base_field_name in range_fields:
        min_field = getattr(form, f"{base_field_name}_min", None)
        max_field = getattr(form, f"{base_field_name}_max", None)
        min_val = min_field.data if min_field and min_field.data is not None else 0
        max_val = max_field.data if max_field and max_field.data is not None else 999999999
        filters['range'].append((base_field_name, min_val, max_val))

    # Process other fields, excluding 'sort_by' and 'order'
    for field_name, field in form.__dict__.items():
        if field_name in [f"{base}_min" for base in range_fields] or field_name in [f"{base}_max" for base in range_fields] or field_name in ['sort_by', 'order']:
            continue

        if isinstance(field, BooleanField):
            if field.data is not None and field.data is not False:
                filters['boolean'].append((field_name, field.data))
        elif isinstance(field, StringField) or isinstance(field, SelectField):
            if field.data:
                filters['string'].append((field_name, field.data))

    # Process sorting fields
    if form.sort_by.data:
        filters['sort'].append((form.sort_by.data, form.order.data))

    return filters
