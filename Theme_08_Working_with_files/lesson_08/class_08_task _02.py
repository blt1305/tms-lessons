#импортировать функцию my_func() с соседнего листа
from l_08_01 import my_func

my_func()

from lesson_05.practice_06 import filter_odd_numbers
#if __name__ == '__main__':  - эту фразу нужно вставить на тот лист, откуда мы импортируем ф-цию перед ф-цией
print(filter_odd_numbers([1,2,3,4,5]))