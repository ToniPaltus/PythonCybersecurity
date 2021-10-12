# https://www.belta.by/sport/
#Задача заключается в том что необходимо спарсить ссылки и названия новостей!

import requests
from bs4 import BeautifulSoup

divs = ['rc_item', 'tl_item', 'news_item_main', 'news_item', 'rc_item', 'tn_item']

url = 'https://www.belta.by/sport/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

links = []
news = []
for item in divs:
    work_div = soup.find_all('div', class_=item)
    #print(work_div)

    for work in work_div:
        #print('Work', work)
        link = work.find('a')
        links.append(link.get('href'))
        news.append(link.get('title'))
#print(links)
#print(news)
result = {}
for i in range(len(news)):
    temp = {news[i]: links[i]}
    result.update(temp)
    print(i + 1, temp)
#print('News:\n', result)