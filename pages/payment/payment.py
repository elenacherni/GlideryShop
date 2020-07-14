from flask import Blueprint, render_template, request, session
from utilities.db.db_manager import dbManager
from datetime import datetime


# payment blueprint definition
payment = Blueprint('payment', __name__, static_folder='static', static_url_path='/payment', template_folder='templates')


# Routes
@payment.route('/payment')
def index():
    ShoppingCartID = session.get('ShoppingCartID')
    totalPriceResult = dbManager.fetch('''SELECT SUM(Amount*Price) totalPrice FROM products_prices as pp JOIN products as p on pp.ProductName=p.ProductName where ShoppingCartID=%s;''', (ShoppingCartID,))
    email = session.get('Email')
    customer = dbManager.fetch('SELECT * FROM customers WHERE Email=%s', (email,))
    return render_template('payment.html', total_Price = totalPriceResult[0].totalPrice, customer=customer[0])

@payment.route('/payment-form',  methods=['POST'])
def form():

    if request.method == 'POST':
        email = request.form['email']
        phone = request.form['phone']
        address_street = request.form['address-street']
        address_number = request.form['address-number']
        city = request.form['city']
        zip = request.form['zip']
        customer_update = dbManager.commit('UPDATE customers SET City=%s, Street=%s, StreetNumber=%s, ZipCode=%s, PhoneNumber=%s WHERE Email = %s', (city, address_street, address_number, zip, phone, email))
        id = request.form['id']
        card_number = request.form['cardnumber']
        cvv = request.form['cvv']
        exp_month = request.form['exp-month']
        exp_year = request.form['exp-year']
        comment = request.form['comment']
        ShoppingCartID = session.get('ShoppingCartID')
        Date = datetime.today().strftime('%y-%m-%d')
        totalPriceResult = dbManager.fetch('''SELECT SUM(Amount*Price) totalPrice FROM products_prices as pp JOIN products as p on pp.ProductName=p.ProductName where ShoppingCartID=%s;''', (ShoppingCartID,))
        totalPrice = totalPriceResult[0].totalPrice
        maxID = dbManager.fetch('SELECT max(OrderID) AS max FROM orders')
        if maxID[0].max :
            OrderID= maxID[0].max+1
        else:
            OrderID=1
        Order_table = dbManager.commit('INSERT into orders VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)', (OrderID, id, card_number, cvv, exp_month, exp_year, comment, ShoppingCartID, Date, totalPrice))
        if Order_table:
            product_delete = dbManager.fetch('SELECT productID FROM products WHERE ShoppingCartID = %s', (ShoppingCartID,))
            if product_delete:
                for i in range(len(product_delete)):
                    row1 = dbManager.commit('DELETE from box_flavours where ProductID = %s', (product_delete[i].productID,))
                    row2 = dbManager.commit('DELETE from icecream_sandwiches where ProductID = %s', (product_delete[i].productID,))
                    row3 = dbManager.commit('DELETE from yogurtbox_toppings where ProductID = %s', (product_delete[i].productID,))
                    row4 = dbManager.commit('DELETE from products where ProductID = %s', (product_delete[i].productID,))
            return render_template('confirmOrder.html')
    elif request.method == 'GET':
        return render_template('payment.html')