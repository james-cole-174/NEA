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
print(mycursor.rowcount, "record inserted.")

def getAllTable(table_name):
    mycursor.execute("SELECT * FROM (%s)" % table_name)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

getAllTable("customers_test")