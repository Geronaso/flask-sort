"""Test file for default config"""

import pytest
from flask_sort import create_app

@pytest.fixture
def app_sort():
    """calls the app to use instead of using the local development app"""
    app = create_app()
    return app

@pytest.fixture
def client(app_sort):
    """Creates a client for tests"""
    return app_sort.test_client()
