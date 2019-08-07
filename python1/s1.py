#databse connection
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password"
)

#prepare a cursor object using cursor() method

cursor = db.cursor()

#execute sql qry using execute() m ethod

cursor.execute("SELECT VERSION()")

#fetch a single row using fetchone() method

data=cursor.fetchone()
print("database version:%s" % data)

db.close()