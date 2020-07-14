from flask import Blueprint, render_template, session
from utilities.db.db_manager import dbManager

# profile blueprint definition
profile = Blueprint('profile', __name__, static_folder='static', static_url_path='/profile', template_folder='templates')


# Routes
@profile.route('/profile')
def index():
    email = session.get('Email')
    ShoppingCartID = session.get('ShoppingCartID')
    OrderDetails = dbManager.fetch('SELECT OrderID, OrderDate, totalPrice FROM orders WHERE shoppingCartID = %s', (ShoppingCartID,))
    customer = dbManager.fetch('SELECT * FROM customers WHERE Email=%s', (email,))
    if OrderDetails:
        return render_template('profile.html', Order_Details=OrderDetails, customer = customer[0])
    return render_template('profile.html', customer = customer[0])

