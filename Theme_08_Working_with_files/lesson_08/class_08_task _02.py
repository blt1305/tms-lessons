#импортировать функцию my_func() с соседнего листа
from class_08_task_01.py import my_func

my_func()

from class_05_task_06.py import filter_odd_numbers
#if __name__ == '__main__':  - эту фразу нужно вставить на тот лист, откуда мы импортируем ф-цию, перед ф-цией
print(filter_odd_numbers([1,2,3,4,5]))