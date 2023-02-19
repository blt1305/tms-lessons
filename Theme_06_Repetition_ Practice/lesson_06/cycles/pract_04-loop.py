#Дан список чисел. Если среди них есть ноль - вывести yes, иначе no.
my_list = list(map(float, input('Введите несколько чисел через пробел: ').split()))
if 0 in my_list:
    print('yes')
else:
    print('no')
