# 5.2 Импортируйте класс Student из первого задания
from student import Student

# 5.3 Создайте переменную students - список объектов класса Student, с разными именами и средней оценкой.
students = [student_1 := Student('Pavlov Artyom', 10),
            student_2 := Student('Isaev Maxim', 5),
            student_3 := Student('Sivtseva Vera', 7),
            student_4 := Student('Andreeva Irina', 6),
            student_5 := Student('Petrov Sergey', 9)
            ]
# 5.4 Посчитайте суммарную стипендию для всех студентов.
total_scholarship = sum([x.get_scholarship()[1] for x in students])
print(total_scholarship)

# 5.5 Посчитайте количество отличников (используйте метод is_excellent).
top_marks = [x.is_excellent() for x in students].count(True)
print(top_marks)

# *5.6 Заверните код для пунктов 4 и 5 к функции calc_sum_scholarship и get_excellent_student_count
def calc_sum_scholarship(lst_of_students):
    return print(f'Суммарная стипендия группы {sum([x.get_scholarship()[1] for x in lst_of_students])} руб.')

def get_excellent_student_count(lst_of_students):
    return print(f'Количество отличников {[x.is_excellent() for x in students].count(True)} чел.')

calc_sum_scholarship(students)

get_excellent_student_count(students)