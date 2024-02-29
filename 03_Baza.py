import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="szpital"
)


def show_databases():
    mycursor = mydb.cursor()  # wejście do bazy
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)


mycursor = mydb.cursor()
sql = "SELECT imie,nazwisko,numer_pesel FROM pacjent WHERE nazwisko like 'Kotwica' "
mycursor.execute(sql)
pacjenci = mycursor.fetchall()

c = 1
for i in pacjenci:
    print(f'{c}. {i[0]} {i[1]} {i[2]}')
    c += 1

sql1 = "INSERT INTO pacjent(id_pacjent,imie,nazwisko,numer_pesel,id_miejscowosc,id_wiek,id_oddzial,id_lekarz,historia_choroby) VALUES (NULL, 'Iza', 'Kowalska', '456978', '1', '1', '1', '1', 'BRAK')"
mycursor.execute(sql1)
mydb.commit()
