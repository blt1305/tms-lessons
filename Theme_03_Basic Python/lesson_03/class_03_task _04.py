#Пользователь вводит в консоль строку.
#Если выведенная строка является палиндромом - выведите True. Если не является - выведите False.
#Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.

#вводим строку, одновременно делаем все буквы маленькими, убираем пробелы
data = input('Введите что-нибудь: ').lower().replace(' ', '')
print(data == data[::-1])       #сравниваем строку со строкой в обратном порядке [старт:стоп:шаг]

