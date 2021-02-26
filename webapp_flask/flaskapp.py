####################################################################################################
#####                   Module Imports                                                         #####
####################################################################################################

import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from flask import Flask, escape, request, render_template, url_for 
import mysqlmodule as msm

####################################################################################################
#####                   Flask setup                                                            #####
####################################################################################################

app = Flask(__name__)

app.config['SECRET_KEY'] = '201def51bb6b28e0290a585c8eb778d6'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


####################################################################################################
#####                   Need to make pages and format those for displaying data                #####
#####                   Need to make buttons to access functions                               #####
####################################################################################################

####################################################################################################
#####                   Decorator link to pages                                                 
####################################################################################################

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/customers')
def customers_page():
    customers = msm.getAllTableDict("customers")
    shipping_address = msm.getAllTableDict("shipping_address")
    return render_template('customers_page.html', customers=customers, title='Customers')

@app.route('/orders')
def orders_page():
    orders = msm.getAllTableDict("orders")
    order_lines = msm.getAllTableDict("order_lines")
    return render_template('orders_page.html', orders=orders, order_lines=order_lines)

@app.route('/products')
def products_page():
    products = msm.getAllTableDict("products")
    return render_template('products_page.html', products=products, title='Products')

####################################################################################################
#####                   Auto run site - MOVE                                                   #####
####################################################################################################

# Auto run site in website if run from this module
if __name__ == '__main__':
    app.run(debug=True)