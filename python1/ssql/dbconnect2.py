from ssql.openconnection import *

db=getconnection()
print(db)



cursor=db.cursor()



query="""insert into employee
values('ee','c',20,'f',9000)"""


try:
    cursor.execute(query)
    db.commit()
    print("succesfully inserted")
except:
    db.rollback()
db.close()