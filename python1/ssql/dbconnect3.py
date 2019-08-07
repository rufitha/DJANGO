from ssql.openconnection import *

db=getconnection()
print(db)



cursor=db.cursor()

try:
    cursor.execute("select * from employee where fname like 'b%'")
    # cursor.execute("update employee where ")
    myresult= cursor.fetchall()

    for x in myresult:
        print(x)
except Exception as e:
    print(e.args)
finally:
    db.close()