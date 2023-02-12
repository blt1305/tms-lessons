#Напишите функцию filter_negative_numbers, которая принимает список чисел, и возвращает новый список,
#составленный из элементов первого без отрицательных чисел,
#Пример: filter_negative_numbers([6, -5, 0, -1, 100]) -> [5, 0, 100]

def filter_negative_numbers(my_list):
    new_list = [x for x in my_list if x >= 0]
    return new_list

my_list = map(float, input('Введите несколько чисел через пробел: ').split())
print(filter_negative_numbers(my_list))


