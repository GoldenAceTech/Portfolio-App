from flask import Blueprint, render_template, abort

bp = Blueprint("projects", __name__, url_prefix="/projects")

projects = {
    "vacation-rental": {
        "name": "Modern Stays - vacation space rental App",
        "hero": "img/vacation-rental-hero.jpg",
        "technologies": ["NodeJS", "Typescript", "HTML", "CSS"],
        "prod": "https://modern-stay.herokuapp.com/",
        "description": [
            "Modern Stays is an online vaction rental space where users can book a place to stay in their desired location for the number of days they want. It has a well designed form and a calendar where users can search for a location and select their check in and check out days, then the page will return a list of stays that are available for the desired days selected where the users can choose from.", "The web app was mainly written in typescript, built with NodeJs and MongoDb for the backend. Other dependencies include ExpressJs to help manage servers and routes, Ejs as the template engine, Passport for the authentication, Mapbox to show stay locations on the map, Helmet etc.", "It was a very interesting app to build for me as this was my first real app that I built from scratch all by myself. There were a lot of challenges but I learned a lot from building this app and it helpedme develop my skill even more. The main challenge I will say was designing the app especially building the calendar from scratch, other than that the backend work were less complicated for me."
        ]
    },
    "habit-tracker": {
        "name": "Habit Tracking App",
        "thumb": "img/habit-tracker.jpg",
        "hero": "img/habit-tracker-hero.jpg",
        "technologies": ["Python", "HTML", "CSS"],
        "prod": "https://ace-habit-tracker-app.herokuapp.com/",
        "description": [
            "The habit tracking app is a web app where users can save daily habits or goals that they want to achieve as a reminder. Users can mark an habit as completed if it has been carried out every single day. An habit added will be shown every day except for days before the day it was saved", "The web app was mainly written in python, built with Flask web application framework and MongoDb for the backend. While building this app, I gained more experience of setting up Flask applications and projects in general. I also learned a lot about testing with pytest."
        ]
    },
    "microblog": {
        "name": "Microblog App",
        "thumb": "img/microblog.jpg",
        "hero": "img/microblog-hero.jpg",
        "technologies": ["Python", "HTML", "CSS"],
        "prod": "https://ace-microblog-app.herokuapp.com/",
        "description": [
            "Microblog app is a simple web app where users can post and read blogs. It has a form for users to submit a blog post and displays all posted blogs.", "The web app was written in Python, with the Flask web application framework and MongoDB for the backend. This was my first time using the Flask framework, I got familiar with Flask by building this app. I also learned about the Python MongoDB framework Pymongo."
        ]
    },
    "movie-watchlist": {
        "name": "Movie Watchlist App",
        "thumb": "img/movie-watchlist.jpg",
        "hero": "img/movie-watchlist-hero.jpg",
        "technologies": ["Python", "HTML", "CSS", "PostgreSQL"],
        "prod": "https://ace-movie-watchlist.herokuapp.com/",
        "description": [
            "This is a flask app that helps users save and set reminders for their favorite movies. Users can save movies they have watched or yet to watch. Users can also check out the movies other users are watching and rate other users movies or even their own movies. A user can delete or update the details of a movie they added.", "Building this app strengthen my SQL skills. I used SQL syntax and functions such as JOINS, VIEWS, UPSERT, CONSTRAINTS etc.", "I also for the first made a dark view of a web app. I learned how to apply the dark view properties, how to store user preference in local storage so that the user choice stays persistent unless changed. Check it out in production."
        ]
    },
}


@bp.route("/<string:slug>")
def project(slug):
    if slug not in projects:
        abort(404)
    return render_template(f"pages/project.html", title=f"{slug}", project=projects[slug])
