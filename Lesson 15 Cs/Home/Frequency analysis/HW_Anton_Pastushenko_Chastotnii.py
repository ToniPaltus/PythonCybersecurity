# Частотный анализ
# Взять любую статью(англ) текста парсите/ txt
# 100% это все символы(посчитать сколько символов)
# посчитать процент каждого символа в тексте
# построить графики в matplotlib столбчатая
import random
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = 'https://en.wikipedia.org/wiki/Lepidoptera'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

p_tegs = soup.find_all()
text = ''
for p in p_tegs:
    text += p.get_text()
text = text.replace('\n', ' ').upper()
#print('Text:', text)
length = len(text)
#print('Length:', length)

alef = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
alef.update({' ': 0})
#print('Alef:', alef)

# Посчитали символы
for i in range(length):
    if text[i] in alef.keys():
        alef[text[i]] += 1
#print('Alef:', alef)

# Посчитали буквы
simbols = 0
for value in alef.values():
    simbols += value
#print('simbols:', simbols)

# Посчитали знаки
other_simbols = length - simbols
#print('Other simbols:', other_simbols)

# Процент букв
for key in alef.keys():
    alef[key] = round(alef[key] / length * 100, 2)
alef.update({'O/s': round(other_simbols / length * 100, 2)})
print('Alef:', alef)

# Проверка
result_sum = 0
for value in alef.values():
    result_sum += value
print('result_sum:', result_sum)

#Гистограмма
all_colors = list(plt.cm.colors.cnames.keys())
color = random.choices(all_colors, k=27)

x = alef.keys()
y = alef.values()

fig, ax = plt.subplots()

ax.bar(x, y, color=color)

plt.xlabel('Буквы')
plt.ylabel('Проценты')
plt.title('Частотный анализ')
plt.xlim(-0.5, 27.5)
plt.ylim(0, 15)
plt.grid(True)
plt.show()