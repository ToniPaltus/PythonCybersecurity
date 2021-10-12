# 13.1
# Парсим с сайта все названия ссылок и сами ссылки на скачивание pdf документов.+
# Складываем в файл в формате Название(title) - *****; Ссылка http://*****+
# Дописываем функцию для чтения из файла разбиваем на строки по ; Выводим на экран.+

import requests
from bs4 import BeautifulSoup

def write(file_name, title, link):
    with open(file_name, 'a') as file_out:
        file_out.write('Title - ' + str(title) + '; ' + 'Link: ' + str(link) + '\n')
def read(file_name):
    print('Read')
    with open(file_name, 'r') as file_in:
        for line in file_in:
            lst = line.split(';')
            lst[1] = lst[1][:-1]
            print(lst)
def clear(file_name):
    with open(file_name, 'w') as f:
        f.close()

urls = ['https://journal-free.ru/avtomobili/za-rulem-12-dekabr-2019-rossiia.html',\
        'https://journal-free.ru/avtomobili/za-rulem-11-noiabr-2019-rossiia.html',\
        'https://journal-free.ru/avtomobili/za-rulem-6-iiun-2019-rossiia.html',\
        'https://journal-free.ru/avtomobili/za_rulem_4_aprel_2019_rossiya.html',\
        'https://journal-free.ru/avtomobili/za-rulem-5-mai-2019-rossiia.html']
file_name ='information.txt'
for ur in urls:
    url = ur
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    work_div = soup.find_all('div', class_='col-xs-12 col-md-7')
    #print(work_div)
    for div in work_div:
        tegs_a = div.find_all('a')
        teg_a = tegs_a[1]
        #print(teg_a)
        link = teg_a.get('href')
        title = teg_a.get_text()
        write(file_name, title, link)
        #print(link)
        #print(title)
read(file_name)
#clear(file_name)
