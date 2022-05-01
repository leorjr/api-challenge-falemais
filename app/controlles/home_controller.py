from flask import Flask, jsonify
from app.utils import functions


def init_app(app: Flask):

    @app.get("/")
    def home():
        data = functions.load_db()

        return data

    @app.get("/planos")
    def get_planos():
        data = functions.load_db()

        return jsonify(data["planos"])

    @app.get("/tarifacao")
    def get_tarifacao():
        data = functions.load_db()

        return jsonify(data["tarifacao"])
