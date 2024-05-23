import mysql.connector 
try: 
    connection = mysql.connector.connect(host="127.0.0.1",port=3306,user="root",password="Daxilol2020") 
    if connection.is_connected(): 
        print("Connected to MySQL database") 
    else: 
        print("Failed to connect to MySQL database") 
except mysql.connector.Error as e: 
    print(f"Error connecting to MySQL database: {e}")