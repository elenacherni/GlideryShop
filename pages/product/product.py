from flask import Blueprint, render_template, request
from utilities.db.db_manager import dbManager

# product blueprint definition
product = Blueprint('product', __name__, static_folder='static', static_url_path='/product', template_folder='templates')


# Routes
@product.route('/product')
def index():
    if 'flavour' in request.args:
        product_flavour = request.args['flavour']
        query_result = dbManager.fetch(
        '''
        SELECT * FROM flavours AS f
        WHERE f.FlavourID=%s
        ''',(product_flavour,))
        if query_result:
            return render_template('product.html', flavour=query_result[0])
    return render_template('product.html')
