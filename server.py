from flask import Flask, request
from flask_cors import CORS
import json

from response import Response

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/python-api/add", methods=["post"])
def addHandle():
    recv = json.loads(request.get_data())
    try:
        a = float(recv["a"])
        b = float(recv["b"])
        c = a + b
        response = Response(20000, c).success()
    except Exception as e:
        response = Response(30001, str(e)).fail()
    return response


if __name__ == "__main__":
    app.run("127.0.0.1", 9091)
