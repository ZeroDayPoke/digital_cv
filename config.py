#!/usr/bin/env python3
"""
config.py - Configuration file for the app
"""
# Path: digital_cv/config.py

import os
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

import os

class Config:
    """
    Configuration class for the Flask app.

    Attributes:
    - ALLOWED_EXTENSIONS (list): List of allowed file extensions for file uploads.
    - UPLOAD_FOLDER (str): Path to the folder where uploaded files will be stored.
    - MAX_FILE_SIZE (int): Maximum allowed file size for uploads, in bytes.
    - SQLALCHEMY_TRACK_MODIFICATIONS (bool): Flag to disable Flask-SQLAlchemy
        modification tracking.
    - SECRET_KEY (str): Secret key used for session management.
    - LANGUAGES (list): List of supported languages.
    - BABEL_DEFAULT_LOCALE (str): Default language for translations.
    - BABEL_DEFAULT_TIMEZONE (str): Default timezone for translations.
    - BABEL_TRANSLATION_DIRECTORIES (str): Path to the directory containing translation files.
    - CV_UPLOAD_FOLDER (str): Path to the folder where CVs will be stored.
    - USE_EXTENDED_BOOTSTRAP (bool): Flag to enable/disable extended Bootstrap.
    """
    ALLOWED_EXTENSIONS = os.getenv('ALLOWED_EXTENSIONS', 'png,jpg,jpeg,gif'.split(','))
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'app/static/images')
    MAX_FILE_SIZE = os.getenv('MAX_FILE_SIZE', 1572864)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')
    LANGUAGES = ["en", "es"]
    BABEL_DEFAULT_LOCALE = "es"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_TRANSLATION_DIRECTORIES = os.path.join(os.getcwd(), 'translations')
    CV_UPLOAD_FOLDER = os.getenv('CV_UPLOAD_FOLDER', 'app/static/cv/')
    DOMAIN_NAME = os.getenv('DOMAIN_NAME', 'http://localhost:8000')
    CV_PDF_NAME = os.getenv('CV_PDF_NAME', 'resume_draft_v2.pdf')
    USE_EXTENDED_BOOTSTRAP = os.getenv('USE_EXTENDED_BOOTSTRAP', True)

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
