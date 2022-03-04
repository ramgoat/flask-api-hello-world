from flask import Flask
from flask import Response
from flask.typing import ResponseReturnValue
from flask import jsonify


class CustomFlask(Flask):

    def make_response(self, rv: ResponseReturnValue) -> Response:

        if isinstance(rv, dict):

            rv = jsonify({"data": rv})
        return super().make_response(rv)