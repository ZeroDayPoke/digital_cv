import os
from werkzeug.utils import secure_filename
from flask import request, current_app

def allowed_file(filename):
    allowed_extensions = current_app.config['ALLOWED_EXTENSIONS']
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def handle_file_upload(model_name):
    file = request.files.get('image')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        
        # Construct upload folder dynamically using model_name
        upload_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], model_name)

        # Create the directory if it doesn't exist.
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
            
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return filename
    return None
