#Пользователь вводит название месяца на английском.
#Выведите количество дней в этом месяце (не учитывая високосный год).
#Подсказка: понадобится создать dict: название месяца -> количество дней.

year = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31,
        'august': 31, 'september': 30, 'october': 31, 'november': 30, 'december': 31}
data = input('Please enter the month: ').lower()        #все в нижний регистр
if data not in year:                                    #если нет в словаре
    print('Error. Check the date.')                     #ошибка
else:
    print(f'{year[data]} days')
