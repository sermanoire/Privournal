#DATABASE

#DATA Fetchall -- List of different records and each column's info in a tuple.

from dotenv import load_dotenv
import os
load_dotenv()

load_dotenv()
import mysql.connector as sql

mycon = sql.connect(host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USER"),
                    database=os.getenv("DB_NAME"),
                    password=os.getenv("DB_PASSWORD"))

if mycon.is_connected():
    print("Connection's strong!")
else:
    print("Not connected.")

cursor = mycon.cursor()

cursor.execute("SELECT * FROM records")
print(cursor.fetchall())


