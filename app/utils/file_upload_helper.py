# app/utils/file_upload_helper.py

import os
from werkzeug.utils import secure_filename
from flask import request, current_app, flash

def allowed_file(filename):
    allowed_extensions = current_app.config['ALLOWED_EXTENSIONS']
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def handle_file_upload(model_name):
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
