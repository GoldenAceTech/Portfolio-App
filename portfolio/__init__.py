from flask import Flask, render_template
from datetime import datetime

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config:
        app.config.from_mapping(test_config)

    from .routes import pages, projects

    app.register_blueprint(pages.bp)
    app.register_blueprint(projects.bp)
    
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.context_processor
    def inject_current_year():
        return {"year": datetime.now().year}

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('pages/error.html', title='Not found', error=error), 404

    return app