import mysql.connector as ms
con = ms.connect(user="root", password="", host="localhost", database="acro")
cr = con.cursor()
sql = "insert into student values(101, 'kamal', 67)"
cr.execute(sql)
con.commit()
print("hello........")