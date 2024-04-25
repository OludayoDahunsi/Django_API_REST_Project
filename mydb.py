import pyodbc

# Create a connection string
conn_str = (
    #r'DRIVER = {ODBC Driver 17 for SQL Server};'
    r'SERVER = campus-quest.com;'
    r'DATABASE = master;'  # master database is typically used to create other databases
    r'UID = sa;'
    r'PWD = academic2024CS680!;'
)

# Establish a connection
cnxn = pyodbc.connect(conn_str)

# Create a cursor object
cursor = cnxn.cursor()

# Create a Database
cursor.execute("CREATE DATABASE test")

# Commit the transaction
cnxn.commit()

print("Database created successfully")
