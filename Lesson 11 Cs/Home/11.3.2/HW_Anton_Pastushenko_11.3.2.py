# https://www.belta.by/sport/
# Задача заключается в том что необходимо спарсить даты и
# названия новостей!+
# сохранить данные в списки
# bs4 list[]list[]. И попробовать
# соеденить в словарь по типу: дата название
# Либо как вам удобно
# для этого понадобится всё выше изученное.
# а так же изучить код страницы.
# **Записать данные в файлы+
# **Читать из файла+
import requests
from bs4 import BeautifulSoup

def write(file_name, something):
    with open(file_name, 'a') as file_out:
        file_out.writelines(str(something))
def read(file_name):
    with open(file_name, 'r') as file_in:
        print()
        for line in file_in:
            print(line, end='')

url = 'https://www.belta.by/sport/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
divs = ['rc_item', 'tl_item', 'news_item_main', 'news_item', 'rc_item', 'tn_item']
news = []

file_name = 'news.txt'
for item in divs:
    work_div = soup.find_all('div', class_=item)
    for work in work_div:
        link = work.find('a')
        news.append(link.get('title'))
        #print(link.get('title'))
        write(file_name, link.get('title') + '\n')
print(news)
read(file_name)

date = soup.find('div', class_='header_date')
time = date.get_text()
print(time)