#DATABASE

#DATA Fetchall -- List of different records and each column's info in a tuple.

import mysql.connector as sql

mycon = sql.connect(host="localhost",
                    user="root",
                    database="privournal",
                    password="manimonit09")

if mycon.is_connected():
    print("Connection's strong!")
else:
    print("Not connected.")

cursor = mycon.cursor()

cursor.execute("SELECT * FROM records")
print(cursor.fetchall())


