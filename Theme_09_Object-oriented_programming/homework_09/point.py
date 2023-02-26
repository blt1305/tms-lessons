import math

# 6.2 Вам необходимо создать класс Point (точка на координатной плоскости), у которой будет два поля: x, y.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 6.3 Добавьте метод distance_to_zero - который будет возвращать расстояние от точки до начала координат (0, 0).
# Например для точки Point(3, 4) это расстояние будет равно 5 (по теореме Пифагора)
    def distance_to_zero(self):
        return math.hypot(self.x, self.y)

# 6.4 Добавьте метод distance_to_point, который принимает другую точку, и ищет расстояние между ними.

    def distance_to_point(self, point_2):
        cathet_1 = math.fabs(point_2.x - self.x)
        cathet_2 = math.fabs(point_2.y - self.y)
        return math.hypot(cathet_1, cathet_2)

# 6.5 Скопируйте код из комментария к слайду и проверьте, что он выводит ожидаемый результат.
if __name__ == '__main__'

p1 = Point(3, 4)
p2 = Point(3, 10)
p3 = Point(10, 10)
#
print('Distance between p1 and zero point:', p1.distance_to_zero())
print('Distance between p2 and zero point:', p2.distance_to_zero())
print('Distance between p3 and zero point:', p3.distance_to_zero())
print('Distance between p1 and p1:', p1.distance_to_point(p1))
print('Distance between p1 and p2:', p1.distance_to_point(p2))
print('Distance between p2 and p1:', p2.distance_to_point(p1))
print('Distance between p1 and p3:', p1.distance_to_point(p3))
print('Distance between p2 and p3:', p2.distance_to_point(p3))
#
# Ожидаемый результат:
# Distance between p1 and zero point: 5.0
# Distance between p2 and zero point: 10.44030650891055
# Distance between p3 and zero point: 14.142135623730951
# Distance between p1 and p1: 0.0
# Distance between p1 and p2: 6.0
# Distance between p2 and p1: 6.0
# Distance between p1 and p3: 9.219544457292887
# Distance between p2 and p3: 7.0
#
