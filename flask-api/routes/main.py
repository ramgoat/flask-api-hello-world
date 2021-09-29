from flask import blueprints
from flask.json import jsonify

blueprint_main = blueprints.Blueprint('main', __name__)

@blueprint_main.route('/', methods=['GET'])
def main():
    return jsonify("Hello, World!")