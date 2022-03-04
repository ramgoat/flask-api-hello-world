# from flask import Flask
from classes.custom_flask import CustomFlask
from routes.fruits import blueprint_fruit
from routes.main import blueprint_main

def create_app():
    app = CustomFlask(__name__)
    app.config["JSON_SORT_KEYS"] = False

    app.register_blueprint(blueprint_fruit)
    app.register_blueprint(blueprint_main)

    return app