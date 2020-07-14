from flask import Blueprint, render_template, request, jsonify, session
from utilities.db.db_manager import dbManager

# order blueprint definition
order = Blueprint('order', __name__, static_folder='static', static_url_path='/order', template_folder='templates')


# Routes
@order.route('/order')
def index():
    if 'tab' in request.args:
        tab_name = request.args['tab']
        return render_template('order.html', tab_name=tab_name)
    return render_template('order.html', tab_name='icecream')


@order.route('/iceCreamOrder')
def iceCreamOrder():
    if request.method == 'GET':
        maxID = dbManager.fetch('SELECT max(ProductID) AS max FROM products ')
        if maxID[0].max:
            productID= maxID[0].max+1
        else:
            productID=1
        selectAmount = request.args['amount']
        ProductName = "גלידה "+selectAmount+" קילו"
        Amount = request.args['quantity']
        ShoppingCartID = session.get('ShoppingCartID')
        ice_cream_tastes = request.args.getlist('ice_cream_tastes')
        if len(ice_cream_tastes) >= 1:
            rowProduct = dbManager.commit('INSERT INTO products VALUES (%s,%s,%s,%s)',(productID, ProductName, Amount, ShoppingCartID))
            print(rowProduct)
            for i in range(len(ice_cream_tastes)):
                rowBox = dbManager.commit('INSERT INTO box_flavours VALUES (%s,%s)',(productID, ice_cream_tastes[i]))
                print(rowBox)
    return render_template('order.html', tab_name='icecream')


@order.route('/yogurtOrder')
def yogurtOrder():
    if request.method == 'GET':
        maxID = dbManager.fetch('SELECT max(ProductID) AS max FROM products ')
        if maxID[0].max:
            productID= maxID[0].max+1
        else:
            productID=1
        ProductName = "יוגורט "+request.args['amount']+" קילו"
        Amount = request.args['quantity']
        ShoppingCartID = session.get('ShoppingCartID')
        yogurt_tastes = request.args.getlist('yogurt_tastes')
        toppings_chosen = request.args.getlist('toppings_chosen')
        if len(yogurt_tastes) >= 1:
            rowProduct = dbManager.commit('INSERT INTO products VALUES (%s,%s,%s,%s)',(productID, ProductName, Amount, ShoppingCartID))
            print(rowProduct)
            for i in range(len(yogurt_tastes)):
                rowBox = dbManager.commit('INSERT INTO box_flavours VALUES (%s,%s)',(productID, yogurt_tastes[i]))
                print(rowBox)
        if len(toppings_chosen) >=1:
            for i in range(len(toppings_chosen)):
                rowBoxTopping = dbManager.commit('INSERT INTO yogurtbox_toppings VALUES (%s,%s)',(productID, toppings_chosen[i]))
                print(rowBoxTopping)
    return render_template('order.html', tab_name='yogurt')


@order.route('/cookieOrder')
def cookieOrder():
    if request.method == 'GET':
        maxID = dbManager.fetch('SELECT max(ProductID) AS max FROM products ')
        if maxID[0].max:
            productID= maxID[0].max+1
        else:
            productID=1
        ProductName = "קוקילידה"
        Amount = request.args['quantity']
        ShoppingCartID = session.get('ShoppingCartID')
        cookie_chosen = request.args['cookie_chosen']
        cookie_filling = request.args['cookie_filling']
        if cookie_chosen and cookie_filling:
            rowProduct = dbManager.commit('INSERT INTO products VALUES (%s,%s,%s,%s)',(productID, ProductName, Amount, ShoppingCartID))
            print(rowProduct)
            rowSanwich = dbManager.commit('INSERT INTO icecream_sandwiches VALUES (%s,%s,%s)',(productID, cookie_chosen, cookie_filling))
            print(rowSanwich)
    return render_template('order.html', tab_name='cookie')

# Endpoints

@order.route('/order/<type>')
def objects(type):
    if type == 'cookie':
        query_cookies = dbManager.fetch('SELECT * FROM cookies')
        if query_cookies:
            cookies = list(map(lambda row:row._asdict(), query_cookies))
            return jsonify({
                'success': True,
                'cookies': cookies,
            })
    elif type == 'topping':
        query_toppings = dbManager.fetch('SELECT * FROM toppings')
        if query_toppings:
            toppings = list(map(lambda row: row._asdict(), query_toppings))
            return jsonify({
                'success': True,
                'toppings': toppings,
            })
    elif type=='ice_cream' or type == 'yogurt':
        query_flavours = dbManager.fetch('SELECT * FROM flavours AS f WHERE f.Type=%s', (type,))
        if query_flavours:
            flavours = list(map(lambda row: row._asdict(), query_flavours))
            return jsonify({
                'success': True,
                'flavours': flavours,
            })
    else:
        return jsonify({'success': False})