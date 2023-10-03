import mysql.connector
from mysql.connector import Error


def connect_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            databse=""
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS books")
        cursor.execute("USE books")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id CHAR(36) PRIMARY KEY,
                title VARCHAR(255),
                status ENUM('to-read', 'in-progress', 'completed')
            )
        """)

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
