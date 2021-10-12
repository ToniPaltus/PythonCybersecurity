# 13.2
# Парсим с сайта все имейлы.
# Складываем в файл.
# Добавляем функцию чтения из файла по запросу
# пользователя. 1 имейл 2 имейл 3 имейл
# вывод в формате:
# 1 имейл
# 2 имейл
# 3 имейл
# https://www.belta.by/contacts/

import re
import requests
from bs4 import BeautifulSoup

def write(file_name, iter, something):
    with open(file_name, 'a') as file_out:
        file_out.write(str(iter) + ' ' + str(something) + '\n')
def read(file_name):
    with open(file_name, 'r') as file_in:
        print()
        for line in file_in:
            print(line, end='')
def clear(file_name):
    with open(file_name, 'w') as f:
        f.close()

url = 'https://www.belta.by/contacts/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

work_divs = soup.find_all('div', class_='text')
emails = []
file_name = 'information.txt'
for div in work_divs:
    #email = re.findall(r'\b\w+@\w+.\w', div.get_text())# Почти правильно
    email = re.findall(r'[a-zA-Z]+@[a-zA-Z0-9-]+(?:.[a-zA-Z0-9-]+)', div.get_text())
    #print(email)
    for item in email:
        if item not in emails:
            emails.append(item)
for i, email in enumerate(emails, start=1):
    write(file_name, i, email)
if bool(input('Read file? (NO ->SKIP): ')):
    read(file_name)
#clear(file_name)
