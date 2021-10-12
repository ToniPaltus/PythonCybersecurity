import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.belta.by/culture/view/ljubov-k-rodine-v%EF%BF%BEkartinah-eleny-krasnoschekovoj-predstavili-na-vystavke-v%EF%BF%BEminske-452443-2021/').text
soup = BeautifulSoup(url, 'lxml')

file = open('HW_Anton_Pastushenko_113_3.txt', 'w')


'''Дата'''
time = soup.find('div', class_='date_full').text
print(time)
file.write(time + '\n')

'''Рубрика'''
rubric = soup.find('a', class_='rubric').text
print(rubric)
file.write(rubric + '\n')

'''Название'''
name = soup.find('a', class_='block_title').text
print(name)
file.write(name + '\n')

'''Контент'''
item = soup.find_all('div', class_='rubricNews_item')
for content in item:
    cont = content.find('a')
    print(cont.get('title'), '\n')
    file.write(cont.get('title') + '\n')

'''Ссылки на фото'''
photo = soup.find_all('a', class_='rubricNews_item_img news_with_rubric_img')
file.write("\n")
for ph in photo:
    box = ph.find('img')
    print(box.get('src'), '\n')
    file.write(box.get('src') + '\n')

'''Теги'''
tg = []
for tag in soup.find_all(True):
    if tag.name not in tg:
        tg.append(tag.name)
print(tg)
file.write('\n')
for i in tg:
    file.write(i + ', ')



'''Подписки в Яндекс, Телега, Вайбер'''
podpiski = soup.find('div', class_="invite_in_messagers").text
print(podpiski)
file.write('\n' + podpiski)


