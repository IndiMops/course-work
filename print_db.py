import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="qwerty",
  database="users"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
