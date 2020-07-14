from flask import Blueprint, render_template, request
from utilities.db.db_manager import dbManager

# contact blueprint definition
contact = Blueprint('contact', __name__, static_folder='static', static_url_path='/contact', template_folder='templates')


# Routes
@contact.route('/contact', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        maxID = dbManager.fetch('SELECT max(ContactID) AS max FROM contacts ')
        if maxID[0].max:
            contactID= maxID[0].max+1
        else:
            contactID=1
        Uname = request.form['full-name']
        Uphone = request.form['phone-number']
        message = request.form['message']
        dbManager.commit('insert into contacts values (%s, %s, %s,%s)', (contactID, Uname,Uphone, message))
        return render_template('contact.html')
    elif request.method == 'GET':
        return render_template('contact.html')

