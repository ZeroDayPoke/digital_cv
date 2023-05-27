# app/routes/main.py
from flask import Blueprint

main_routes = Blueprint('main_routes', __name__, url_prefix='')

@main_routes.route('/')
def index():
    return "Hello, world!"
