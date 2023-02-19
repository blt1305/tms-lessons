#Дан словарь "слово" -> число. Вывести ключ, соответствующий максимальному значению.
#Пример: {'a': 1, 'b': 2} -> 'b'.

my_dict = {'олово' : 10, 'железо' : 5, 'золото' : 13}
max_num = 0
for i, j in my_dict.items():
    if j > max_num:
        max_num = j
        result = i
print(result)
