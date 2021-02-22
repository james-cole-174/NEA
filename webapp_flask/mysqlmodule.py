####################################################################################################
#####                   Module Imports                                                         #####
####################################################################################################

import mysql.connector
from datetime import datetime

####################################################################################################
#####                   Database connection                                                    #####
####################################################################################################

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="^9#^QsfJRZ",
    database="mydatabase"
)

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

def getAllTable(table_name):
    sql = f"SELECT * FROM {table_name}"
    mycursor.execute(sql)
    result_values = mycursor.fetchall()
    for x in result_values:
        print(x) ######################## Prints instead of returns ################################
    logEvent(f"Records from {table_name} accessed.")

def  getAllTableDict(table_name):
    sql = f"SELECT * FROM {table_name}"
    mycursor.execute(sql)
    result_values = mycursor.fetchall()
    sql = f"SHOW columns FROM {table_name}"
    mycursor.execute(sql)
    result_columns = mycursor.fetchall()
    result_dictionary = {}
    column_names = ()
    values = ()
    dictionaries = []
    for i in result_columns:
        column_names += (i[0],)
    for i in result_values:
        for j in range(len(i)):
            result_dictionary[column_names[j]] = i[j]
        dictionaries.append(result_dictionary.copy())
    logEvent(f"Records from {table_name} accessed.")
    return dictionaries

def deleteRecord(table_name, column, check_info):
    sql = "DELETE FROM %s WHERE %s = '%s'" % (table_name, column, check_info)
    mycursor.execute(sql)
    mydb.commit()
    logEvent(f"{mycursor.rowcount}, record(s) deleted from {table_name}.")

def updateRecord(table_name, column, check_info, new_info):
    sql = "UPDATE %(table)s SET %(column)s = '%(new)s' WHERE %(column)s = '%(check)s'" % {"column": column, "table": table_name, "new":new_info, "check":check_info}
    mycursor.execute(sql)
    mydb.commit()
    logEvent(f"{mycursor.rowcount}, record(s) updated in {table_name}.")

def clearTable(table_name):
    sql = "DELETE FROM %s" % table_name
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
