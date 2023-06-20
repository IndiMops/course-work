import mysql.connector

# Підключення до MySQL сервера
mydb = mysql.connector.connect(
  host="localhost",    # адреса сервера
  user="root",         # користувач
  password="qwerty"    # пароль
)

# Створення бази даних user
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE users")

# Відображення всіх баз даних
mycursor.execute("SHOW DATABASES")
for db in mycursor:
  print(db)
