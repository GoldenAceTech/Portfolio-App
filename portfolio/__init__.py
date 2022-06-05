from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import pages

    app.register_blueprint(pages.bp)
    

    return app