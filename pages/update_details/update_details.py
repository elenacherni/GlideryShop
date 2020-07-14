from flask import Blueprint, render_template,request, redirect, url_for, session
from utilities.db.db_manager import dbManager

# update_details blueprint definition
update_details = Blueprint('update_details', __name__, static_folder='static', static_url_path='/update_details', template_folder='templates')

# Routes

@update_details.route('/update_details', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        email = request.form['Email']
        firstName = request.form['FirstName']
        lastName = request.form['LastName']
        phone = request.form['PhoneNumber']
        address_street = request.form['Street']
        address_number = request.form['StreetNumber']
        city = request.form['City']
        zip = request.form['ZipCode']
        psw = request.form['Password']
        customer_update = dbManager.commit('UPDATE customers SET FirstName=%s, LastName=%s, PhoneNumber=%s, Street=%s,StreetNumber=%s, City=%s, ZipCode=%s, Password=%s WHERE Email = %s', (firstName, lastName, phone, address_street, address_number, city, zip, psw,email))
        print(customer_update)
        return redirect(url_for('profile.index'))

    email = session.get('Email')
    customer = dbManager.fetch('SELECT * FROM customers WHERE Email=%s', (email,))
    return render_template('update_details.html', customer = customer[0])