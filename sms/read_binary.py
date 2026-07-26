# file = open("image.png","rb")
# data= file.read()
# print(data)
# file.close()
# with open ("copy_img.png","wb") as file:
#     file.write(data)

import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "sujal@1234",
    database = "sms_linkcode"
)
print("db connected")

cursor = conn.cursor()

#table create
# cursor.execute("create table files(id int primary key auto_increament, filename varchar(20), filedata LONGBLOG)")
# print("table created")

# read binary data

# file = open("image.png","rb")
# data= file.read()
# print(data)
# file.close()

# query = "insert into files(filename,filedata) values(%s,%s)"
# values = ("image.png", data)
# cursor.execute(query,values)
# conn.commit()
# print("data save")

# featch
cursor.execute("select * from files where id = %s, (1,)")
record = cursor.fetchone()
if record:
    filename = record[1]
    filedata = record[2]
    #save to sys
    fiel = open(filename, "wb")
    file.write(filedata)
    file.close()
    print("downloaded")
else:
    print("record not found")
cursor.close()
conn.close()



