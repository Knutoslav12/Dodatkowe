import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="szpital")
mycursor = mydb.cursor()


def menu():
    while True:
        print("MENU")
        print("1. Lista pacjentów.")
        print("2. Lista lekarzy.")
        print("3. Lista oddziałów.")
        print("4. Wyszukaj pacjenta wg nazwiska lub nr PESEL.")
        print("5. Wyświetlenie pacjentów wg oddziałów.")
        print("6. Wyświetlenie pacjentów wg lekarza.")
        print("7. Rejestracja nowego pacjenta.")
        print("8. Wyrejestrowanie pacjenta.")
        print("9. Edycja danych pacjenta.")
        print("10. Zakończ program")
        wybor = int(input("Podaj nr opcji: "))
        if wybor in range(1, 11):
            return wybor


def opcja_1():
    sql = "SELECT imie,nazwisko,numer_pesel FROM pacjent"
    mycursor.execute(sql)
    pacjenci = mycursor.fetchall()
    licznik = 1
    for pacjent in pacjenci:
        print(f'{licznik}. {pacjent[0]} {pacjent[1]} {pacjent[2]}')
        licznik += 1


def opcja_2():
    sql = "SELECT lekarz.imie_l, lekarz.nazwisko_l, oddzialy.oddzial FROM lekarz INNER JOIN oddzialy ON " \
          "lekarz.id_oddzial = oddzialy.id_oddzial "
    mycursor.execute(sql)
    lekarze = mycursor.fetchall()
    licznik = 1
    for lekarz in lekarze:
        print(f'{licznik}. {lekarz[0]} {lekarz[1]} {lekarz[2]}')
        licznik += 1


def opcja_3():
    sql = "SELECT oddzial FROM oddzialy"
    mycursor.execute(sql)
    oddzialy = mycursor.fetchall()
    licznik = 1
    for oddzial in oddzialy:
        print(f'{licznik}. {oddzial[0]}')
        licznik += 1


def opcja_4():
    nazwisko = input("Podaj nazwisko: ")
    pesel = input("Podaj nr PESEL: ")
    sql="""SELECT pacjenci.imie, pacjenci.nazwisko, pacjenci.numer_pesel FROM pacjent WHERE nazwisko = '%s' or numer_pesel = '%s' """
    mycursor.execute(sql)
    dane = mycursor.fetchall()
    licznik = 1
    for pacjent in dane:
        print(f'{licznik}. {pacjent[0]} {pacjent[1]} {pacjent[2]}')
        licznik += 1


