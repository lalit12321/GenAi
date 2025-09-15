import mysql.connector as ms
con = ms.connect(user="root",password="",host="localhost",database="acro")
cr = con.cursor()
print("Connection Successfully")
create_table_query = """
CREATE TABLE IF NOT EXISTS vehicle (

);
"""
cr.execute(create_table_query)
con.commit()
print("Table created successfully")
con.close()