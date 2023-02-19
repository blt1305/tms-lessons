#Пользователь вводит произвольное количество латинских букв через пробел.
#Буквы могут быть как в верхнем, так и в нижнем регистре (на результат работы это влиять не должно).
#Напишите функцию map_to_tuples, которая принимает список из этих букв и возвращает список из кортежей.
#В каждом кортеже первой должна идти буква в верхнем регистре, а второй эта же буква в нижнем.
#Выведите результат работы функции на экран. Используйте функции map, lower, upper

#Пример:
#Ввод пользователя: a B c
#Результат программы: [('A', 'a'), ('B', 'b'), ('C', 'c')]

def map_to_tuples(lst) :
    my_lst = lst.split()
    a = map(lambda x: x.upper(), my_lst)
    b = map(lambda x: x.lower(), my_lst)
    result = list(zip(a, b))
    return  result

a = map_to_tuples(input())
print(a)
