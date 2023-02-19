#Даны три числа. Если они все больше 0 - вывести yes, иначе - no

a, b, c = map(float, input('Введите 3 числа через пробел: ').split())
if a > 0 and b > 0 and c > 0:
    print('yes')
else:
    print('no')