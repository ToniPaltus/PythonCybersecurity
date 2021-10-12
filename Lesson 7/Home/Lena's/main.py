# 7.1 Information about...
'''
# Напишите программу, которая по запросу пользователя:
# Определяет вашу версию Python +
# Определяет емкость системы +
# Определяет процессор +
# И все, что тебя интересует
# В ответ программа выдает комментарии,
# например, если у вас Linux - «Вау, вы
# сделать хакера! ' Так далее.
# При вводе слова exit программа запускается.
# прервано.
# Также при желании:
# записать все данные о вашей системе в файл,
# и вывести его из файла по запросу.
'''

from platform import python_version, machine, processor, system, version, architecture, \
    python_implementation, mac_ver, uname, java_ver, release, python_branch

module_dict = {
    1: 'python_version',
    2: 'machine',
    3: 'processor',
    4: 'system',
    5: 'version',
    6: 'architecture',
    7: 'python_implementation',
    8: 'mac_ver',
    9: 'uname',
    10: 'java_ver',
    11: 'release',
    12: 'python_branch'
}

def print_menu(dictionary):
    count = 1
    print('\nAvailable modules:')
    for key in dictionary.keys():
        if count == int(len(dictionary) / 2 + 1):
            print()
        print(key, '->', dictionary[key], end='; ')
        count += 1
def good_number(dictionary):
    while True:
        print_menu(dictionary)
        number = input('\nEnter number of module: ').replace(' ', '')
        if number.isdigit():
            number = int(number)
            if number in dictionary.keys():
                return number
            else:
                print('Uncorrected input. Please try again...')
        else:
            print('Uncorrected input. Please try again...')
def write(File_name, dictionary):
    with open(File_name, 'w') as file_out:
        way = bool(input('Write all information at once? (No -> skip) '))
        if not way:
            finish = False
            iter = 1
            while not finish:
                number = good_number(dictionary)
                file_out.write(str(iter) + ') ' + dictionary[number].title().replace('_', ' ') + ': ' + str(
                    eval(dictionary[number])()) + '\n')
                iter += 1
                finish = bool(input('Finish? (No -> skip) '))
        else:
            for i in range(1, len(module_dict) + 1):
                file_out.write(
                    str(i) + ') ' + dictionary[i].title().replace('_', ' ') + ': ' + str(eval(dictionary[i])()) + '\n')
def read(File_name):
    with open(File_name, 'r') as file_in:
        print()
        for line in file_in:
            print(line, end='')

file_name = 'information.txt'
write(File_name=file_name, dictionary=module_dict)
read(File_name=file_name)
