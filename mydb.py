import mysql.connector

database = mysql.connector.connect(
           host='localhost',
           user='root',
           passwd='Parul@8721'
        )

cursor = database.cursor()

cursor.execute("CREATE DATABASE crm_database")

print("All done")
