#Дано: список студентов (скопируйте его в комментарии к слайду).
#Отсортируйте список по году рождения и выведите в консоль.
#Решите задачу сначала не используя lambda функцию, затем используя.

students_list = [
   ('Ivan', 'Ivanov', 2003),
   ('Petr', 'Petrov', 2005),
   ('Sidr', 'Sidorov', 2004)
]
a = sorted(students_list, key = lambda x: x[-1])
print(a)

aa = sorted(students_list, key = lambda x: -x[-1])    # можно и по убыванию
print(aa)

def students_sorted_year(lst):
   return  -lst[-1]                    #без лямбды, со своей функцией, можно и по убыванию

b = sorted(students_list, key = students_sorted_year)
print(b)