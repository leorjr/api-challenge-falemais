from flask import Flask
from app.controlles.home_controller import HomeController


def init_app(app: Flask):

    @app.get("/")
    def home():
        return HomeController.get_all_informations()

    @app.get("/plans")
    def get_plans():
        return HomeController.get_plans()

    @app.get("/pricing")
    def get_pricing():
        return HomeController.get_pricing()

    @app.post("/calculate-pricing")
    def calculate():
        return HomeController.calculate()

    return app
