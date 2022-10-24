import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="", database="soham_11", port=3308)

cursor = db.cursor()

try:
    cursor.execute("show tables")
    for x in cursor:
        print(x)
    cursor.execute("select * from reminder")
    for i in cursor:
        print(i)
except:
    print("Error: unable to fetch data")
