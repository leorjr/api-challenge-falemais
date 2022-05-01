import json
from flask import Flask
from dotenv import load_dotenv
from app.controlles import home_controller

load_dotenv()


def create_app():
    app = Flask(__name__)

    home_controller.init_app(app)

    return app
