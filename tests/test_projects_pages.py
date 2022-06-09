from flask.testing import FlaskClient

def test_vacation_rental(client: FlaskClient):
    """Testing the vacation rental description page"""

    response = client.get('/projects/vacation-rental')
    assert b"img/vacation-rental-hero.jpg" in response.data
    assert b"https://modern-stay.herokuapp.com/" in response.data
    assert b"NodeJS" in response.data
    assert b"Modern Stays" in response.data

def test_habit_tracker(client: FlaskClient):
    """Testing the vacation rental description page"""

    response = client.get('/projects/habit-tracker')
    assert b"img/habit-tracker-hero.jpg" in response.data
    assert b"https://ace-habit-tracker-app.herokuapp.com/" in response.data
    assert b"Python" in response.data
    assert b"Habit Tracking App" in response.data

def test_microblog(client: FlaskClient):
    """Testing the vacation rental description page"""

    response = client.get('/projects/microblog')
    assert b"img/microblog-hero.jpg" in response.data
    assert b"https://ace-microblog-app.herokuapp.com/" in response.data
    assert b"Python" in response.data
    assert b"Microblog" in response.data