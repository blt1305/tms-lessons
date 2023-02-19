# 4.2 Создайте класс Student, с полями full_name, average_mark (средняя оценка).
class Student:
    def __init__(self, full_name, average_mark):
        self.full_name = full_name
        self.average_mark = average_mark

# 4.3 Добавьте в класс метод get_scholarship, который подсчитывает и возвращает стипендию данного студента
# по следующему алгоритму:
# a) Если средняя оценка < 6 - вернуть 60 (рублей)
# b) Если средняя оценка >= 6, но < 8 - вернуть 80 (рублей)
# c) Если средняя оценка >= 8 - вернуть 100 (рублей)

    def get_scholarship(self):
        if self.average_mark < 6:
            return self.full_name, 60
        elif 6 <= self.average_mark < 8:
            return self.full_name, 80
        else:
            return self.full_name, 100

# 4.4 Добавить в класс метод is_excellent, который возвращает bool:
# a) True, если средняя оценка >= 9
# b) False, иначе

    def is_excellent(self):
        return self.average_mark >= 9

students = [student_1 := Student('Pavlov Artyom', 10),
            student_2 := Student('Isaev Maxim', 5),
            student_3 := Student('Sivtseva Vera', 7),
            student_4 := Student('Andreeva Irina', 6),
            student_5 := Student('Petrov Sergey', 9)
            ]

print(student_5.is_excellent())