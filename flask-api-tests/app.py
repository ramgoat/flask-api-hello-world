from init.init_app import create_app
# from flask import Flask
# from routes.main import blueprint_main
# from routes.fruits import blueprint_fruit

# def create_app():
#     app = Flask(__name__)
#     app.config["JSON_SORT_KEYS"] = False

#     app.register_blueprint(blueprint_fruit)
#     app.register_blueprint(blueprint_main)

#     return app

from classes.custom_response import CustomResponse

if __name__ == '__main__':
    app = create_app()
    app.response_class = CustomResponse
    app.run()