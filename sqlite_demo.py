import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT
    )
""")
conn.commit()

# Insert
cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
               ("Rahul", 21, "C++"))
cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
               ("Anjali", 24, "JavaScript"))
conn.commit()

cursor.execute("SELECT id, name, age FROM students")
rows = cursor.fetchall()
print("All Students:")
for row in rows:
    print(row)

# 4. Update
cursor.execute("UPDATE students SET age = ? WHERE name = ?", (25, "Rahul"))
conn.commit()

# Delete
cursor.execute("DELETE FROM students WHERE name = ?", ("Anjali",))
conn.commit()

cursor.execute("SELECT id, name, age FROM students")
print("\nAfter Update & Delete:")
for row in cursor.fetchall():
    print(row)
conn.close()