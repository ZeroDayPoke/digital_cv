#!/usr/bin/env python3

from flask import Flask, g, request


def get_locale(app: Flask) -> str:
    """
    Determine the best locale to use for translations.

    Args:
        app (Flask): The current Flask application instance.

    Returns:
        str: Locale code.
    """
    requested_locale = request.args.get('locale')
    if requested_locale in app.config['LANGUAGES']:
        return requested_locale

    user = g.get('user', None)
    if user:
        user_locale = user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    if best_match:
        return best_match

    return app.config['BABEL_DEFAULT_LOCALE']
