from flask import jsonify


class Response:
    def __init__(self, code=0, data=None):
        self.code = code
        self.data = data

    def success(self):
        response = {
            "code": self.code,
            "data": self.data
        }
        return jsonify(response)

    def fail(self):
        response = {
            "code": self.code,
            "message": self.data
        }
        return jsonify(response)