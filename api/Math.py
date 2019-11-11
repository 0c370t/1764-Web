from flask_restplus import Namespace, Resource
from flask import request

api = Namespace("Math", url_prefix="/math")


@api.route("/Addition")
@api.doc(description="Adds two numbers together",
         responses={200: "X + Y", 500: "Internal Server Error", 403: "Not Authorized"})
@api.param("X", type=int, required=True)
@api.param("Y", type=int, required=True)
class TestClass(Resource):
    def get(self):
        x = int(request.args["X"])
        y = int(request.args["Y"])
        return x + y
