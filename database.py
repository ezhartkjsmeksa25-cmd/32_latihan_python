import mysql.connector

def connect_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ezhar2010",  # Password root MySQL
            database="db_login"     # Nama database
        )
        if db.is_connected():
            return db
    except mysql.connector.Error as err:
        print(f"❌ Gagal terhubung ke database: {err}")
        return None