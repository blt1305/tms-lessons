#Пользователь вводит год.
#Если введённый год високосный - выведите True, иначе - False.

data = int(input('Введите год: '))      #проверяем кратность 4-м
print(data % 4 == 0)