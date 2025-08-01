from flask import Flask
from src.assets.config import Config
from src.main.blueprints.home import home_bp


def create_app():
    
    app = Flask(__name__, template_folder=Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
    
    app.register_blueprint(home_bp)

    return app