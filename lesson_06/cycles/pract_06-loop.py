#Дан словарь "слово" -> число. Вывести максимальное число среди значений словаря.
#Пример: {'a': 1, 'b': 2} -> 2. Смотрите примечание в слайде.

my_dict = {'олово' : 10, 'железо' : 5, 'золото' : 13}
max_num = 0
for i, j in my_dict.items():
    if j > max_num:
        max_num = j
print(max_num)
