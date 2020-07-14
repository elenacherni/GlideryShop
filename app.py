from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## About
from pages.about.about import about
app.register_blueprint(about)

## Catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)

## Product
from pages.product.product import product
app.register_blueprint(product)

## Order
from pages.order.order import order
app.register_blueprint(order)

## shoppingcart
from pages.shoppingcart.shoppingcart import shoppingcart
app.register_blueprint(shoppingcart)

## Contact
from pages.contact.contact import contact
app.register_blueprint(contact)

## ConfirmOrder
from pages.confirmOrder.confirmOrder import confirmOrder
app.register_blueprint(confirmOrder)

## Events
from pages.events.events import events
app.register_blueprint(events)

## Payment
from pages.payment.payment import payment
app.register_blueprint(payment)

## sign_in
from pages.sign_in.sign_in import sign_in
app.register_blueprint(sign_in)

## log_out
from pages.log_out.log_out import log_out
app.register_blueprint(log_out)

## sign_up
from pages.sign_up.sign_up import sign_up
app.register_blueprint(sign_up)

## profile
from pages.profile.profile import profile
app.register_blueprint(profile)

## update_details
from pages.update_details.update_details import update_details
app.register_blueprint(update_details)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)
