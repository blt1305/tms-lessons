#Дан список чисел. Найти их максимальное среди них.

my_list = list(map(float, input('Введите несколько чисел через пробел: ').split()))
result = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] > result:
        result = my_list[i]
print(result)        
