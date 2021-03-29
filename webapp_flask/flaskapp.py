####################################################################################################
#####                   Module Imports                                                         #####
####################################################################################################

import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from forms import ProductSearchForm
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

@app.route('/product', methods = ['GET', 'POST']) 
def products_page():
    search = ProductSearchForm(request.form)
    results = True
    if request.method == 'POST':
        #products = msm.searchTable("products", "product_name", search.data["search"])
        sort_method = search.data["select"]
        if sort_method[0] == '1': # name
            search_column = 'product_name'
        elif sort_method[0] == '2': # quantity
            search_column = 'quantity'
        elif sort_method[0] == '3': # price
            search_column = 'unit_price'
        if sort_method[1] == '0':
            sort_type = 'DESC'
        elif sort_method[1] == '1':
            sort_type = 'ASC'
        products = msm.searchTableFilter("products", "product_name", search.data["search"], search_column, sort_type)
    else:
        products = msm.getAllTableDictionary("products")
    products_len = len(products)
    if products_len == 0:
        results = False
    product_rows = []
    if products_len % 3 == 1:
        products.append(0) #need way to not show blanks
        products.append(0)
    elif products_len % 3 == 2:
        products.append(0)
    for i in range(0, products_len, 3):
            product_rows.append(products[i:i+3])
    return render_template('products_page.html', rows=product_rows, title='Products', form=search, results=results)

####################################################################################################
#####                   Auto run site                                                          #####
####################################################################################################

# Auto run site in website if run from this module
if __name__ == '__main__':
    app.run(debug=True)
