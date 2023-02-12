#Во всех задачах, где дан массив чисел - используйте функцию input_list чтобы получить этот массив от пользователя.
#Для тренировки предлагается сделать каждую задачу тремя способами: с помощью обычного цикла for,
#с помощью генератора списков, с помощью функции map.

def input_list_param(promt = '', sep = ' ', element_type = int):
    return list(map(element_type, input(promt).split(sep)))


#2.1 Дан список чисел. Увеличьте каждый элемент в 100 раз.
#с помощью обычного цикла for
lst_main = input_list_param()

lst_1 = []
for x in lst_main:
    lst_1.append(x * 100)
print(lst_1)

#с помощью генератора списков
lst_2 = [x * 100 for x in lst_main]
print(lst_2)

#с помощью функции map
lst_3 = list(map (lambda x: x * 100, lst_main))
print(lst_3)

#2.2 Дан список чисел. Преобразуйте этот список в список строк.
#с помощью обычного цикла for
lst_str = input_list_param(element_type=str)
lst_4 = []
for x in lst_str:
    lst_4.append(x)
print(lst_4)

#с помощью генератора списков
lst_5 = [x for x in lst_str]
print(lst_5)

#с помощью функции map
lst_6 = list (map(lambda x: x, lst_str))
print(lst_6)

#2.3 Дан список чисел. Разделите каждый элемент на 100 и округлите до целого числа (функция round).
# список lst_main в первом задании

#с помощью обычного цикла for
lst_7 = []
for x in lst_1:
    lst_7.append(round(x / 100))
print(lst_7)

#с помощью генератора списков
lst_8 = [round(x / 100) for x in lst_1]
print(lst_8)

#с помощью функции map
lst_9 = list(map(lambda x: round(x / 100), lst_1))
print(lst_9)

#2.4* Напишите свою реализацию функций my_map, возвращающую список.
#с помощью обычного цикла for
#с помощью генератора списков
#с помощью функции map

#2.5** Напишите свою реализацию функций my_map, которая вместо возвращения списка использует ключевое слово yield при генерации очередного элемента.
#с помощью обычного цикла for
#с помощью генератора списков
#с помощью функции map