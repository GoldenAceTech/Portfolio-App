from flask.testing import FlaskClient


def test_home(client: FlaskClient):
    response = client.get("/")
    assert b"Home | Portfolio" in response.data
    assert b"Vacation space rental app with NodeJs and MongoDB" in response.data
    assert b"Habit Tracking app with Python (Flask) and MongoDB" in response.data
    assert b"Microblog app with Python (Flask) and MongoDB" in response.data


def test_about(client: FlaskClient):
    response = client.get("/about")
    assert b"About | Portfolio" in response.data
    assert b"Hi, I'm Afolabi!" in response.data


def test_contact(client: FlaskClient):
    response = client.get("/contact")
    assert b"Contact | Portfolio" in response.data
    assert b"Email:" in response.data
    assert b"GitHub:" in response.data
    assert b"Twitter:" in response.data
