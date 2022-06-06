from datetime import datetime
from flask import Blueprint, render_template

bp = Blueprint('pages', __name__)

projects = [
    {
        "name": "Vacation space rental app with NodeJs and MongoDB",
        "thumb": "img/vacation-rental.jpg",
        "hero": "img/vacation-rental-hero.jpg",
        "categories": ["NodeJs", "Javascript"],
        "slug": "vacation-rental",
        "prod": "https://modern-stay.herokuapp.com/",
    },
    {
        "name": "Habit Tracking app with Python (Flask) and MongoDB",
        "thumb": "img/habit-tracker.jpg",
        "hero": "img/habit-tracker-hero.jpg",
        "categories": ["Python", "Flask", "Web"],
        "slug": "habit-tracker",
        "prod": "https://ace-habit-tracker-app.herokuapp.com/",
    },
    {
        "name": "Microblog app with Python (Flask) and MongoDB",
        "thumb": "img/microblog.jpg",
        "hero": "img/microblog-hero.jpg",
        "categories": ["Python", "Flask", "Web"],
        "slug": "microblog",
        "prod": "https://ace-microblog-app.herokuapp.com/",
    },
]

@bp.route('/')
def home():
    return render_template('pages/index.html', title='Home', projects=projects)

@bp.route('/about')
def about():
    return render_template('pages/about.html', title='About')

@bp.route('/contact')
def contact():
    return render_template('pages/contact.html', title='Contact')

@bp.context_processor
def inject_current_year():
    return {"year": datetime.now().year}