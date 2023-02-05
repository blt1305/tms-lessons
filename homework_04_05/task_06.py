#Напишите функцию is_palindrome, которая принимает на вход строку, и возвращает True если это палиндром, иначе False.
def is_palindrome(my_string: str) -> bool:
    my_string = my_string.lower().replace(' ','')         #все в нижний регистр, убрать пробелы
    if len(my_string) <= 1:                               #очевидно, если в строке 1 знак - она явл. палиндромом
        return True
    elif my_string[0] != my_string[-1]:                   #если первый и последний символы не равны
        return False                                       #не является палиндромом
    else:
        print(my_string[1:-1])                            #печатаю фразу для наглядности
        return is_palindrome(my_string[1:-1])             #рекурсия, проверяем с первого по предпоследний символ


my_string = 'Леша на полке клопа нашел'
print(is_palindrome(my_string))

my_string = '12345678987654321'
print(is_palindrome(my_string))

my_string = '12345678987654___321'
print(is_palindrome(my_string))