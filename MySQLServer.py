import mysql.connector
from mysql.connector import Error

def Create_Database():
  try:
    connection = mysql.connector.connect(host="localhost", user="root", password="tilammg1234")

    if connection.is_connected():
      myCursor = connection.cursor()

      myCursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
      print("Database 'alx_bokk_store' created successfully!")
  except Error as e:
    print(f"Database Connection Failed: {e}")
  
  finally:
    if 'connection' in locals() and connection.is_connected():
      myCursor.close()
      connection.close()

if __name__ == "__main__":
  Create_Database()