#Пользователь вводит произвольное число. Посчитайте сумму цифр этого числа используя операторы % и //
#Пример для числа 12.
#Ответ должен быть получен примерно так:
#answer = 12 % 10  # 2
#answer += 12 // 10  # 1
#print(answer)  # 3

#вариант решения 1. Просто складываем все цифры числа, итог к однозначному числу не приводим
my_num_1 = int(input('Введите число: '))
result = 0                      #переменная, где будем накапливать результат
my_list = []                    #список цифр для контроля
while my_num_1 > 9:             #пока наше число > 9, т.е. однозначное
    result += my_num_1 % 10       #в результат пойдет остаток от деления на 10, т.е. последняя цифра
    my_list.append(my_num_1 % 10) #для контроля эту же цифру скидываем в список
    my_num_1 = my_num_1 // 10       #обновляем наше число, оно станет короче на одну цифру после целочисленного деления на 10
else:                           #после штатного завершения цикла добавим к результату оставшуюся цифру (первую в нашем числе)
    result += my_num_1
    my_list.append(my_num_1)      #добавим в список
    print(my_list)
print(f'Вариант 1: {result}')     #итог, получила 42, по условию задачи делать с жтим ничего не требуется


#вариант 2. Полученный итог тоже свернем, сложив все цифры
def sum_of_digits(my_num : int) -> int:     #функция, схема цикла та же, что и вверху
    result = 0
    while my_num > 9:
        result += my_num % 10
        my_num = my_num // 10
    else:                                   #штатное завершение цикла
        result += my_num                    #добавляем оставшуюся цифру
    if result > 9:                          #если результат больше 9,
        return sum_of_digits(result)        #рекурсия, применим функцию к результату
    return result

my_num_2 = int(input('Введите число: '))
print(f'Вариант 2: {sum_of_digits(my_num_2)}')
