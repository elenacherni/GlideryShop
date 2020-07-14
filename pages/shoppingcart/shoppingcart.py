from flask import Blueprint, render_template, request, session, redirect, url_for
from utilities.db.db_manager import dbManager

# shoppingcart blueprint definition
shoppingcart = Blueprint('shoppingcart', __name__, static_folder='static', static_url_path='/shoppingcart', template_folder='templates')


# Routes
@shoppingcart.route('/shoppingcart')
def index():
    if session.get('logged_in'):
        ShoppingCartID = session.get('ShoppingCartID')
        typeIceCream = 'ice_cream'
        typeYogurt = 'yogurt'
        iceCreamsResults = dbManager.fetch('''SELECT p.productID, pp.productName, Amount, Price, Flavour FROM products_prices as pp JOIN products as p on pp.ProductName=p.ProductName JOIN box_flavours bf on p.ProductID = bf.ProductID JOIN flavours f on bf.FlavourID = f.FlavourID where ShoppingCartID=%s AND Type=%s order by ProductID''', (ShoppingCartID, typeIceCream))
        yogurtsResults = dbManager.fetch('''SELECT p.productID, pp.productName, Amount, Price, Flavour FROM products_prices as pp JOIN products as p on pp.ProductName=p.ProductName JOIN box_flavours bf on p.ProductID = bf.ProductID JOIN flavours f on bf.FlavourID = f.FlavourID where ShoppingCartID=%s AND Type=%s order by ProductID''', (ShoppingCartID, typeYogurt))
        yogurtsToppingsResults = dbManager.fetch('''SELECT p.productID, ToppingName FROM products as p join yogurtbox_toppings yt on p.ProductID = yt.ProductID join toppings t on yt.ToppingID = t.ToppingID where ShoppingCartID=%s order by ProductID''', (ShoppingCartID,))
        cookiesResults = dbManager.fetch('''SELECT p.productID, pp.productName, Amount, Price, CookieType, Flavour FROM products_prices as pp JOIN products as p on pp.ProductName=p.ProductName join icecream_sandwiches i on p.ProductID = i.ProductID join cookies c on i.CookieID = c.CookieID join flavours f on i.FlavourID = f.FlavourID where ShoppingCartID=%s''', (ShoppingCartID,))
        totalPriceResult = dbManager.fetch('''SELECT SUM(Amount*Price) totalPrice FROM products_prices as pp JOIN products as p on pp.ProductName=p.ProductName where ShoppingCartID=%s;''', (ShoppingCartID,))
        totalAmountResult = dbManager.fetch('''SELECT SUM(Amount) totalAmount FROM products_prices as pp JOIN products as p on pp.ProductName=p.ProductName where ShoppingCartID=%s;''', (ShoppingCartID,))
        if iceCreamsResults or yogurtsResults or yogurtsToppingsResults or cookiesResults or totalPriceResult or totalAmountResult:
            return render_template('shoppingcart.html', iceCreams=iceCreamsResults, yogurts=yogurtsResults, toppings = yogurtsToppingsResults, cookies = cookiesResults, totalPrice = totalPriceResult[0].totalPrice, totalAmount=totalAmountResult[0].totalAmount)
        return render_template('shoppingcart.html')
    else:
        return render_template('sign_in.html')

@shoppingcart.route('/deleteCart')
def deleteItems():
    if request.method == 'GET':
        Delete_icecream = request.args.getlist('delete-icecream')
        Delete_yogurt = request.args.getlist('delete-yogurt')
        Delete_cookie = request.args.getlist('delete-cookie')
        if len(Delete_icecream) >= 1:
            for i in range(len(Delete_icecream)):
                dbManager.commit('DELETE FROM box_flavours WHERE ProductID= %s', (Delete_icecream[i],))
                dbManager.commit('DELETE from products where productID = %s', (Delete_icecream[i],))
        if len(Delete_yogurt) >= 1:
            for i in range(len(Delete_yogurt)):
                dbManager.commit('DELETE FROM box_flavours WHERE ProductID= %s', (Delete_yogurt[i],))
                dbManager.commit('DELETE FROM yogurtbox_toppings WHERE ProductID= %s', (Delete_yogurt[i],))
                dbManager.commit('DELETE from products where productID = %s', (Delete_yogurt[i],))
        if len(Delete_cookie) >= 1:
            for i in range(len(Delete_cookie)):
                dbManager.commit('DELETE FROM icecream_sandwiches WHERE ProductID= %s', (Delete_cookie[i],))
                dbManager.commit('DELETE from products where productID = %s', (Delete_cookie[i],))
    return redirect(url_for('shoppingcart.index'))
