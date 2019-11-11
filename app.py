from flask import Flask
from flask_restplus import Api, Resource
from api import math_api

application = Flask(__name__)
api = Api(application, title="1764 Scouting", version="", default="Default Namespace", ordered=True,
          contact="contact@noimbrian.com")

api.add_namespace(math_api)
