####################################################################################################
#####                   Module Imports                                                         #####
####################################################################################################

import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from itertools import islice
from forms import SearchForm
from flask import Flask, escape, request, render_template, url_for 
import mysqlmodule as msm

####################################################################################################
#####                   Flask setup                                                            #####
####################################################################################################

app = Flask(__name__)

app.config['SECRET_KEY'] = '201def51bb6b28e0290a585c8eb778d6'

####################################################################################################
#####                   Need to make pages and format those for displaying data (part complete)#####
#####                   Need to make buttons to access functions                               #####
#####                   Need to add search bars                                                #####
#####                   - need to integrate into html                                          #####
#####                   - need to show results in page                                         #####
####################################################################################################

####################################################################################################
#####                   Decorator link to pages                                                ##### 
####################################################################################################

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/customer', methods = ['GET', 'POST'])
def customers_page():
    search = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    customers = msm.getAllTableDictionary("customers")
    shipping_address = msm.getAllTableDictionary("shipping_address")
    return render_template('customers_page.html', customers=customers, title='Customers')

@app.route('/order', methods = ['GET', 'POST'])
def orders_page():
    search = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    orders = msm.getAllTableDictionary("orders")
    order_lines = msm.getAllTableDictionary("order_lines")
    return render_template('orders_page.html', orders=orders, order_lines=order_lines)

@app.route('/product', methods = ['GET', 'POST']) #page not working
def products_page():
    search = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    products = msm.getAllTableDictionary("products")
    products_len = len(products)
    if products_len // 3 == 0:
        product_rows = [products[x:x+3] for x in range(0, products_len, 3)]
    elif products_len // 3 == 1:
        products.append(0)
        products.append(0)
        product_rows = [products[x:x+3] for x in range(0, products_len, 3)]
    elif products_len // 3 == 2:
        products.append(0)
        product_rows = [products[x:x+3] for x in range(0, products_len, 3)]
    # need to add formatting to make the products into rows then submit them to the page
    # also need to add jinja formatting to the page to take each row and show it
    return render_template('products_page.html', rows=product_rows, title='Products', form=search)

####################################################################################################
#####                   Auto run site                                                          #####
####################################################################################################

# Auto run site in website if run from this module
if __name__ == '__main__':
    app.run(debug=True)