"""Init file, load the configuration and default methods used in the API"""

import os
from flask import Flask, json
from werkzeug.exceptions import HTTPException

from . import views

def create_app(test_config=None):
    """Create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ['API_KEY'],
    )
    # In case of config.py file
    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    app.register_blueprint(views.bp)

    # Generic Error Handler for application/json data
    @app.errorhandler(HTTPException)
    def handle_exception(error):
        # Start with the correct headers and status code from the error
        response = error.get_response()
        # Replace the body with JSON
        response.data = json.dumps({
            "code": error.code,
            "name": error.name,
            "description": error.description,
        })
        response.content_type = "application/json"
        return response

    return app

app = create_app()
