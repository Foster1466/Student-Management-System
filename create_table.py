from sqlite3 import *

con = None
try:
    con = connect("Student.db")
    print("Connected")
    cursor = con.cursor()
    sql = "create table student(rno int primary key, name text, marks int)"
    cursor.execute(sql)
    print("table created")

except Exception as e:
    print("table creation issue", e)

finally:
    if con is not None:
        con.close()
        print("closed")
