from flask import Flask, render_template, request, send_from_directory, redirect, url_for, send_file, jsonify
import os
import sys
from urllib.parse import unquote


app = Flask(__name__)

root_dir = os.path.dirname(os.path.abspath(__file__))

# Unir la ruta absoluta con el directorio "src/uploads"
upload_folder = os.path.join(root_dir, 'uploads')

# Asignar la ruta absoluta a la configuración
app.config['UPLOAD_FOLDER'] = upload_folder

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():

    if 'file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(url_for('index'))

    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    # Suponiendo que los archivos están en una carpeta llamada "archivos"
    file_path = f"{app.config['UPLOAD_FOLDER']}/{filename}"
    return send_file(file_path, as_attachment=True)

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    filename = unquote(filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if os.path.exists(file_path):
        os.remove(file_path)

    return redirect(url_for('index'))