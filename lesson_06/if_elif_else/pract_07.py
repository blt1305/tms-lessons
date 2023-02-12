#Дано три числа. Вывести количество положительных чисел среди них.

my_list = list(map(float, input('Введите 3 числа через пробел: ').split()))
resalt = 0
for i in my_list:
    if i > 0:
        resalt += 1
print(resalt)

