#Создать функцию sum_and_max, которая принимает на вход неопределенное количество аргументов
#и возвращает их сумму и максимальное из них. Использовать встроенные sum и max разрешено.

def sum_and_max(*args):
    return sum(args), max(args)


print(sum_and_max(1, 2, 3, 4, 5))
print(sum_and_max(5.6, 8, -6, 0, -1.2))
