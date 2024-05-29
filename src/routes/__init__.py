from flask import Flask


def register_routes(app: Flask):
    from .files_routes import files_routes
    from .main_route import main_route

    app.register_blueprint(files_routes)
    app.register_blueprint(main_route)