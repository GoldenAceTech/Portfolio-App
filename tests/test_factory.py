from flask import Flask
from flask.testing import FlaskClient
from portfolio import create_app


def test_config(app: Flask) -> None:
    """Testing the app Configurations

    Args:
        app (Flask): The test flask app
    """
    assert not create_app().testing
    assert app.testing

def test_hello(client: FlaskClient) -> None:
    """Testing the flask client

    Args:
        client (FlaskClient): The test flask client
    """
    response = client.get('/hello')
    assert b'Hello, World!' in response.data