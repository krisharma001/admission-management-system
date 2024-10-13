import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",   # MySQL username
        password="daal bhadwe",   # MySQL password
        database="admission_system"
    )
