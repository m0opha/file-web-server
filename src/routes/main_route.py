from flask import Blueprint, current_app, render_template
import os

main_route = Blueprint("main_route",__name__)

@main_route.route('/')
def index():
    files = os.listdir(current_app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)
