def sprawdzanie_roku(pesel, rok):
    if (pesel[0], pesel[1]) != (rok[2], rok[3]):
        print("Podany rok urodzenia jest niezgodny z danymi zawartymi w numerze PESEL!")
        return 1
    else:
        return 0


def sprawdzanie_miesiaca(pesel, miesiac, rok):
    if int(rok) > 1999:
        if (int(pesel[2]), pesel[3]) != (int(miesiac[0]) + 2, miesiac[1]):
            print("Podany miesiąc urodzenia jest niezgodny z danymi zawartymi w numerze PESEL!")
            return 1
        else:
            return 0
    else:
        if (pesel[2], pesel[3]) != (miesiac[0], miesiac[1]):
            print("Podany miesiąc urodzenia jest niezgodny z danymi zawartymi w numerze PESEL!")
            return 1
        else:
            return 0


def sprawdzanie_dnia(pesel, dzien):
    if (pesel[4], pesel[5]) != (dzien[0], dzien[1]):
        print("Podany dzień urodzenia jest niezgodny z danymi zawartymi w numerze PESEL!")
        return 1
    else:
        return 0


def sprawdzanie_plci(pesel, plec):
    if plec == 'K':
        cyfry = [0,2,4,6,8]
        if int(pesel[9]) not in cyfry:
            print("Podana płeć jest niezgodna z danymi zawartymi w numerze PESEL!")
            return 1
        else:
            return 0
    elif plec == 'M':
        cyfry = [1,3,5,7,9]
        if int(pesel[9]) not in cyfry:
            print("Podana płeć jest niezgodna z danymi zawartymi w numerze PESEL!")
            return 1
        else:
            return 0


def suma_kontrolna(pesel):
    suma = 0
    wagi = [1,3,7,9,1,3,7,9,1,3]
    for i in range(0,10):
        liczba_pomnozona = str(int(pesel[i]) * int(wagi[i]))
        if len(liczba_pomnozona) == 2:
            liczba_pomnozona = liczba_pomnozona[1]
        suma += int(liczba_pomnozona)
    
    suma = str(suma)
    if len(suma) == 2:
        suma = suma[1]
    suma_k = 10 - int(suma)

    if str(suma_k) != pesel[10]:
        print("Suma kontrolna numeru PESEL jest nieprawidłowa!")
        return 1
    else:
        return 0


def sprawdzanie_pesel():
    pesel = input("Podaj PESEL: ")
    if len(pesel) != 11:
        print("Podany numer PESEL jest niepoprawny")
    plec = input("Podaj płeć [K/M]: ")
    rok = input("Podaj rok urodzenia (w formacie RRRR): ")
    miesiac = input("Podaj miesiąc urodzenia (w formacie MM): ")
    dzien = input("Podaj dzień urodzenia (w formacie DD): ")
    if sprawdzanie_roku(pesel, rok) == 1:
        exit()

    elif sprawdzanie_miesiaca(pesel, miesiac, rok) == 1:
        exit()
    elif sprawdzanie_dnia(pesel, dzien) == 1:
        exit()

    elif sprawdzanie_plci(pesel, plec) == 1:
        exit()
    elif suma_kontrolna(pesel) == 1:
        exit()
    else:
        print("Dobre wieści! Numer PESEL jest poprawny.")
