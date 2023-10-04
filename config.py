#!/usr/bin/env python3
"""
config.py - Configuration file for the app
"""
# Path: digital_cv/config.py

import os
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'supersecretkey'
    DB_USER = os.getenv('DB_USER', 'cv_user')
    DB_PASS = os.getenv('DB_PASS', 'pass_cv')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'cv_db')
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    LANGUAGES = ["en", "es"]
    BABEL_DEFAULT_LOCALE = "es"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Set the development configuration
class DevelopmentConfig(Config):
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', True)

# Set the production configuration
class ProductionConfig(Config):
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', False)

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
