from db import get_connection
from student import student
from user_class import user

# entrire crud

def add_stud():
    conn = get_connection()
    cursor = conn.cursor()  
    
    name = input("Enter yr name: ")
    age = int(input("Enter yr age: "))
    email = input("enter yr mail id: ")
    
    obj = student(name, age, email)
    
    query = "insert into student (name,age,email) values(%s,%s,%s)"  
    values = (obj.name, obj.age, obj.email)
    
    cursor.execute(query, values)
    conn.commit()
    
    cursor.close()  
    conn.close()
    
    print("student added")

#add_stud()

def add_users(self):
    conn = get_connection()
    cursor = conn.cursor()
    username = input("enter yr username")
    password = input("enter yr pwd")
    role = input("enter yr role")
    obj = user(username,password,role)
    query = "insert into login(username,password,role) values(%s,%s,%s)"
    values = (obj.username,obj.password,obj.role)
    cursor.execute(query,values)
    conn.commit()
    print("added")

def view_stud():
     conn = get_connection()
     cursor = conn.cursor()
     cursor.execute("select * from student")
     rows = cursor.fetchall()
     return rows
#print(view_stud())
