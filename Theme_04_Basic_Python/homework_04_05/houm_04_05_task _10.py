#Напишите функцию get_most_frequent_word, которая на вход принимает текст (только английские слова и пробелы),
#и возвращает самое часто встречающееся слово. Если таких слов несколько - верните любое.
#"hello this is a string with words and spaces and big big woooooooooord and and and" -> "and"

def get_most_frequent_word(my_string: str) -> str:
    list_words = my_string.split()          # преобразуем строку в список слов, словарь будет нужен, не меняем его
    set_words = set(list_words)             # только уникальные
    my_dict = {i: 0 for i in set_words}     # создаем словарь, где ключ - уникальные слова, зничение - пока нули
    for i in range(len(list_words)):        # идем по списку, где каждое слово является ключом словаря
        my_dict[list_words[i]] += 1         # каждый раз по ключу добавляем +1 в значение
    list_words_2 = [[values, key] for key, values in my_dict.items()] #вложенные списки [частота, слово]
    list_words_3 = sorted(list_words_2, key=lambda x: x[0], reverse=True)  # сортировка по убыванию
    return list_words_3[0][1]


my_string = "hello this is a string with words and spaces and big big woooooooooord and and and"
print(get_most_frequent_word(my_string))