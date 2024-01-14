import mysql.connector
mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    port='3306',
    database='szpital'
)
mycursor = mydb.cursor()
mycursor.execute('SHOW DATABASES')
data = mycursor.fetchone()

for x in mycursor:
    print(x)

mycursor.execute('SELECT imie, nazwisko FROM pacjent')
result = mycursor.fetchall()

#for x in result:
#    print(x)

c = 1
for x in result:
    print(f'{c} - {x[0]} {x[1]}')
    c += 1
