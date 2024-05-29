from urllib.parse import unquote
import os
from flask import (Blueprint, 
                   request,  
                   redirect, 
                   url_for, 
                   send_file, 
                   jsonify,
                   current_app)

files_routes = Blueprint("files_routes", __name__)


@files_routes.route('/upload', methods=['POST'])
def upload_file():

    if 'file' not in request.files:
        return redirect(url_for('main_route.index'))
    
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('main_route.index'))

    if file:
        file.save(os.path.join(
                                current_app.config['UPLOAD_FOLDER'], 
                                file.filename)
                              )
        
        return redirect(url_for('main_route.index'))


@files_routes.route('/download/<filename>')
def download_file(filename):
    file_path = f"{current_app.config['UPLOAD_FOLDER']}/{filename}"
    return send_file(file_path, as_attachment=True)


@files_routes.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    filename = unquote(filename)
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    
    if os.path.exists(file_path):
        os.remove(file_path)

    return redirect(url_for('main_route.index'))