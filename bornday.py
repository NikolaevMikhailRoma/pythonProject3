print('hello')

year = input('enter Pyshkin bornyear: ')

if int(year) == 1799:
    print('Verno')
    day = input('enter Pyshkin bornday: ')
    if int(day) == 6:
        print('Verno')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')