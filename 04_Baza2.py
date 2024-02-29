import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="szpital"
)
mycursor = mydb.cursor()
name = input('Imię: ')
sname = input('Nazwisko: ')

sql = "INSERT INTO pacjent(id_pacjent,imie,nazwisko,numer_pesel,id_miejscowosc,id_wiek,id_oddzial,id_lekarz,historia_choroby) VALUES (NULL, %s, %s, '456978', '1', '1', '1', '1', 'BRAK')"
data = (name, sname)
mycursor.execute(sql, data)
mydb.commit()
