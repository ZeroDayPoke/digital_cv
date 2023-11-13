# Path: app/routes/route_utils/decorators.py

from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.has_role('ADMIN'):
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('main_routes.index'))
        return f(*args, **kwargs)
    return decorated_function
