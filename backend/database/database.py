import mysql.connector
from mysql.connector import Error


def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",    # Your MySQL host
            user="root",         # Your MySQL username
            password="admin",     # Your MySQL password
            database="books"  # Your MySQL database name
        )
        return conn
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None


if __name__ == "__main__":
    connection = connect_db()
    if connection:
        print("Connected to the database")
        # You can perform database operations using 'connection' here
    else:
        print("Failed to connect to the database")
