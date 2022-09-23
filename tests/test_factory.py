"""test the configuration and the app is able to start"""


from flask_sort import create_app


def test_config():
    """Create the app"""
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing
