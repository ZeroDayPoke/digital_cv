# app/utils/file_upload_helper.py

import os
from werkzeug.utils import secure_filename
from flask import request, current_app, flash

def allowed_file(filename):
    """
    Check if the given filename has an allowed extension.
    Args:
        filename (str): The name of the file to check.
    Returns:
        bool: True if the file has an allowed extension, False otherwise.
    """
    allowed_extensions = current_app.config['ALLOWED_EXTENSIONS']
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def handle_file_upload(model_name, field_name='image'):
    file = request.files.get(field_name)

    if not file or file.filename == '':
        return None

    if allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], model_name)

        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return filename

    flash('Error: Invalid file extension.', 'danger')
    return None

def handle_file_upload_alt(model_name, file):
    if not file or file.filename == '':
        return None

    if allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], model_name)

        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return filename

    flash('Error: Invalid file extension.', 'danger')
    return None
