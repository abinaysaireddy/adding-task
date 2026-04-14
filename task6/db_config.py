import mysql.connector 
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="abinay@22",
        database="logaudit_db"
    )