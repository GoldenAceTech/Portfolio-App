from typing import Generator
import pytest
from portfolio import create_app
from flask import Flask
from flask.testing import FlaskClient


@pytest.fixture
def app() -> Generator[Flask, None, None]:
    """Get the flask app with test configurations

    Yields:
        Generator[Flask, None, None]: Flask app
    """
    app = create_app({"TESTING": True})
    yield app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """creates a test client for the application

    Args:
        app (Flask): The app Flask object

    Returns:
        FlaskClient: A flask test client that works like the app but for testing
    """
    with app.test_client() as client:
        with app.app_context():
            yield client
