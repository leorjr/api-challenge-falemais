from flask import Flask
from app.utils import functions


def init_app(app: Flask):

    @app.get("/")
    def home():

        data = functions.load_db()

        return data

    return app
