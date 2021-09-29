from flask import blueprints, jsonify

blueprint_fruit = blueprints.Blueprint("fruits", __name__, url_prefix='/fruits')

fruit = ["banana", "pear", "orange"]

@blueprint_fruit.route('', methods=['GET'])
def getAll():
    response = {"fruits": fruit}

    return jsonify(response)