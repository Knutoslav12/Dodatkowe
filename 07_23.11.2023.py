list = ['Nowak', 'Kowalski', 'Koniecpolski']
while True:
    print('---MENU---')
    print('     1. Lista pracowników.')
    print('     2. Sortowanie A->Z.')
    print('     3. Sortowanie Z->A.')
    print('     4. Wyszukaj pracownika.')
    print('     5. Zatrudnij pracownika.')
    print('     6. Zwolnij pracownika.')
    print('     7. Zakończ program.')
    choice = int(input('Podaj numer funkcji [1-7]: '))

    if choice == 1:
        num = 1
        for i in list:
            print(f'     {num} - {i}')
            num += 1
        input()
    elif choice == 2:
        list.sort()
        num = 1
        for i in list:
            print(f'     {num} - {i}')
            num += 1
        input()
    elif choice == 3:
        list.sort()
        list.reverse()
        num = 1
        for i in list:
            print(f'     {num} - {i}')
            num += 1
        input()
    elif choice == 4:
        search = input('Szukanie pracownika: ')
        count = 0
        for i in list:
            if i == search:
                print(i)
                count += 1
        if count == 0:
            print(f'Nazwisko {search} nie znajduje się na liście!')
        input()
    elif choice == 5:
        surname = input('Zatrudnij pracownika: ')
        list.append(surname)
        input()
    elif choice == 6:
        surname = input('Zwolnij pracownika: ')
        count = 0
        for i in list:
            if i == surname:
                count += 1
        if count >= 1:
            list.remove(surname)
        else:
            print(f'Nazwisko {surname} nie znajduje się na liście!')
        input()
    elif choice == 7:
        exit(0)
    else:
        print(f'Opcja nr {choice} nie istnieje!')
        input()
