# Создайте список с элементами 1, 2 и 3.
my_list = [1,2,3]
print(my_list)
# Добавьте элемент “four” в конец списка.
my_list.append('four')
print(my_list)
# Присвойте элементу с индексом 1 значение “two”
my_list[1] = 'two'
print(my_list)
# Проверьте значение списка: [1, ‘two’, 3, ‘four’]
print(my_list)
# Добавьте в конец списка множество с элементами 5 и 6
my_list = my_list + [{5,6}]
print(my_list)
# Добавьте в множество в конце списка элемент 7
my_list[-1].add(7)
print(my_list)
# Добавьте кортеж (2.5, 2.6) в список на место с индексом 2.
my_list.insert(2, (2.5, 2.6))
# Проверьте значение списка: [1, ‘two’, (2.5, 2.6), 3, ‘four’, {5, 6, 7}]
print(my_list)


