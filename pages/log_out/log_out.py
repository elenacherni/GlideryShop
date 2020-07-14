from flask import Blueprint, redirect, url_for, session

# log_out blueprint definition
log_out = Blueprint('log_out', __name__, static_folder='static', static_url_path='/log_out', template_folder='templates')

# Routes
@log_out.route('/log_out')
def index():
    session.clear()
    return redirect(url_for('homepage.index'))
