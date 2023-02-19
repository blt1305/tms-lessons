#Вывести на экран числа кратные 5 от 0 до 100 включительно.
#1.1 Сделать это с помощью функции range с шагом 5
#1.2 Сделать это с помощью функции range c шагом 1 и вложенным if

my_list_1 = []
for i in range(0, 101, 5):
    my_list_1.append(i)
print(my_list_1)

my_list_2 = []
for i in range(101):
    if i % 5 == 0:
        my_list_2.append(i)
print(my_list_2)
