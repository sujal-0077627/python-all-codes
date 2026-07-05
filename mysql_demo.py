import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="school"
)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), age INT)")
cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Ram", 20))
conn.commit()

cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)
conn.close()