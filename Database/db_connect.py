import mysql.connector
import KEYS

mydb = mysql.connector.connect(host="localhost", user="root", passwd=KEYS.pass_key, database="eihl")
mycursor = mydb.cursor()
