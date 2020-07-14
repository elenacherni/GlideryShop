from flask import Blueprint, render_template,request, redirect, url_for, session
from utilities.db.db_manager import dbManager

# sign_in blueprint definition
sign_in = Blueprint('sign_in', __name__, static_folder='static', static_url_path='/sign_in', template_folder='templates')

# Routes


@sign_in.route('/sign_in')
def index():
    if 'customerNotFound' in request.args:
        tab_name = request.args['customerNotFound']
        return render_template('sign_in.html', tab_name=tab_name)
    return render_template('sign_in.html')



@sign_in.route('/sign_in_form', methods=['POST'])
def sign_in_form():
    if request.method == 'POST':
        email = request.form['Email']
        psw = request.form['Password']
        customer = dbManager.fetch('SELECT * FROM customers WHERE Email=%s AND Password=%s', (email,psw))
        shoppingCartID = dbManager.fetch('SELECT ShoppingCartID FROM shopping_carts WHERE Email=%s', (email,))
        if customer and len(customer):
            session['logged_in'] = True
            session['customer'] = {
                'FirstName': customer[0].FirstName,
                'LastName': customer[0].LastName,
                'Email': customer[0].Email,
                'City': customer[0].City,
                'Street': customer[0].Street,
                'StreetNumber': customer[0].StreetNumber,
                'ZipCode': customer[0].ZipCode,
                'PhoneNumber': customer[0].PhoneNumber,
                'DateOfBirth': customer[0].DateOfBirth,
                'Password': customer[0].Password,
            }
            session['Email'] = customer[0].Email
            session['ShoppingCartID'] = shoppingCartID[0].ShoppingCartID

            return redirect(url_for('homepage.index'))
        else:
            return redirect('/sign_in?customerNotFound=true')
    return render_template('sign_in.html')
