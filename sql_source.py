import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="^9#^QsfJRZ",
    database="mydatabase"
)

mycursor = mydb.cursor()

##############################
# ADD LOG FILE #
##############################

def getAllTable(table_name):
    sql = "SELECT * FROM %s" % (table_name)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def deleteRecord(table_name, column, check_info):
    sql = "DELETE FROM %s WHERE %s = '%s'" % (table_name, column, check_info)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

def updateRecord(table_name, column, check_info, new_info):
    sql = "UPDATE %(table)s SET %(column)s = '%(new)s' WHERE %(column)s = '%(check)s'" % {"column": column, "table": table_name, "new":new_info, "check":check_info}
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) updated")

def clearTable(table_name):
    sql = "DELETE FROM %s" % table_name
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

def addRecordToTable(table_name, info_dict):
    formatted_keys = ", ".join(info_dict.keys())
    formatted_values = "', '".join(info_dict.values())
    sql = f"INSERT INTO {table_name} ({formatted_keys}) VALUES ('{formatted_values}')"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) inserted.")
