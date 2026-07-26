from crud import *

def login():
    conn=get_connection()
    cursor = conn.cursor
    username = input("enter yr username")
    pasword = input("enter yr pass")
    cursor.execute("select role from login where username=%s", (username,))
    row = cursor.fetchone()
    if row[0]=='admin':
        print("1.add user to main app\n2.add studet\n.view student\n4.exit\n")
    elif row[0]=='user':
        print("1 view student")

login()
