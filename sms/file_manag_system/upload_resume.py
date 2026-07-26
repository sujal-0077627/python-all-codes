from db import connection 
def upload():
    path = input("enter yr path to upload resume \n")
    fiel = open(path, "rb")
    data = file.read()
    file.close()
    filename = path.split("\\")[-1]
    extension = file.split('_')[-1]
    conn = connection()
    cursor = conn.cursor()
    query = "insert into files(filename,filetype,filedata)"



