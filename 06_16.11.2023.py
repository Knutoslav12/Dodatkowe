employees = ['Kowalski', 'Nowak', 'Koniecpolski']
def menu():
    print('---MENU---')
    print('     1. Lista pracowników.')
    print('     2. Sortowanie A->Z.')
    print('     3. Sortowanie Z->A.')
    print('     4. Wyszukaj pracownika.')
    print('     5. Zatrudnij pracownika.')
    print('     6. Zwolnij pracownika.')
    print('     7. Zakończ program.')
    choice = int(input('Podaj numer funkcji [1-7]: '))
    return choice
menu()
def list_e():
    c = len(employees)
    for i in range(0, c):
        print(f'{i+1}. - {employees[i]}')
if menu() == 1:
    print('Lista pracowników: ')
    list_e()
elif menu() == 2:
    print('Sortowanie A->Z: ')
    employees.sort()
    list_e()
elif menu() == 3:
    print('Sortowanie Z->A: ')
    employees.sort()
    employees.reverse()
    list_e()
elif menu() == 4:
    print('Wyszukaj pracownika: ')
elif menu() == 5:
    print('Zatrudnij pracownika: ')
elif menu() == 6:
    print('Zwolnij pracownika: ')
elif menu() == 7:
    print('ZAKOŃCZONO DZIAŁANIE PROGRAMU.')
    exit()
else:
    print('NIE MA TAKIEJ OPCJI!')
