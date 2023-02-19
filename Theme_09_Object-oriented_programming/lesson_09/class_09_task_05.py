# * Задача 5. Инкапсуляция
import random
# 5.1 Скопируйте класс из предыдущего задания.

class User():
    def __init__(self, login, password):
        self.login = login
        self.__key = random.randint(1, 1000)
        self.__password = self.__encode(password)


    def check_password(self, user_password):
        user_password = self.__encode(user_password)
        return user_password == self.__password

    def reset_password(self, new_password):
        new_password = self.__encode(new_password)
        self.__password = new_password

# 5.2 Давайте теперь хранить пароль в зашифрованном виде. Создайте новое поле __key = random.randint(1, 1000)
    #def __init__(self, key):


# 5.3 Добавьте приватный метод __encode, шифрующий строку:
# def __encode(self, s):
#     return ''.join([chr(ord(i) ^ self.__key) for i in s])

    def __encode(self, s):
        return ''.join([chr(ord(i) ^ self.__key) for i in s])

# 5.4 Используйте метод __encode:
# В конструкторе, при инициализации поля __password
# В методе check_password
# В методе reset_password



# 5.5 Перепишите код из комментария к ПРЕДЫДУЩЕМУ СЛАЙДУ, удостоверьтесь что результат такой же.
my_user = User('dima_buevich', 'SuperSecretP@ssword')

print(my_user.login)
# print(my_user.__password)  # так нельзя, будет ошибка

print(my_user.check_password('WrongPassword'))
print(my_user.check_password('SuperSecretP@ssword'))

my_user.reset_password('NewP@ssword')

print(my_user.check_password('SuperSecretP@ssword'))
print(my_user.check_password('NewP@ssword'))



# Ожидаемый результат:
# dima_buevich
# False
# True
# False
# True


# 5.6 В этом и есть сила инкапсуляции, мы можем как угодно менять внутреннюю реализацию нашего класса,
# при этом не нужно менять код, который использовал наш класс.


