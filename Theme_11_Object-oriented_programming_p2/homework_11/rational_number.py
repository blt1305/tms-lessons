def get_nod(a, b):        #НОД для двух чисел
    if b == 0:
        raise ZeroDivisionError("Число b не может быть равно 0")
    while a % b != 0:
        if a < b:
            a, b = b, a
        a = a % b
    return b

# 1. Создайте класс Rational (рациональное число) с двумя приватными полями __numerator (числитель)
# и __denominator (знаменатель).


class Rational:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

# 2. Добавьте в класс методы-атрибуты (@property) numerator и denominator,
# которые возвращают __numerator и __denominator соответственно.

# Возможно у вас возникнет вопрос, зачем такие сложности, почему нельзя просто сделать поля публичными?
# Ответ: тогда их можно было бы изменить извне, а мы бы хотели чтобы извне можно было только читать их значения,
# но не записывать

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

# 3. Добавьте в класс магически метод __str__, который должен возвращать строку в формате "{numerator} / {denominator}".
# Теперь вы можете передавать объект Rational в функцию print и он будет напечатан так, как вы определили это.

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'

# Переопределение магического метода оператора равенства

    def __eq__(self, other: 'Rational') -> bool:
        return self.__numerator == other.__numerator and self.__denominator == other.__denominator

# 4. Переопределите магические методы умножения и деления. Они должны принимать второй объект типа Rational
# и возвращать новый объект того же типа. Для проверки можно использовать онлайн калькулятор дробей.
    def __mul__(self, other: 'Rational') -> 'Rational':
        return Rational(self.__numerator * other.__numerator , self.__denominator * other.__denominator)

    def __truediv__(self, other: 'Rational') -> 'Rational':
        return Rational(self.__numerator * other.__denominator, self.__denominator * other.__numerator)

# *5. Переопределите магические методы сложения и вычитания. Не забудьте привести дроби к
# одинаковому знаменателю (шпаргалка).
    def __add__(self, other):
        return Rational((self.__numerator * other.__denominator + other.__numerator * self.__denominator),
                        (self.__denominator * other.__denominator))

# *6. Переопределите магические методы сравнения для операторов ==, !=, >=, <=, <, >.
# Возможно в процессе тестирования ваши дроби не сокращаются автоматически. Например в результате сложения
# Rational(1, 4) + Rational(1, 4) получится дробь 2 / 4, однако её можно сократить (нормализовать).




# *7. Напишите метод __normalise, который ничего не принимает (кроме self), и сокращает дробь.
# Для этого необходимо найти НОД (наибольший общий делитель) и разделить на него числитель и знаменатель.
# Вычислить НОД можно как максимальное число от 2 до min(nominator, denominator),
# на которые числитель и знаменатель делятся без остатка.

    def __normalise(self):
        a = abc(self.__numerator)
        b = abc(self.__denominator)
        if b == 0:
            raise ZeroDivisionError("Знаменатель дроби не может быть равен 0")
        while a % b != 0:
            if a < b:
                a, b = b, a
            a = a % b
        nod = b
        self.__numerator /= nod
        self.__denominator /= nod

# 8. Используйте метод __normalise в конструкторе. Убедитесь что код print(Rational(2, 4)) печатает на экран "1 / 2".



# 9. Добавьте в метод __normalise нормализацию для знака (знаменатель всегда должен быть положительным,
# а знак дроби определяется знаком числителя). Например код print(Rational(-1, -2)) должен выводить на экран "1 / 2".




# 10. Посчитайте значение выражения, используя только объекты класса Rational. Убедитесь что результат равен 1573 / 800.










if __name__ == '__main__':
    my_num = Rational(100, 200)
    assert str(Rational(10, 20)) == '10 / 20'
    assert Rational(5, 6) == Rational(5, 6)
    assert Rational(1, 2) / Rational(3, 4) == Rational(4, 6)
    print(Rational(4, 6))
    sd_1 = Rational(1, 4)
    sd_2 = Rational(3, 2)
    sd_3 = Rational(1, 8)
    sd_4 = Rational(156, 100)
    assert sd_1 * (sd_2 + sd_3) + sd_4 == Rational(1573, 800)







