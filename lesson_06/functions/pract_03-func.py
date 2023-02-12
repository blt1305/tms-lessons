#Напишите функцию simple_compare, которая принимает два числа и возвращает True, если первое число меньше второго.
#Иначе возвращает False.

def simple_compare (a, b):
    return a < b

a, b = map(float, input('Введите 2 числа через пробел: ').split())
print(simple_compare(a, b))