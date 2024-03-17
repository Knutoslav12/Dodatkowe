list = [['Styczeń'], ['Luty'], ['Marzec'], ['Kwiecień'], ['Maj'], ['Czerwiec'], ['Lipiec'], 
        ['Sierpień'], ['Wrzesień'], ['Październik'], ['Listopad'], ['Grudzień']]
list[0][1] = int(input(f'Temperatura - {list[0][0]}: '))
list[1][1] = int(input(f'Temperatura - {list[1][0]}: '))
# print(f'{list[0][0]} = {list[0][1]} st. C')
# print(f'{list[1][0]} = {list[1][1]} st. C')

for i in range(0,12):
    list[i][1] = int(input(f'Temperatura - {list[i][0]}: '))
print(list.readlines())