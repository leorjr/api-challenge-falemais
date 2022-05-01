from flask import Flask
from app.utils import functions
from app.controlles import home_controller


def init_app(app: Flask):

    @app.get("/")
    def home():
        return home_controller.get_all_informations()

    @app.get("/plans")
    def get_plans():
        return home_controller.get_plans()

    @app.get("/pricing")
    def get_pricing():
        return home_controller.get_pricing()

    @app.post("/calculate-pricing")
    def calculate():
        return home_controller.calculate()

    return app
