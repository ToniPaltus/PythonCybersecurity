'''
0
Объеденить все программы в одну +
1
Обязательно настроить сохранение в файл+
2
--**создать функции для запросов на получение информации с сайта (1-10 примеры)
превратить в функции, сделать вывод меню для пользователя с перичнем возможных +
операций (запросов), по слову "qq" выйти из программы.
3
Так же дописать функцию, которая будет искать слова (либо теги) по запросу
введенному пользователем
+вывод всех результатов постараться их причесать (минимум лишнего)!!!!+
4
--**** Сделать так, чтобы это работало с любым сайтом (принимаем ввод +
5
--***** packages+
'''

import requests
import re
import pandas as panda
from bs4 import BeautifulSoup
func_dict = {
    1: 'get_html_code',
    2: 'get_html_table_code',
    3: 'get_all_links_from_table',
    4: 'get_countries_from_links_from_table',
    5: 'get_data_frame',
    6: 'get_something_by_choice',
    7: 'get_unique_tegs',
    8: 'get_something_by_choice2',
    9: 'get_date',
    10: 'get_date2',
    11: 'get_tag',
    12: 'get_word'
}

def write(file_name, something):
    with open(file_name, 'w') as file_out:
        file_out.writelines(str(something))
def read(file_name):
    with open(file_name, 'r') as file_in:
        print()
        for line in file_in:
            print(line, end='')

def get_html_code(url):
    soup = BeautifulSoup(url, 'lxml')
    return soup.prettify("utf-8")
def get_html_table_code(url):
    soup = BeautifulSoup(url, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    #table = soup.find('table', {'class': 'wikitable sortable'}).prettify("utf-8") но ссылки не записываются в файл
    return table
def get_all_links_from_table(url):
    table = get_html_table_code(url)
    if table != None:
        return table.findAll('a')
def get_countries_from_links_from_table(url):
    links = get_all_links_from_table(url)
    if links != None:
        countries = []
        for link in links:
            countries.append(link.get('title'))
        return countries
def get_data_frame(url):
    countries = get_countries_from_links_from_table(url)
    data_frame = panda.DataFrame()
    data_frame['Country:'] = countries
    return data_frame
def get_something_by_choice(url):
    soup = BeautifulSoup(url, 'lxml')
    head = soup.head
    title = soup.head.title
    titlel = soup.head.title.get_text()
    body = soup.body

    while True:
        choice = input('1 - Head HTML code\n2 - Title HTML code\n3 - Title HTML text\n4 - Body HTML code\nInput: ')
        choice = choice.replace(' ', '')
        if choice.isdigit() and len(choice) == 1:
            choice = int(choice)
            if choice == 1:
                return head
            elif choice == 2:
                return title
            elif choice == 3:
                return titlel
            elif choice == 4:
                return body
            else:
                print('Uncorrect input. Try again...')
        else:
            print('Uncorrect input. Try again...')
def get_unique_tegs(url):
    soup = BeautifulSoup(url, 'lxml')
    tegs = []
    for tag in soup.find_all(True):
        if tag.name not in tegs:
            tegs.append(tag.name)
    return tegs
def get_something_by_choice2(url):
    soup = BeautifulSoup(url, 'lxml')
    tr = soup.find_all('tr')
    itr = soup.find_all('i')
    itrr = soup.i.get_text()
    css_soup = soup.select('i')

    while True:
        choice = input('1 - all tr\n2 - all i\n3 - all i text\n4 - css select i\nInput: ')
        choice = choice.replace(' ', '')
        if choice.isdigit() and len(choice) == 1:
            choice = int(choice)
            if choice == 1:
                return tr
            elif choice == 2:
                return itr
            elif choice == 3:
                return itrr
            elif choice == 4:
                return css_soup
            else:
                print('Uncorrect input. Try again...')
        else:
            print('Uncorrect input. Try again...')
def get_date(url):
    soup = BeautifulSoup(url, 'lxml')
    resDate = []
    dates = soup.find_all('span', class_='date')
    # print(dates)

    lines = [date.get_text() for date in dates]
    for line in lines:
        m = re.search(r'(\d{4})', line)
        if m:
            resDate.append(m.group(1))
    return resDate
def get_date2(url):
    try:
        soup = BeautifulSoup(url, 'lxml')
        # get_value
        date = soup.find('span', class_='date').text
        #print(date)
        #print(type(date))

        resDate = []
        dates = soup.find_all('span', class_='date')
        #print(dates)
        #print(type(dates))

        lines = [date.get_text() for date in dates]

        # get date
        for line in lines:
            m = re.search(r'(\d{4})', line)
            if m:
                resDate.append((m.group(1)))
        return resDate
    except:
        print('Yoops. Something went wrong...')
def good_input_int(min, max):
    while True:
        value = input('>>> Enter number of function: ')
        value = value.replace(' ', '')
        if value.isdigit():
            value = int(value)
            if value >= min and value <= max:
                return value
            else:
                print('Uncorrect input. Try again...')
        else:
            print('Uncorrect input. Try again...')
def get_tag(url):
    soup = BeautifulSoup(url, 'lxml')
    my_tag = input('Enter tag: ')
    for tag in soup.find_all(True):
        if tag.name == my_tag:
            return tag
    return 'Not found'
def get_word(url):
    soup = BeautifulSoup(url, 'lxml')
    text = soup.get_text('\n', strip=True)
    #print(text)
    my_word = input('Enter word: ')
    words = text.split()
    if my_word in words:
        return my_word
    return 'Not found'
def get_menu(url):
    flg = True
    while flg:
        for key in func_dict.keys():
            print(key, '->', func_dict[key], sep='')
        choice = good_input_int(1, len(func_dict))
        data = eval(func_dict[choice])(url)
        print('Your fuction: ' + func_dict[choice], data, sep='\n')
        write_flg = bool(input('Write in file? (NO -> SKIP): '))
        if write_flg:
            try:
                file_name = func_dict[choice] + '.txt'
                write(file_name=file_name, something=data)
                read(file_name)
            except:
                print('Error')
        flg = bool(input('\n>>> Finish? (YES -> SKIP ): '))

# Url for tests:
# https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area
# https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0
# https://metanit.com/

web_address = input('Enter web address: ')
url = requests.get(web_address).text
get_menu(url)