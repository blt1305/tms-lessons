# Запишите в файл file_01.txt строку "Hello world"
with open('file_01.txt', 'w') as f:
    f.write('Hello world\n')

# Прочитайте все строки файла file_02.txt, выведите их в консоль.
with open('file_02.txt', 'w') as f:     #создаем файл
    f.write('Hello world\n')
    f.write('Hello world\n')
    f.write('Hello world\n')

with open('file_02.txt', 'r') as f:     #читаем файл
    for line in f:
        print(line)

def my_func():
    print('Python')
