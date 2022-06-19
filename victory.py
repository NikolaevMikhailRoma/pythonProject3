chetchic = 0
year = input('Ввдедите год рождения Майли Сайрус:')
if int(year) == 1992:
    chetchic+=1

year = input('Ввдедите год рождения Эйнштейна:')
if int(year) == 1879:
    chetchic+=1

year = input('Ввдедите год рождения Перикла:')
if int(year) == -429:
    chetchic+=1

year = input('Ввдедите год рождения Ньютона:')
if int(year) == 1643:
    chetchic+=1

year = input('Ввдедите год рождения Мэрилин Менсона:')
if int(year) == 1969:
    chetchic+=1

print('Процент правильных ответов: {}'.format(chetchic*100/5))
print('Процент неправильных ответов: {}'.format((5-chetchic)*100/5))