import mysql.connector as ms
con = ms.connect(user="root", password="", host="localhost", database="acro")

cr = con.cursor()
sql = "select * from student"

cr.execute(sql)
data = cr.fetchmany()#--> return all value in tuple format
for row in data:
    print(row)
print("\tRoll")
#print(data)
#print("hello........")