from flask import Blueprint, render_template

# confirmOrder blueprint definition
confirmOrder = Blueprint('confirmOrder', __name__, static_folder='static', static_url_path='/confirmOrder', template_folder='templates')


# Routes
@confirmOrder.route('/confirmOrder')
def index():
    return render_template('confirmOrder.html')
