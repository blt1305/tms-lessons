#https://www.youtube.com/watch?v=Vk-tGND2bfc (принцип стеков)

#Калькулятор выполняет действия +, -, *, /, //, %, принимает скобки.
#НЕ выполняет операции с отрицательными числами.
#
NUMERATES = list(map(str, list(range(0, 10)))) + ['.']        #список цифр для парсинга
def get_prior(x):
    '''Расстановка приоритетов арифметических операций.
    У закрывающейся скобки самый высокий, т.к. при закрытии скобки должны выполниться действия в скобках.
    У открывающейся - нулевой.'''
    if x == ')':
        return 4
    elif x == '^':
        return 3
    elif x in ['*', '/', '%', '$']:
        return 2
    elif x in ['+', '-']:
        return 1
    elif x == '(':
        return 0


def get_list(str_in):
    '''Парсим строку по знакам арифметических операций.
       Внутри цикла формируем список из (индекс эл-та, элемент), затем выбираем из него пары, соответствующие НЕ цифрам
       (т.е. знакам арифм.операций).
       И пока в обрабатываемой строке есть такие знаки:
       берем фрагмент строки от начала до знака, добавляем в формируемый список,
       добавляем сам арифм. знак в формируемый список,
       режем вход. строку - формируем от арифм. знака до конца строки
       Если больше арифм. знаков в строке не осталось - оставшуюся часть строки добавляем в список, выходим из цикла.'''
    if '**' in str_in:                          #двусимвольные операторы меняем на односимвольные
        str_in = str_in.replace('**', '^')
    elif '//' in str_in:                        #двусимвольные операторы меняем на односимвольные
        str_in = str_in.replace('//', '$')
    elif ' ' in str_in:                         #удаляем случайно введенные пробелы
        str_in = str_in.replace(' ', '')
    elif ',' in str_in:                         #заменяем запятые на точки
        str_in = str_in.replace(',', '.')
    elif str_in[0] == '-':
        print("Калькулятор не работает с отрицательными числами.")
    elif '(-' in str_in or '( -' in str_in:
        print("Калькулятор не работает с отрицательными числами.")

    lst_out = []
    while True:
        data = list(enumerate(str_in))       #пара  индекс - символ
        data_1 = [x for x in data if x[1] not in NUMERATES] #пара индекс - символ для НЕ цифр
        if len(data_1) > 0:                                 #пока есть такие пары строке
            piece_of_string = str_in[0 : data_1[0][0]]      #формируем фрагмент строки от начала до первого арифм.знака
            lst_out.append(piece_of_string)                 #добавляем этот фрагмент в список
            lst_out.append(data_1[0][1])                    #добавляем в список первый знак арифм. операции
            str_in = str_in[(data_1[0][0]+1) : ]            #режем строку - от арифм. знака до конца строки
        else:
            lst_out.append(str_in)                          #если арифм.знаков больше нет - добавляем хвостик в список
            break
    while '' in lst_out:                                    #пустые элементы, кот. появляются перед скобками, удаляем
        lst_out.remove('')
    return lst_out


def get_number(lst):
    ''' Преобразовать элементы списка в цифры
        Вначале пробуем в тип int, если не получилось - пробуем в тип float,
        или оставляем как есть, в строчном формате.'''
    for i in range(len(lst)):
        try:
            lst[i] = int(lst[i])
        except:
            try:
                lst[i] = float(lst[i])
            except:
                lst[i] = lst[i]
    return lst


def get_count(lst):
    '''Ф-ция для арифметических вычеслений'''
    for i in range(len(lst)):
        if lst[1] == '+':
            return lst[0] + lst[2]
        elif lst[1] == '-':
            return lst[0] - lst[2]
        elif lst[1] == '*':
            return lst[0] * lst[2]
        elif lst[1] == '/':
            try:                        #проверка деления на 0
                lst[0] / 0
            except :
                ZeroDivisionError
            return lst[0] / lst[2]
        elif lst[1] == '^':
            try:
                type(lst[2]) is float
            except:
                ValueError
            return lst[0] ** lst[2]
        #в моем калькуляторе отрицательную и дробную степень нельзя
        elif lst[1] == '$':
            try:                            #проверка деления на 0
                lst[0] // 0
            except:
                ZeroDivisionError
            return lst[0] // lst[2]
        elif lst[1] == '%':
            try:                            # проверка деления на 0
                lst[0] // 0
            except:
                ZeroDivisionError
            return lst[0] % lst[2]


def get_count_short_list(lst_1, lst_2):
    '''Составляет короткий лист из трех элементов разных списков [спис_1, спис_2, спис_1] и выполняет арифметич.
    действие в соответствии со средним элементом. Результат кладет в первый список, удаляет из первого и второго списков
    последние элементы.'''
    short_list = [lst_1[-2], lst_2[-1], lst_1[-1]]
    lst_1[-2] = get_count(short_list)
    del lst_1[-1]
    del lst_2[-1]
    return lst_1[0]


def get_result(lst):
    '''Получение окончательного результата с использованием двух стеков.
    В первом цифры, во втором знаки. Принцип см. по ссылке https://www.youtube.com/watch?v=Vk-tGND2bfc'''
    stack_1, stack_2 = [], []
    i = 0
    while i < len(lst):
        if type(lst[i]) != str:
            stack_1.append(lst[i])
            i += 1
        else:
            if lst[i] == '(':
                stack_2.append(lst[i])
                i += 1
            elif lst[i] == ')':
                get_count_short_list(stack_1, stack_2)
                i += 1
                if stack_2[-1] == '(':
                    stack_2.pop()
            elif len(stack_2) == 0:
                stack_2.append(lst[i])
                i += 1
            elif get_prior(lst[i]) > get_prior(stack_2[-1]):
                stack_2.append(lst[i])
                i += 1
            else:
                get_count_short_list(stack_1, stack_2)
    while len(stack_1) > 1:
        get_count_short_list(stack_1, stack_2)
    return stack_1


string_in = input('Что хотим посчитать? ')     #входящая строка
lst = get_list(string_in)
lst = get_number(lst)
print(f'Ответ: {get_result(lst)[0]}')


if __name__ == '__main__':
    my_str = '1+2*(3+4/2-(1+2))*2+1'
    assert 10