#Пользователь вводит целое трёхзначное число. Выведите сумму чисел числа.

data = input('Введите трехзначное число: ')
my_list = list(data)
resalt = int(my_list[0]) + int(my_list[1]) + int(my_list[2])
print(resalt)
