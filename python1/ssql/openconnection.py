

import mysql.connector
def getconnection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",
        database="luminar"
    )
    return db