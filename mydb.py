import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Bolanle',
   
)


# Prepare a cursor object
cursorObject = dataBase.cursor()


# Create a Database
cursorObject.execute("CREATE DATABASE safehr2")

print("Database created successfully")