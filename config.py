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
    ALLOWED_EXTENSIONS = os.getenv('ALLOWED_EXTENSIONS', 'png,jpg,jpeg,gif'.split(','))
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'app/static/images')
    MAX_FILE_SIZE = os.getenv('MAX_FILE_SIZE', 1572864)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')


    LANGUAGES = ["en", "es"]
    BABEL_DEFAULT_LOCALE = "es"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_TRANSLATION_DIRECTORIES = os.path.join(os.getcwd(), 'translations')

class DevelopmentConfig(Config):
    DB_USER = os.getenv('DB_USER', 'cv_user_dev')
    DB_PASS = os.getenv('DB_PASS', 'pass_cv_dev')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'cv_db_dev')
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', True)

class TestingConfig(Config):
    TESTING = True
    DB_USER = os.getenv('DB_USER', 'cv_user_test')
    DB_PASS = os.getenv('DB_PASS', 'pass_cv_test')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'cv_db_test')
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    DB_USER = os.getenv('DB_USER', 'cv_user_prod')
    DB_PASS = os.getenv('DB_PASS', 'pass_cv_prod')
    DB_HOST = os.getenv('DB_HOST', 'db')
    DB_NAME = os.getenv('DB_NAME', 'cv_db_prod')
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', False)

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
