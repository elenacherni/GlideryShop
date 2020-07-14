from flask import Blueprint, render_template, request
from utilities.db.db_manager import dbManager

# events blueprint definition
events = Blueprint('events', __name__, static_folder='static', static_url_path='/events', template_folder='templates')


# Routes
@events.route('/events', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        maxID = dbManager.fetch('SELECT max(OfferID) AS max FROM occasion_offers ')
        if maxID[0].max:
            OfferID= maxID[0].max+1
        else:
            OfferID=1
        Uname = request.form['FullName']
        Uphone = request.form['PhoneNumber']
        insertData = dbManager.commit('insert into occasion_offers values (%s, %s, %s)', (OfferID, Uname,Uphone))
        if insertData:
            return render_template('events.html')
    elif request.method == 'GET':
        return render_template('events.html')