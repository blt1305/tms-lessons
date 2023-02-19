#Дан список чисел. Найти их сумму.

my_list = list(map(float, input('Введите несколько чисел через пробел: ').split()))
resalt = 0
for x in my_list:
    resalt += x
print(resalt)