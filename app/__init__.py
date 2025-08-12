from flask import Flask
from flask_cors import CORS
from .config import Config
from .routes import bp

def create_app():
    #app = Flask(__name__, static_folder="static")
    app = Flask(__name__, template_folder='static')
    app.config.from_object(Config)
    CORS(app)
    app.register_blueprint(bp)
    return app
