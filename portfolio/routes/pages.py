from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

projects = [
    {
        "name": "Vacation space rental app with NodeJs and MongoDB",
        "thumb": "img/vacation-rental.jpg",
        "categories": ["NodeJs", "Typescript", "MongoDB"],
        "slug": "vacation-rental",
    },
    {
        "name": "Habit Tracking app with Python (Flask) and MongoDB",
        "thumb": "img/habit-tracker.jpg",
        "categories": ["Python", "Flask", "Web","MongoDB"],
        "slug": "habit-tracker",
    },
    {
        "name": "Microblog app with Python (Flask) and MongoDB",
        "thumb": "img/microblog.jpg",
        "categories": ["Python", "Flask", "Web", "MongoDB"],
        "slug": "microblog",
    },
    {
        "name": "Movie watchlist app with Python (Flask) and PostgreSQL",
        "thumb": "img/movie-watchlist.jpg",
        "categories": ["Python", "Flask", "Web", "PostgreSQL"],
        "slug": "movie-watchlist",
    },
]

slug_to_project = {project["slug"]: num for num, project in enumerate(projects)}


@bp.route("/")
@bp.route("/projects")
def home():
    return render_template("pages/index.html", title="Home", projects=projects)


@bp.route("/about")
def about():
    return render_template("pages/about.html", title="About")


@bp.route("/contact")
def contact():
    return render_template("pages/contact.html", title="Contact")
