from ssql.openconnection import *

db=getconnection()
print(db)



cursor=db.cursor()

fname=input("enter the fname")
lname=input("enter the lname")
age=int(input("enter the age"))
gender=input("press m->male f->female")
sal=int(input("enter the salary"))

sql="""insert into employee(fname,lname
,age,sex,income)values('%s','%s','%d','%c','%d') 
"""%(fname,lname,age,gender,sal)

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
