####################################################################################################
#####                   Module Imports                                                         #####
####################################################################################################

import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from forms import ProductSearchForm, OrderSearchForm
from flask import Flask, escape, request, render_template, url_for 
import mysqlmodule as msm
import datetime
from itertools import groupby

####################################################################################################
#####                   Flask setup                                                            #####
####################################################################################################

app = Flask(__name__)

app.config['SECRET_KEY'] = '201def51bb6b28e0290a585c8eb778d6'

####################################################################################################
#####                   Need to make buttons to access functions                               #####
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
    customers = msm.getAllTableDictionary("customers")
    shipping_address = msm.getAllTableDictionary("shipping_address")
    return render_template('customers_page.html', customers=customers, title='Customers')

@app.route('/profit', methods = ['GET', 'POST'])
def profits_page(): ############# CROSS TABULATION WOOOOOOOOOO HOOOOOOOOO
    orders = msm.getAllTableDictionary("orders")
    dates = []
    for order in orders:
        dates.append(datetime.date(int(order["order_date"][6:]), int(order["order_date"][3:5]), int(order["order_date"][:2])))
    dates.sort()
    first_order = dates[0]
    last_order = dates[len(dates)-1]
    months = (last_order.month - first_order.month) + (12 * (last_order.year - first_order.year)) + 1
    orders_month_array = []
    count = 0
    for i in range(1, months):
        for date in dates:
            if ((date.month - first_order.month + 1) + (12 * (date.year - first_order.year))) == i:
                orders_month_array.append([orders[count]["order_id"], (date.month, date.year)])
                count += 1
    month_array = []
    for key, group in groupby(orders_month_array, lambda x: x[1]):
        members = []
        for thing in group:
            members.append(thing[0])
        month_array.append([{"month":str(key), "orders":members}])
    for row in month_array:
        order_details = []
        for order in row[0]["orders"]:
            order_details.append(msm.searchExact("Orders", "order_id", order)[0])
        row[0]["order_details"] = order_details
        order_total = 0
        for order in row[0]["order_details"]:
            order_total += order["order_subtotal"]
        row[0]["order_total"] = order_total
        date = row[0]["month"]
        formatted_date = date.strip("()")
        row[0]["month"] = formatted_date
    return render_template('profits_page.html', months=month_array)

@app.route('/order', methods = ['GET', 'POST'])
def orders_page():
    search = OrderSearchForm(request.form)
    results = True
    if request.method == 'POST':
        sort_method = search.data["select"]
        if sort_method[0] == '1': # name
            search_column = 'order_id'
        elif sort_method[0] == '2': # status
            search_column = 'order_status'
        elif sort_method[0] == '3': # price
            search_column = 'order_subtotal'
        if sort_method[1] == '0':
            sort_type = 'DESC'
        elif sort_method[1] == '1':
            sort_type = 'ASC'
        orders = msm.searchTableFilter("orders", "order_id", "", search_column, sort_type)
    else:
        orders = msm.getAllTableDictionary("orders")
    for order in orders:
        orderID = order["order_id"]
        order["order_lines"] = msm.searchExact("order_lines", "order_id", orderID)
        for line in order["order_lines"]:
            products = msm.searchExact("Products", "product_id", line["fk_product_id"])
            line["product_name"] = products[0]["product_name"]
    return render_template('orders_page.html', orders=orders, form=search)

@app.route('/product', methods = ['GET', 'POST']) 
def products_page():
    search = ProductSearchForm(request.form)
    results = True
    if request.method == 'POST':
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
