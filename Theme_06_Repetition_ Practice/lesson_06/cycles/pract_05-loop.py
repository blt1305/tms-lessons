#Дана строка. Посчитайте сколько раз в ней встречается символ "a".

my_str = list(input('введите строку: '))
result = 0
for x in my_str:
    if x == 'a':
        result += 1
print(result)
