####################################################################################################
#####                   Module Imports                                                         #####
####################################################################################################

import mysql.connector
from datetime import datetime

####################################################################################################
#####                   Database connection                                                    #####
####################################################################################################

# PC
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="^9#^QsfJRZ",
    database="mydatabase"
)

# LAPTOP
'''
mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="MYSQL"
)
'''
mycursor = mydb.cursor()

####################################################################################################
#####                   Event logging                                                          #####
####################################################################################################

def logEvent(log_info):
    event_time = datetime.now()
    with open("./NEA/db_log.txt", "a") as log:
        log.write(f"|{event_time}| {log_info}\n")

####################################################################################################
#####                   Database I/O                                                           #####
####################################################################################################

# defunct
def getAllTableArray_Print(table_name):
    sql = f"SELECT * FROM {table_name}"
    mycursor.execute(sql)
    result_values = mycursor.fetchall()
    for x in result_values:
        print(x) 
    logEvent(f"Records from {table_name} accessed.")

# defunct
def getAllTableArray_Return(table_name):
    sql = f"SELECT * FROM {table_name}"
    mycursor.execute(sql)
    result_values = mycursor.fetchall()
    logEvent(f"Records from {table_name} accessed.")
    for x in result_values:
        return x 

def getAllTableDictionary(table_name):
    sql = f"SELECT * FROM {table_name}"
    mycursor.execute(sql)
    return getRecordsAsDictionary(table_name, mycursor.fetchall())

def getRecordsAsDictionary(table_name, records):
    sql = f"SHOW columns FROM {table_name}"
    mycursor.execute(sql)
    result_columns = mycursor.fetchall()
    result_dictionary = {}
    column_names = ()
    values = ()
    dictionaries = []
    for i in result_columns:
        column_names += (i[0],)
    for i in records:
        for j in range(len(i)):
            result_dictionary[column_names[j]] = i[j]
        dictionaries.append(result_dictionary.copy())
    logEvent(f"Records from {table_name} accessed.")
    return dictionaries

def deleteRecord(table_name, column, check_info):
    sql = f"DELETE FROM {table_name} WHERE {column} = '{check_info}'"
    mycursor.execute(sql)
    mydb.commit()
    logEvent(f"{mycursor.rowcount}, record(s) deleted from {table_name}.")

def updateRecord(table_name, column, check_info, new_info):
    sql = f"UPDATE {table_name} SET {column} = '{new_info}' WHERE {column} = '{check_info}'"
    mycursor.execute(sql)
    mydb.commit()
    logEvent(f"{mycursor.rowcount}, record(s) updated in {table_name}.")

def clearTable(table_name):
    sql = f"DELETE FROM {table_name}"
    mycursor.execute(sql)
    mydb.commit()
    logEvent(f"All records in {table_name} deleted. {mycursor.rowcount}, record(s) deleted.")

def addRecordToTable(table_name, info_dict):
    formatted_columns = ", ".join(info_dict.keys())
    formatted_info = "', '".join(info_dict.values())
    sql = f"INSERT INTO {table_name} ({formatted_columns}) VALUES ('{formatted_info}')"
    mycursor.execute(sql)
    mydb.commit()
    logEvent(f"{mycursor.rowcount}, record(s) inserted in {table_name}.")

def searchExact(table_name, search_column, search_term):
    sql = f"SELECT * FROM {table_name} WHERE {search_column} LIKE '{search_term}'"
    mycursor.execute(sql)
    return getRecordsAsDictionary(table_name, mycursor.fetchall())

def searchTable(table_name, search_column, search_term):
    sql = f"SELECT * FROM {table_name} WHERE {search_column} LIKE '%{search_term}%'"
    mycursor.execute(sql)
    return getRecordsAsDictionary(table_name, mycursor.fetchall())

def searchTableFilter(table_name, search_column, search_term, filter_column, filter_order):
    sql = f"SELECT * FROM {table_name} WHERE {search_column} LIKE '%{search_term}%' ORDER BY {filter_column} {filter_order}"
    mycursor.execute(sql)
    return getRecordsAsDictionary(table_name, mycursor.fetchall())

####################################################################################################
#####                   Orders                                                                 #####
####################################################################################################

def newOrder(customerID, date, shipping, lines):
    ##### different item weights may be different shipping #####
    if shipping == "Expedited":
        shipping_cost = 9.99
    elif shipping == "Standard":
        shipping_cost = 4.99
    order_info = {
        "fk_customer_id": str(customerID),
        "order_date": str(date),
        "shipping_method": shipping,
        "order_status": "Processing",
        "shipping_amount": str(shipping_cost),
    }
    addRecordToTable("orders", order_info)
    ##### need to add orderlines and then calculate subtotal costs #####
    for _ in range(lines):
        product_cost += addOrderLine() #######################


def addOrderLine(orderID, productID, quantity):
    record = searchExact("products", "product_id", productID)[0]
    line_price = quantity * int(record["unit_price"])
    order_line_info = {
        "order_id": str(orderID),
        "fk_product_id": str(productID),
        "quantity": str(quantity),
        "total_line_price": str(line_price)
    }
    addRecordToTable("order_lines", order_line_info)
    

