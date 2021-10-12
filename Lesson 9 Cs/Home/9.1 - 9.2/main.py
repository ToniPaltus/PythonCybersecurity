import json
import re
import requests

# 9.1
'''
Пользователь отправляет input (), как показано ниже. Это json.
Вы должны создать dict и проанализировать все данные из строки json в dict.
Если поле не задано
используйте значение по умолчанию, для замужнего ложного, для неупорядоченного:
ложный.
Напишите 2 функции, сначала верните строку json, вторая
вернуть dict.
нить
------> json ------> dict | dict ------> json ------>
файл
------> строка ----> json ----> dict | строка ----> файл
** Приятно иметь: попробуйте поместить свои данные в * .txt и добавить функцию для записи
и читать в / из файла по строке.
'''

'''
    test str
    {"name": "john", "age": 10, "married": True, "divorced": false}
    {"name": "Alex", "age": 3, "married": true, "divorced": False}
    {"name": "Sara", "age": 13, "married": true, "divorced": false}
    {"name": "Jozeph", "age": 40, "married": False, "dist": false}
'''
'''
keys_dict = {
    1: "name",
    2: "age",
    3: "married",
    4: "divorced"
}
def json_to_dict(my_json):
    my_dict = json.loads(my_json)
    for key in my_dict.keys():
        if str(my_dict[key]).isalpha():
            my_dict[key] = str(my_dict[key]).title()
    return my_dict
def dict_to_json(my_dict):
    my_json = json.dumps(my_dict, indent=4)
    return my_json
def is_correct_dict(my_dict):
    del_lst = []
    for key in my_dict.keys():
        if key not in keys_dict.values():
            del_lst.append(key)
    for item in del_lst:
        del my_dict[item]

    my_dict['name'] = str(my_dict['name']).title()

    if my_dict['married'] == 'True':
        my_dict['married'] = True
    else:
        my_dict['married'] = False

    for key in my_dict.keys():
        if key == 'age' and my_dict[key] < 18:
            my_dict['married'] = False
            my_dict['divorced'] = '--//--'

    return my_dict
def write(file_name, something):
    with open(file_name, 'a') as file_out:
        file_out.write(str(something))
def read(file_name):
    with open(file_name, 'r') as file_in:
        print()
        for line in file_in:
            print(line, end='')

file_name = 'dict_and_JSON.txt'

my_json = input('Enter new member in new dictionary: ')
my_json = my_json.lower()
my_dict = json_to_dict(my_json)
my_dict = is_correct_dict(my_dict)
print('My dictionary:', my_dict, sep='\n')
write(file_name=file_name, something=my_dict)

my_json = dict_to_json(my_dict)
print('My JSON:', my_json, sep='\n')
write(file_name=file_name, something=my_json)
read(file_name)
'''

# 9.2
'''
URL:
http://www.cbr.ru/scripts/XML_daily.asp?
Получить значения данных валют, запихнуть всё в
dict.
Евро,
США, Венгерских форинтов, Норвежских крон , Турецких лир, Вон
Республики Корея, Белорусский рубль

Просто введите этот код
и запустите его.
Попробуй получить
данные по тегам из
json и поместите его в
дикт!
Исследуй и читай
этот код, гугл
могу помочь тебе/
** Приятно иметь: попробуйте
поместить ваши данные в
* .txt и добавить func
писать и читать
в / из файла по строке.
'''


def write(file_name, something):
    with open(file_name, 'a') as file_out:
        file_out.write(str(something))
def read(file_name):
    with open(file_name, 'r') as file_in:
        print()
        for line in file_in:
            print(line, end='')

URL = 'http://www.cbr.ru/scripts/XML_daily.asp?'
find_list = ['Евро', 'США', 'Венгерских форинтов', 'Норвежских крон', 'Турецких лир', 'Вон Республики Корея', 'Белорусский рубль']
find_list_eng = ['EUR', 'USD', 'HUF', 'NOK', 'TRY', 'KRW', 'BYN']

my_dict = {}
for i in range(len(find_list)):
    country = f"{find_list[i]}</\w*><\w*>(\d*\,?\d*)"

    req = requests.get(URL)
    rate = float(re.search(country, req.text).group(1).replace(",", "."))

    temp = {find_list_eng[i]: rate}
    my_dict.update(temp)
    '''
    if find_list[i] in country:
        temp = {find_list_eng[i]: rate}
        my_dict.update(temp)
    '''

file_name = 'information.txt'
print('dict:', my_dict, sep='\n')
write(file_name=file_name, something=my_dict)
print()

json_object = json.dumps(my_dict, indent=4)
print("json string:", json_object, sep='\n')
write(file_name=file_name, something=json_object)
read(file_name)
