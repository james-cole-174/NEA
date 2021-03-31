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
#####                   Decorator link to pages                                                ##### 
####################################################################################################

####################################################################################################
#####                   Home Page                                                              #####
####################################################################################################

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

####################################################################################################
#####                   Customer Page                                                          #####
####################################################################################################

@app.route('/customer', methods = ['GET', 'POST'])
def customers_page():
    customers = msm.getAllTableDictionary("customers") # Just gets all the customers info
    shipping_address = msm.getAllTableDictionary("shipping_address")
    return render_template('customers_page.html', customers=customers, title='Customers')

####################################################################################################
#####                   Profit Page                                                          #####
####################################################################################################

@app.route('/profit', methods = ['GET', 'POST'])
def profits_page(): 
    orders = msm.getAllTableDictionary("orders")
    dates = []
    for order in orders: # Gets the dates of all the orders
        dates.append(datetime.date(int(order["order_date"][6:]), int(order["order_date"][3:5]), int(order["order_date"][:2])))
    dates.sort() # Sorts the orders by oldest first
    first_order = dates[0]
    last_order = dates[len(dates)-1]
    months = (last_order.month - first_order.month) + (12 * (last_order.year - first_order.year)) + 1 # Gets the amount of months between the first and last order
    orders_month_array = []
    count = 0
    for i in range(1, months):
        for date in dates:
            if ((date.month - first_order.month + 1) + (12 * (date.year - first_order.year))) == i:
                orders_month_array.append([orders[count]["order_id"], (date.month, date.year)]) # If there is an order in that month its added to an array 
                count += 1 # So this is now an array of all the dates that a order happened
    month_array = []
    for key, group in groupby(orders_month_array, lambda x: x[1]): # Key is month (with year) of the order 
        members = [] # Things in the array with the same "key" (happened in the same month)
        for thing in group: 
            members.append(thing[0]) # Get appended to the list of members
        month_array.append([{"month":str(key), "orders":members}]) # Each group then gets appened to a list of dictionaries 
        # with the key as the month and the value as the orders that happened in that month
    for row in month_array: # This now gets the details of each order from the order table
        order_details = []
        for order in row[0]["orders"]:
            order_details.append(msm.searchExact("Orders", "order_id", order)[0])
        row[0]["order_details"] = order_details
        order_total = 0
        for order in row[0]["order_details"]: # This calculates the monthly subtotal by summing all the order subtotals from the month
            order_total += order["order_subtotal"]
        row[0]["order_total"] = order_total
        date = row[0]["month"]
        formatted_date = date.strip("()") # This formats the date to MM, YYYY
        row[0]["month"] = formatted_date
    return render_template('profits_page.html', months=month_array)

####################################################################################################
#####                   Order Page                                                          #####
####################################################################################################

@app.route('/order', methods = ['GET', 'POST'])
def orders_page():
    search = OrderSearchForm(request.form) # Get the form results
    results = True
    if request.method == 'POST': # If theres a POST it means the form was submitted
        sort_method = search.data["select"] # Gets the search information, formatted as two integers
        # The first integer specifies the property to sort results by
        if sort_method[0] == '1': # name
            search_column = 'order_id'
        elif sort_method[0] == '2': # status
            search_column = 'order_status'
        elif sort_method[0] == '3': # price
            search_column = 'order_subtotal'
        # The second integer specifies the order to sort the results by
        if sort_method[1] == '0':
            sort_type = 'DESC'
        elif sort_method[1] == '1':
            sort_type = 'ASC'
        orders = msm.searchTableFilter("orders", "order_id", "", search_column, sort_type) # Get the searched for orders
    else: # Happens when visiting the page from a different page and just displays all the orders as no search has been done yet
        orders = msm.getAllTableDictionary("orders") # Gets all the orders as there was no search
    for order in orders: # For each order it uses the order key to get all the order lines that are associated to the order by having the same order id
        orderID = order["order_id"]
        order["order_lines"] = msm.searchExact("order_lines", "order_id", orderID)
        for line in order["order_lines"]: # For each products in the order line it gets the product associated to the order line by the foreign key - product id
            products = msm.searchExact("Products", "product_id", line["fk_product_id"])
            line["product_name"] = products[0]["product_name"]
    return render_template('orders_page.html', orders=orders, form=search)

####################################################################################################
#####                   Product Page                                                          #####
####################################################################################################

@app.route('/product', methods = ['GET', 'POST']) 
def products_page():
    search = ProductSearchForm(request.form) # Get the form results
    results = True
    if request.method == 'POST': # If theres a POST it means the form was submitted
        sort_method = search.data["select"] # Gets the search information, formatted as two integers
        # The first integer specifies the property to sort results by
        if sort_method[0] == '1': # name
            search_column = 'product_name'
        elif sort_method[0] == '2': # quantity
            search_column = 'quantity'
        elif sort_method[0] == '3': # price
            search_column = 'unit_price'
        # The second integer specifies the order to sort the results by
        if sort_method[1] == '0':
            sort_type = 'DESC'
        elif sort_method[1] == '1':
            sort_type = 'ASC'
        products = msm.searchTableFilter("products", "product_name", search.data["search"], search_column, sort_type) # Get the searched for products
    else: # Happens when visiting the page from a different page and just displays all the products as no search has been done yet
        products = msm.getAllTableDictionary("products") # Gets all the products as there was no search
    products_len = len(products)
    if products_len == 0: # Checks to see if any results came out of the search
        results = False
    product_rows = []
    if products_len % 3 == 1: # Fills out the products with blanks to make rows fit the grid structure
        products.append(0) 
        products.append(0)
    elif products_len % 3 == 2:
        products.append(0)
    for i in range(0, products_len, 3): # Breaks the products into rows of 3
        product_rows.append(products[i:i+3])
    return render_template('products_page.html', rows=product_rows, title='Products', form=search, results=results)

####################################################################################################
#####                   Auto run site                                                          #####
####################################################################################################

# Auto run site in website if run from this module
if __name__ == '__main__':
    app.run(debug=True)
