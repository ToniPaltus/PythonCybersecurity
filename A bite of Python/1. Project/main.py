import sys
print('Аргументы коммандной строки: ')
for i in sys.argv:
    print(i)
print('Переменная PYTHONPATH содержит', sys.path, '\n')