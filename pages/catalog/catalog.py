from flask import Blueprint, render_template, request
from utilities.db.db_manager import dbManager

# catalog blueprint definition
catalog = Blueprint('catalog', __name__, static_folder='static', static_url_path='/catalog', template_folder='templates')


# Routes
@catalog.route('/catalog')
def index():
    if 'type' in request.args:
        catalog_name = request.args['type']
        query_results = dbManager.fetch('''
        SELECT * FROM flavours AS f
        WHERE f.Type=%s
        ''',(catalog_name,))
        if query_results:
           return render_template('catalog.html', flavours=query_results)
    return render_template('catalog.html')

