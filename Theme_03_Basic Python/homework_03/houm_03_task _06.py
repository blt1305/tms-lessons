#Пользователь вводит месяц и число. Выведите True, если такой день есть в году.

my_guide = {'янв': 31, 'фев': 28, 'мар': 31, 'апр': 30, 'мая': 31, 'июн': 30, 'июл': 31,
            'авг': 31, 'сен': 30, 'окт': 31, 'ноя': 30, 'дек': 31}      #справочник по дням в м-це
data = input('Введите дату, месяц через пробел: ').split()              #введенные данные делю по пробелу

#беру нулевой эл-т, перевожу его в числовой формат и сравниваю с ключом словаря,
#причем беру только первые три буквы, т.к. слово меняется при склонении ("мая" в словаре изначально)
print(0 < int(data[0]) <= my_guide[data[1][0:3]])       #ноль не включаем, последнее число месяца включаем