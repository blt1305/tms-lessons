#Задача 3. Полиморфизм

# 3.1 Скопируйте классы из прошлого задания.

class Animal():
   def __init__(self, name, age):
      self.name = name
      self.age = age


   def make_voice(self):
      print('Я не знаю какой звук мне издать, я же абстрактное животное.')


class Dog(Animal):
   def __init__(self, name, age, breed):
      super().__init__(name, age)
      self.breed = breed


   def make_voice(self):
      print('Гав')

# 3.2 Добавьте в класс Animal метод make_voice, который печатает на экран "Я не знаю какой звук мне издать,
# я же абстрактное животное".

# 3.3 Добавьте в класс Dog метод make_voice, который печатает на экран строку "Гав".

# 3.4 Создайте класс Cat, наследующийся от Animal.
# Помимо полей name и age у класса должно быть поле is_vaccinated (привит или нет).

class Cat(Animal):
   def __init__(self, name, age, is_vaccinated):
      super().__init__(name,age)
      self.is_vaccinated = is_vaccinated

# 3.5 Добавьте в класс Cat метод make_voice, который печатает на экран строку "Мяу".
   def make_voice(self):
      print('Мяу')

# 3.6 Перепишите код из комментария к слайду, удостоверьтесь что он выводит ожидаемый результат.

animals = [
   Animal('Животное', 5), # создание абстрактного животного довольно бессмысленно, но для понимания ООП это ок
   Dog('Шарик', 10, 'Доберман'),
   Cat('Матроскин', 9, True),
]
for animal in animals:
   animal.make_voice()



# Ожидаемый результат:
# Я не знаю какой звук мне издать, я же абстрактное животное
# Гав
# Мяу


