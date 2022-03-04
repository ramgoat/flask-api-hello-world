from flask import blueprints
from flask.json import jsonify
from flask import Response
from classes.custom_response import CustomResponse

blueprint_main = blueprints.Blueprint('main', __name__)

@blueprint_main.route('/', methods=['GET'])
def main():
    # return jsonify("Hello, World!")
    # return "Hello, World! I've bypassed jsonify()!!!!!!!"
    
    return {"Hi": "there"}