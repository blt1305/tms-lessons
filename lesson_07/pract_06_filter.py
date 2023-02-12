#Во всех задачах, где дан массив чисел - используйте функцию input_list чтобы получить этот массив от пользователя.
#Для тренировки предлагается сделать каждую задачу тремя способами: с помощью обычного цикла for,
#с помощью генератора списков, с помощью функции filter.

def input_list_param(promt = '', sep = ' ', element_type = int):
    return list(map(element_type, input(promt).split(sep)))

#3.1 Дан список чисел. Удалите из него отрицательные числа.

my_list = input_list_param()
print(my_list)

#с помощью обычного цикла for
lst_1 = []
for x in my_list:
    if x >= 0:
        lst_1.append(x)
print(lst_1)

#с помощью генератора списков
lst_2 = [x for x in my_list if x >= 0]
print(lst_2)

#с помощью функции filter
lst_3 = list(filter(lambda x: x >= 0, my_list))
print(lst_3)

#3.2 Дан список чисел. Удалите из него нечётные числа.
#с помощью обычного цикла for
lst_4 = []
for x in my_list:
    if x % 2 == 0:
        lst_4.append(x)
print(lst_4)

#с помощью генератора списков
lst_5 = [x for x in my_list if x % 2 == 0]
print(lst_5)

#с помощью функции filter
lst_6 = list(filter(lambda x: x % 2 == 0, my_list))
print(lst_6)

#3.3 Дан список чисел. Выведите три числа: количество положительных чисел, поличество нулей,
#и количество отрицательных чисел. Используйте функции filter и len.
#с помощью обычного цикла for
lst_7 = [0, 0, 0]
for x in my_list:
    if x > 0:
        lst_7[0] += 1
    elif x == 0:
        lst_7[1] += 1
    else:
        lst_7[2] += 1
print(*lst_7)

#с помощью генератора списков
print(len([x for x in my_list if x > 0]), len([x for x in my_list if x == 0]), len([x for x in my_list if x < 0]))

#с помощью функции filter
lst_8 = [len (list(filter(lambda x: x > 0, my_list))), len (list(filter(lambda x: x == 0, my_list))),
        len (list(filter(lambda x: x < 0, my_list)))]
print(*lst_8)

#3.4* Напишите свою реализацию функций my_filter, возвращающую список.
#с помощью обычного цикла for
#с помощью генератора списков
#с помощью функции filter

#3.5** Напишите свою реализацию функций my_filter, которая вместо возвращения списка использует ключевое слово yield
#при генерации очередного элемента.
#с помощью обычного цикла for
#с помощью генератора списков
#с помощью функции filter