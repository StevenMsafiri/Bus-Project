import mysql.connector
from mysql.connector import Error

# Database connection
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password='    ',  # Replace with your MySQL password
            database='todos'  # Replace with your database name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Connect to the database
connection = create_connection()
cursor = connection.cursor()
