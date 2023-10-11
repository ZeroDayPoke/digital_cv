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

def handle_file_upload(model_name):
    """
    Handles file upload for a given model.

    Args:
        model_name (str): The name of the model to upload the file for.

    Returns:
        str: The filename of the uploaded file if successful, None otherwise.
    """
    print("Handling file upload...")
    file = request.files.get('image')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        
        upload_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], model_name)

        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
            
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return filename
    flash('Error: File not found or not allowed.', 'danger')
    return None
