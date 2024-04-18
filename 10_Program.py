#https://www.w3schools.com/python/python_mysql_insert.asp

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="szpital"
)
mycursor = mydb.cursor()
print("MENU PROGRAMU")
print("_____________________________________________________")
print("    1.  Lista pacjentów")
print("    2.  Lista lekarzy")
print("    3.  Lista oddziałów")
print("    4.  Wyszukaj pacjenta według nazwiska lub nr PESEL")
print("    5.  Wyświetlenie pacjentów według oddziałów")
print("    6.  Wyświetlenie pacjentów według lekarza")
print("    7.  Rejestracja nowego pacjenta")
print("    8.  Wyrejestrowanie pacjenta")
print("    9.  Edycja danych pacjenta")
print("    10. Zakończ program")
print("_____________________________________________________")
#wybor = input("Czekam na wybór: ")

#opcja numer 1
print("----- Lista pacjentów -----")
sql = "SELECT imie,nazwisko,numer_pesel FROM  pacjent"
mycursor.execute(sql)
pacjenci = mycursor.fetchall()
licznik = 1
for pacjent in pacjenci:
  print(licznik,".",pacjent[0]," ",pacjent[1]," ",pacjent[2])
  licznik = licznik+1

#opcja numer 2
print("----- Lista lekarzy -----")
sql = "SELECT lekarz.imie_l,lekarz.nazwisko_l,oddzialy.oddzial FROM lekarz INNER JOIN oddzialy ON lekarz.id_oddzial = oddzialy.id_oddzial"
mycursor.execute(sql)
lekarze = mycursor.fetchall()
licznik = 1
for lekarz in lekarze:
  print(licznik,".",lekarz[0]," ",lekarz[1]," ",lekarz[2])
  licznik = licznik+1

#opcja numer 3
print("----- Lista oddziałów -----")
sql = "SELECT oddzialy.oddzial FROM oddzialy"
mycursor.execute(sql)
oddzialy = mycursor.fetchall()
licznik = 1
for oddzial in oddzialy:
  print(licznik,".",oddzial[0])
  licznik = licznik+1

#opcja numer 4
print("----- Wyszukiwanie pacjenta wg nazwiska lub PESEL -----")
nazwisko = input("Podaj nazwisko lub wciśnij ENTER: ")
pesel = input("Podaj PESEL lub wciśnij ENTER: ")
dane = (nazwisko, pesel)
sql = "SELECT imie, nazwisko, numer_pesel FROM pacjent Where nazwisko = %s or numer_pesel = %s"

mycursor.execute(sql,dane)

pacjenci = mycursor.fetchall()
licznik = 1
for pacjent in pacjenci:
  print(licznik,".",pacjent[0],pacjent[1],pacjent[2])
  licznik = licznik+1

#opcja numer 5
print("----- Wyświetlenie pacjentów według oddziałów -----")
sql = "SELECT imie, nazwisko, oddzial FROM pacjent INNER JOIN oddzialy ON pacjent.id_oddzial = oddzialy.id_oddzial GROUP BY oddzial, nazwisko,imie"

mycursor.execute(sql)
pacjenci = mycursor.fetchall()
licznik = 1
for pacjent in pacjenci:
  print(licznik,".",pacjent[0],pacjent[1])
  licznik = licznik+1

# opcja nr 7
print("-----Rejestracja nowego pacjenta-----")
imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
numer_pesel = input("Podaj nr PESEL: ")
for i in range(0,len(numer_pesel)):
  if ord(numer_pesel[i]) in range(49,58,1):
    continue
  else:
    print("Niepoprawny nr PESEL!")
    exit()
numer_pesel = int(numer_pesel)
miejscowosc = int(input("Podaj nr miejscowosci: "))
wiek = int(input("Podaj wiek pacjenta: "))
oddzial = int(input("Podaj nr oddzialu: "))
lekarz = int(input("Podaj numer lekarza: "))
historia = input("Podaj historię choroby: ")

val = (imie, nazwisko, numer_pesel, miejscowosc, wiek, oddzial, lekarz, historia)
# sql = ("INSERT INTO 'pacjent' ('id_pacjent', 'imie', nazwisko', 'numer_pesel', 'id_miejscowosc', 'id_wiek', 'id_oddzial', 'id_lekarz', 'historia_choroby') VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)")
sql = ("INSERT INTO pacjent (id_pacjent, imie, nazwisko, numer_pesel, id_miejscowosc, id_wiek, id_oddzial, id_lekarz, historia_choroby) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)")
mycursor.execute(sql,val)
mydb.commit()
