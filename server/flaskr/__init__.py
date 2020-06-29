import os

from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    from . import db, route
    route.init_app(app)
    return app
