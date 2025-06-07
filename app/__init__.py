from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register Blueprints
    from .routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
