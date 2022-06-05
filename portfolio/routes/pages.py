from datetime import datetime
from flask import Blueprint, render_template

bp = Blueprint('pages', __name__)

@bp.route('/')
def home():
    return render_template('pages/index.html', title='Home')

@bp.route('/about')
def about():
    return render_template('pages/about.html', title='About')

@bp.route('/contact')
def contact():
    return render_template('pages/contact.html', title='Contact')

@bp.context_processor
def inject_current_year():
    return {"year": datetime.now().year}