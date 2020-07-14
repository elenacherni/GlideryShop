from flask import Blueprint, render_template,request, redirect, url_for,session
from utilities.db.db_manager import dbManager
from datetime import datetime
# sign_up blueprint definition
sign_up = Blueprint('sign_up', __name__, static_folder='static', static_url_path='/sign_up', template_folder='templates')


# Routes
@sign_up.route('/sign_up')
def index():
    if 'emailexist' in request.args:
        tab_name = request.args['emailexist']
        return render_template('sign_up.html', tab_name=tab_name)
    return render_template('sign_up.html')


@sign_up.route('/sign_up_form', methods=['POST'])
def sign_up_form():
    if request.method == 'POST':
        email = request.form['Email']
        fName = request.form['FirstName']
        lName = request.form['LastName']
        DOB = request.form['DateOfBirth']
        psw = request.form['Password']
        now = datetime.now()

        checkCustomer = dbManager.fetch('SELECT * FROM customers WHERE Email=%s ', (email,))
        print(checkCustomer)
        if checkCustomer == []:
            maxID = dbManager.fetch('SELECT max(ShoppingCartID) AS max FROM shopping_carts ')
            if maxID[0].max:
                ShoppingCartID= maxID[0].max+1
            else:
                ShoppingCartID=1
            dbManager.commit('INSERT INTO customers VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s)', (email, psw, fName, lName, DOB, '', '', 0, '', ''))
            db = dbManager.commit('INSERT INTO shopping_carts VALUES (%s, %s, %s)', (ShoppingCartID, now, email))
            print(db)
            return redirect(url_for('sign_in.index'))
        else:
            return redirect('/sign_up?emailexist=true')
