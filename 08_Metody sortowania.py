from random import *
import os

# kolorki (konkurencja nie śpi)
class TextStyle:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# dane od użytkownika 
d = int(input(f'{TextStyle.BOLD}{TextStyle.CYAN}Podaj początek przedziału: {TextStyle.END}'))
g = int(input(f'{TextStyle.BOLD}{TextStyle.CYAN}Podaj koniec przedziału: {TextStyle.END}'))
n = int(input(f'{TextStyle.BOLD}{TextStyle.CYAN}Podaj ilość liczb do wylosowania: {TextStyle.END}'))
liczby = []

# losowanie
for i in range(n):
    liczby.append(randrange(d, g + 1))
# menu
def menu():
    print(f'{TextStyle.BOLD}{TextStyle.GREEN}Zakres losowania:{TextStyle.END} {d} - {g}')
    print(f'{TextStyle.BOLD}{TextStyle.GREEN}Ilość losowanych liczb:{TextStyle.END} {n}')
    print("-----MENU-----")
    print("     1. Sortowanie bąbelkowe - rosnąco.")
    print("     2. Sortowanie bąbelkowe - malejąco.")
    print("     3. Sortowanie przez wstawianie - rosnąco.")
    print("     4. Sortowanie przez wstawianie - malejąco.")
    print("     5. Sortowanie przez wybór (selekcję) - rosnąco.")
    print("     6. Sortowanie przez wybór (selekcję) - malejąco.")
    print("     7. Sortowanie przez zliczanie - rosnąco.")
    print("     8. Sortowanie przez zliczanie - malejąco.")
    print(f'    {TextStyle.RED} 9. Zakończ program.{TextStyle.END}')
# powrot
def powrot():
    while True:
        q = input(f'{TextStyle.BOLD}{TextStyle.CYAN}Czy chcesz powrócić do menu? [T/N]: {TextStyle.END}')
        if q == 'T' or q == 't':
            break
        elif q == 'N' or q == 'n':
            exit(0)
        else:
            continue
# sortowanie bąbelkowe rosnące
def babelkowe_r():
    for i in range(1, n):
        for j in range(0, n - 1):
            if liczby[j] > liczby[j + 1]:
                liczby[j], liczby[j + 1] = liczby[j + 1], liczby[j]
    print(f'{TextStyle.BOLD}{TextStyle.GREEN}Posortowane rosnąco liczby metodą bąbelkową: {liczby}{TextStyle.END}')
    powrot()
# sortowanie bąbelkowe malejące
def babelkowe_m():
    for i in range(1, n):
        for j in range(0, n - 1):
            if liczby[j] < liczby[j + 1]:
                liczby[j], liczby[j + 1] = liczby[j + 1], liczby[j]
    print(f'{TextStyle.BOLD}{TextStyle.GREEN}Posortowane malejąco liczby metodą bąbelkową: {liczby}{TextStyle.END}')
    powrot()
# sortowanie przez wstawianie rosnące
def wstawianie_r():
    for i in range(1, n):
        pom = liczby[i]  # zmienna pomocnicza (element z listy), "ta liczba podniesiona"
        j = i - 1
        while j >= 0 and liczby[j] > pom:
            liczby[j + 1] = liczby[j]
            j = j - 1
        liczby[j + 1] = pom
    print(f'{TextStyle.BOLD}{TextStyle.GREEN}Posortowane rosnąco liczby metodą przez wstawianie: {liczby}{TextStyle.END}')
    powrot()
# sortowanie przez wstawianie malejące
def wstawianie_m():
    for i in range(1, n):
        pom = liczby[i]  # zmienna pomocnicza (element z listy)
        j = i - 1
        while j >= 0 and liczby[j] < pom:
            liczby[j + 1] = liczby[j]
            j = j - 1
        liczby[j + 1] = pom
    print(f'{TextStyle.BOLD}{TextStyle.GREEN}Posortowane malejąco liczby metodą przez wstawianie: {liczby}{TextStyle.END}')
    powrot()
# sortowanie przez selekcję rosnące
def selekcja_r():
    l = len(liczby)
    for i in range(l):
        min_index = i
        for j in range(i + 1, l):
            if liczby[j] < liczby[min_index]:
                min_index = j
        liczby[i], liczby[min_index] = liczby[min_index], liczby[i]
    print(f'{TextStyle.BOLD}{TextStyle.GREEN}Posortowane rosnąco liczby metodą selekcji: {liczby}{TextStyle.END}')
    powrot()
# sortowanie przez selekcję malejące
def selekcja_m():
    l = len(liczby)
    for i in range(l):
        max_index = i
        for j in range(i + 1, l):
            if liczby[j] > liczby[max_index]:
                max_index = j
        liczby[i], liczby[max_index] = liczby[max_index], liczby[i]
    print(f'{TextStyle.BOLD}{TextStyle.GREEN}Posortowane malejąco liczby metodą selekcji: {liczby}{TextStyle.END}')
    powrot()
# sortowanie przez zliczanie rosnące
def zliczanie_r():
    max_value = max(liczby)
    count = [0] * (max_value + 1)
    for num in liczby:
        count[num] += 1
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    print(f'{TextStyle.BOLD}{TextStyle.GREEN}Posortowane rosnąco liczby metodą zliczania: {sorted_arr}{TextStyle.END}')
    powrot()
# sortowanie przez zliczanie malejące
def zliczanie_m():
    max_value = max(liczby)
    count = [0] * (max_value + 1)
    for num in liczby:
        count[num] += 1
    sorted_arr = []
    for i in range(max_value, -1, -1):
        sorted_arr.extend([i] * count[i])
    print(f'{TextStyle.BOLD}{TextStyle.GREEN}Posortowane malejąco liczby metodą zliczania: {sorted_arr}{TextStyle.END}')
    powrot()
# główna część programu
while True:
    os.system('cls')
    menu()
    wybor = int(input(f'{TextStyle.BOLD}{TextStyle.CYAN}Dokonaj wyboru [1-9]: {TextStyle.END}'))
    if wybor == 1:
        babelkowe_r()
    elif wybor == 2:
        babelkowe_m()
    elif wybor == 3:
        wstawianie_r()
    elif wybor == 4:
        wstawianie_m()
    elif wybor == 5:
        selekcja_r()
    elif wybor == 6:
        selekcja_m()
    elif wybor == 7:
        zliczanie_r()
    elif wybor == 8:
        zliczanie_m()
    elif wybor == 9:
        exit()
    else:
        print(f'{TextStyle.BOLD}{TextStyle.RED}Wybrano nieistniejącą opcję!{TextStyle.END}')
        input(f'{TextStyle.BOLD}{TextStyle.CYAN}Wciśnij dowolny klawisz, aby kontynuować...{TextStyle.END}')
