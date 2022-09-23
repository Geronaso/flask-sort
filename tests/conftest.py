"""Create some configurations used in the tests files"""

import pytest
from flask_sort import create_app

@pytest.fixture
def app_sort():
    """calls the app to use instead of using the local development app"""
    app = create_app()
    yield app

@pytest.fixture
def client():
    """Creates a client for tests"""
    app = create_app()
    return app.test_client()
