from ssql.openconnection import *

db=getconnection()
print(db)



cursor=db.cursor()

cursor.execute("drop table if exists employee")

sql= """create table employee (
    fname char(20),
lname char(20),
age int,
sex char(1),
income float)"""

cursor.execute(sql)

db.close()