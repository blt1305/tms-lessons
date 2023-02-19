# 2.2 Импортируйте класс Person из первого задания
from person import Person

# 2.3 Создайте переменную my_best_friend класса Person (пускай имена будут вымышленными).
# my_best_friend = Person('Ivan Ivanov', 20, 'M')
my_best_friend = Person('Ivan Ivanov', 20, 'M')     #создаем экземпляр класса

print(my_best_friend.full_name)                     #обращаемся к полям класса
print(my_best_friend.age)
print(my_best_friend.gender)

# 2.4 Выведите информацию my_best_friend на экран (метод print_person_info).
my_best_friend.print_person_info()

# 2.5 Выведите год рождения my_best_friend на экран.
print(my_best_friend.get_birth_year())
print(my_best_friend.get_birth_year_1())

