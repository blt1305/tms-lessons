#Дано число. Если оно положительно - выведите positive, если отрицательно - negative, если равно нулю - zero.
num = int(input('число: '))
if num > 0:
    print('positive')
elif num < 0:
    print('negative')
else:
    print('zero')