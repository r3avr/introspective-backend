from flask import Flask
from app.routes import main  # This is importing the actual Blueprint object

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app
