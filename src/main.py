import os
from flask import Flask
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    root_dir = os.path.dirname(os.path.abspath(__file__))
    upload_folder = os.path.join(root_dir, 'uploads')
    app.config['UPLOAD_FOLDER'] = upload_folder
    register_routes(app)

    return app