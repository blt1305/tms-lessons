# Запишите свои данные в файл file_06.csv в формате CSV.
import csv
header = ('name', 'surname', 'gender')
i_am = [('Elena', 'Sec', 'F')]

with open('file_06.csv', 'w') as file:
    writer = csv.writer(file, delimiter = '*')
    writer.writerow(header)
    writer.writerow(i_am)

# Пример:
# name,surname,gender
# Dmitry,Buevich,M
# Пользователь вводит свои данные (имя, фамилия, возраст). Запишите эти данные в файл file_07.csv формате CSV.
# Прочитайте файл из прошлого задания и выведите данные в формате "{Фамилия} {Имя} {Возраст}".
