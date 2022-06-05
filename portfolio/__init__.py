from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config:
        app.config.from_mapping(test_config)

    from .routes import pages

    app.register_blueprint(pages.bp)
    
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app