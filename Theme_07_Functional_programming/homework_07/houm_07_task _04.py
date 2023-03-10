#Пользователь вводит произвольное количество слов через пробел. Затем (на следующей строке) вводит один символ (разделитель).
#Вам нужно написать функцию my_join, которая принимает список из строк и символ-разделить, и возвращает строку,
#в которой все слова из списка соединены через символ разделитель.

#Пример ввода пользователя:
#hello this is my string
#@

#Вывод программы: hello@this@is@my@string
#Используйте функцию reduce.

from functools import reduce
# def my_join(lst, sep):
#     my_list = lst.split()
#     my_list_1 = [x + sep for x in my_list]
#     result = reduce(lambda x, y: x + y, my_list_1)
#     return result

def my_join(lst, sep):
    #my_list = lst.split()
    #my_list_1 = [x + sep for x in my_list]
    result = reduce(lambda x, y: x + sep + y, lst)
    return result


a = input('введите строку: ').split()
b = input('введите символ-разделитель: ')
print(my_join(a, b))
