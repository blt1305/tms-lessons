# 3.2 Импортируйте класс Person из первого задания
from person import Person

# 3.3 Создайте переменную my_friends - список из объектов класса Person.
# Добавьте в него некоторое количество вымышленных друзей с разными именами, возрастом и полом.
pers_1 = Person('Serhio Libre', 32, 'M')
pers_2 = Person('Petr Petrov', 25, 'M')
pers_3 = Person('Pomidora Tomato', 22, 'F')
pers_4 = Person('Abuela', 65, 'F')

# 3.4 Выведите информацию о каждом друге на экран.
my_friends = [pers_1, pers_2, pers_3, pers_4]
for x in my_friends:
    x.print_person_info()

# *3.5 Найдите среди друзей самого старшего, выведите информацию о нём на экран.
friends_tuple = [(x.__dict__['full_name'], x.__dict__['age']) for x in my_friends]        #список из кортежей (имя, возраст)
friends_tuple_sorted = sorted(friends_tuple, key=lambda x: (x[1]), reverse=True)                #сортировка по убыванию
print(f'Самый старший друг - {friends_tuple_sorted[0][0]}, возраст - {friends_tuple_sorted[0][1]} лет.')


# *3.6 Выведите на экран информацию о всех друзьях мужского пола (можно использовать функцию filter,
# либо генератор списков).
print([x.__dict__ for x in my_friends if x.gender == 'M'])

# *3.7 Заверните код из пунктов 5 и 6 в функции get_oldest_pearson и filter_male_person соответственно.
def get_oldest_pearson(lst_of_people: list):
    fr_tpl = [(x.__dict__['full_name'], x.__dict__['age']) for x in lst_of_people]
    fr_tpl_sorted = sorted(fr_tpl, key=lambda x: (x[1]), reverse=True)
    return print(f'Самый старший друг - {fr_tpl_sorted[0][0]}, возраст - {fr_tpl_sorted[0][1]} лет.')


def filter_male_person(lst_of_people: list):
    return print([x.__dict__ for x in lst_of_people if x.gender == 'M'])


get_oldest_pearson(my_friends)
filter_male_person(my_friends)