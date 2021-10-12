# 13.3
# Парсим с сайта описания и даты (дату вытаскиваем из
# описания).
# 12.10.2010 ----> 12/10/2010
# в формате "Дата **/**/**** ++++ описание"

import re
import requests
from bs4 import BeautifulSoup

def write(file_name, month, year):
    with open(file_name, 'a') as file_out:
        file_out.write(str(month) + ' ' + str(year) + '\n')
def read(file_name):
    with open(file_name, 'r') as file_in:
        print()
        for line in file_in:
            print(line, end='')
def clear(file_name):
    with open(file_name, 'w') as f:
        f.close()

dict = {
    1: 'январь',
    2: 'февраль',
    3: 'март',
    4: 'апрель',
    5: 'май',
    6: 'июнь',
    7: 'июль',
    8: 'август',
    9: 'сентябрь',
    10: 'октябрь',
    11: 'ноябрь',
    12: 'декабрь'
}

url = 'https://journal-free.ru/avtomobili/za-rulem-11-noiabr-2019-rossiia.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
str = soup.text
file_name = 'dates.txt'

dates = re.findall(r'([а-я]+)\s(\d{4})', str)
#print('Dates', dates, type(dates))
for date in dates:
    for key in dict:
        if date[0] == dict[key]:
            print(date, '--->', key, date[1])