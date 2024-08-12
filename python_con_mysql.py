import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='12345678',database='face_recognition')
my_cursor=conn.cursor()

conn.commit()
conn.close()


print("Connection succesfully created!")