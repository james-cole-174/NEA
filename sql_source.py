import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="^9#^QsfJRZ",
    database="mydatabase"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers_test (name VARCHAR(255), address VARCHAR(255))")

sql = "INSERT INTO customers_test (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) inserted.")

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

getAllTable("customers_test")
