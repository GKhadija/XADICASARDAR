import mysql.connector 
# try:
connection = mysql.connector.connect(host = "127.0.0.1", port=3306, user = "root",password = "Daxilol2020")

#     if connection.is_connected(): 
#         print("Connected to MySQL database") 
#     else: 
#         print("Failed to connect to MySQL database") 
# except mysql.connector.Error as e: 
#     print(f"Error connecting to MySQL database: {e}")
    
cursor=connection.cursor()
# cursor.execute('CREATE DATABASE my_db')
create_course_table_query="""
CREATE TABLE my_db.Pizza(
    id INT PRIMARY KEY,
    name VARCHAR(40),
    release_year DATE,
    direction VARCHAR(40)
)
INSERT INTO my_db.Pizza (id,name,release_year,direction)
VALUES
(12, "qarisiq", 2024, "bayil"),
(21,"Peperoni", 2024,, "Ecemi"),
(23,"Pendirli",2022,"Azadliq")
"""

cursor.execute(create_course_table_query)
