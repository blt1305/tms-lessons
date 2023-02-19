#Скопируйте функции прошлых 5 заданий в один файл.
#Напишите программу, которая спрашивает у пользователя номер задачи, решение которой он хочет проверить,
#пользователь вводит число от 1 до 5,
#в зависимости от выбранного номера запросите у пользователя входные данные для задачи (если это нужно) и выведите ответ.
def decor_2(func):         #декоратор ко 2-й функции
    def wrapper():                                  #спрашивает 2 числа, выводит их сумму
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        result = func(a, b)
        print(f'Сумма чисел: {result}')
    return wrapper

def decor_3(func):         #декоратор к 3-й функции
    def wrapper():                                  #спрашивает 2 числа, выводит результат их сравнения
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        result = func(a, b)
        print(f'Первое число меньше второго? Ответ: {result}')
    return wrapper

def decor_4(func):         #декоратор к 4-й функции
    def wrapper():                                  #спрашивает 2 числа, выводит результат их сравнения
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        result = func(a, b)
        print(f'Результат сравнения: {result}')
    return wrapper

def decor_5(func):         #декоратор к 5-й функции
    def wrapper():                              #просит на вход несколько чисел, выводит список без отрицательных чисел
        my_list = map(float, input('Введите числа, разделённые пробелом: ').split())
        result = func(my_list)
        print(f'Мы удалили отрицательные числа из вашего списка: {result}')
    return wrapper

def hello_world():
    print('Hello world!')

@decor_2
def my_sum(a, b):
    return a + b

@decor_3
def simple_compare (a, b):
    return a < b
@decor_4
def compare (a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

@decor_5
def filter_negative_numbers(my_list):
    new_list = [x for x in my_list if x >= 0]
    return new_list


number = int(input('Введите номер задачи от 1 до 5: '))                                 #основной цикл
func_list = [hello_world, my_sum, simple_compare, compare, filter_negative_numbers]     #вводим номер
if 1 <= number <= 5:
    final_result = func_list[number - 1]()                   #в зависимости от введенного номера вызываем функцию
else:
    print('Задачи с таким номером нет.')
