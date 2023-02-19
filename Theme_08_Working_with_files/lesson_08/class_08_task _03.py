#JSON
# 3. Создайте словарь с вашими данными (имя, фамилия, и т.д), запишите его в файл file_03.json в формате JSON.
import json
my_dict_03 = {'name' : 'Elena', 'surname' : 'Sec', 'age' : 40}
with open ('file_03.json', 'w') as file:
    json.dump(my_dict_03, file)

# 4. Пользователь вводит свои данные (имя, фамилия, возраст). Запишите эти данные в файл file_04.json формате JSON.
name = input()
surname = input()
age = input()
with open ('file_04.json', 'w') as file:
    my_dict_04 = {'name': name, 'surname': surname, 'age': age}
    json.dump(my_dict_04, file)


# 5. Прочитайте файл из прошлого задания и выведите данные в формате "{Фамилия} {Имя} {Возраст}".
with open('file_04.json', 'r') as file:
    data = json.load(file)
    print(data)

