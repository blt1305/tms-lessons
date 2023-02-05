#Напишите функцию list_sum, которая принимает на вход список и возвращает сумму элементов списка.
#Использование встроенной функции sum запрещено.

def list_sum(my_list: list):
    result = 0
    for i in range(len(my_list)):
        result += my_list[i]
    return result


my_list_1 = [4, 5, 6]
print(list_sum(my_list_1))

my_list_2 = [0, 2.5, -8]
print(list_sum(my_list_2))