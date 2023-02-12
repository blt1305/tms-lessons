#* Решите прошлую задачу, в которой теперь пользователь может вводить буквы в любом регистре.
#Вам по прежнему нужно удалить все гласные. При этом вывести результат нужно вывести сохранив изначальный регистр.

#Пример:
#Ввод пользователя: a B c d E F
#Результат программы: ['B', 'c', 'd', 'F']

#Используйте функции filter, lower, upper.

def remove_vowels():
    my_str = input().split()
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = list (filter(lambda x: x.lower() not in vowels, my_str))
    return result

print(remove_vowels())