from flask import Blueprint, render_template, abort

bp = Blueprint("projects", __name__, url_prefix="/projects")

projects = {
    "vacation-rental": {
        "name": "Modern Stays - vacation space rental App",
        "hero": "img/vacation-rental-hero.jpg",
        "technologies": ["NodeJS", "Typescript", "HTML", "CSS"],
        "prod": "https://modern-stay.herokuapp.com/",
    },
    "habit-tracker": {
        "name": "Habit Tracking App",
        "thumb": "img/habit-tracker.jpg",
        "hero": "img/habit-tracker-hero.jpg",
        "technologies": ["Python", "HTML", "CSS"],
        "prod": "https://ace-habit-tracker-app.herokuapp.com/",
    },
    "microblog": {
        "name": "Microblog App",
        "thumb": "img/microblog.jpg",
        "hero": "img/microblog-hero.jpg",
        "technologies": ["Python", "HTML", "CSS"],
        "prod": "https://ace-microblog-app.herokuapp.com/",
    },
    "movie-watchlist": {
        "name": "Movie Watchlist App",
        "thumb": "img/movie-watchlist.jpg",
        "hero": "img/movie-watchlist-hero.jpg",
        "technologies": ["Python", "HTML", "CSS", "PostgreSQL"],
        "prod": "https://ace-movie-watchlist.herokuapp.com/",
    },
}


@bp.route("/<string:slug>")
def project(slug):
    if slug not in projects:
        abort(404)
    project = projects[slug]
    return render_template(f"pages/projects/{slug}.html", title=f"{slug}", project=project)
