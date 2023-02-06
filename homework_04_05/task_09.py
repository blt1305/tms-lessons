#Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы),
#и возвращает самое длинное слово из этого текста. Для разбиения строки на слова используйте функцию split.
#"hello this is a string with words and spaces and big big woooooooooord" -> "woooooooooord"

def get_longest_word(my_string: str) -> str:
    list_words = my_string.split()      #преобразуем строку в список слов
    len_word = len(list_words[0])       #максимальная длина пока - длина первого слова
    for i in range(1, len(list_words)): #счетчик слов от первого до последнего
        if len(list_words[i]) > len_word:       #если длина очередного слова больше, чем длина найденного до этого максимального
            resalt = list_words[i]              #в результат отправим слово
            len_word = len(list_words[i])       #изменим переменную с макс. длиной слова

    return resalt


my_str = "hello this is a string with words and spaces and big big woooooooooord"
print(get_longest_word(my_str))