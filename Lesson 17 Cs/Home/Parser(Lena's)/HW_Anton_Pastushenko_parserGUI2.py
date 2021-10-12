# + возможность ввода ссылки сайта с которого парсим,
# • выбора тегов для парсинга(title body rubric)
# + ввод названия файла для сохранения текста
# + функция парсинга даты,
# • описания статей
# • названий

#--------------------------------------------
import requests
from bs4 import BeautifulSoup
import pandas
from tkinter import *



def zagr():
    url = requests.get(ent.get()).text
    soup = BeautifulSoup(url, 'lxml')
    print('загружено')
    return soup
def creat(filename):
    # print(filename)
    global f
    f = open(filename.get() + '.txt', 'w')
    print('файл создан')
    return f
def parsDate():
    soup = zagr()
    if f:
        data = soup.find('div', class_='header_date').text
        data = data.replace('\n', '')
        data = data.replace(' ', '', 28)
        f.write('\n'+ data + '\n----------------------------')
        print(data+'\n----------------------------')
        print('записано')
def parsTitle():
    soup = zagr()
    if f:
        data = soup.find_all('div', class_='fp_r_title')
        f.write('\nНазвания заглавий: \n')
        for content in data:
            cont = content.find('a')
            if cont.get('title'):
                print(cont.get('title'))
                f.write(cont.get('title')+'\n')
        print('записано')
def parsBody():
    soup = zagr()

    item = soup.find_all('div', class_='rubricNews_item')
    for content in item:
        cont = content.find('a')
        print(cont.get('title'), '\n')
        f.write(cont.get('title') + '\n****\n')

#---------------------------------------------
root = Tk()

root['width'] = 415
root['height'] = 200

# Загружаем ссылку
lbl = Label(root, text = 'ссылка на сайт:')
# https://www.belta.by/
lbl.place(x = 20, y = 20)
ent = Entry(root, width = 26)
ent.place(x = 140, y = 20)

btn = Button(root, text='загрузить', command = zagr)
btn.place(x = 320, y = 16)

# Парсинг
btitle = Button(root, text='parsing title', command = parsTitle )
btitle.place(x = 20, y = 50)

btitle = Button(root, text='parsing body', command = parsBody)
btitle.place(x = 120, y = 50)

btitle = Button(root, text='parsing rubric')
btitle.place(x = 220, y = 50)

btitle = Button(root, text='parsing date', command = parsDate)
btitle.place(x = 320, y = 50)


lbl = Label(root, text = 'имя файла:')
lbl.place(x = 20, y = 90)
filename = Entry(root, width = 26)
filename.place(x = 140, y = 90)

btn = Button(root, text='создать', command = lambda : creat(filename))
btn.place(x = 320, y = 86)

def btn_command():
    lbl['text'] = '= '
    btitle['command'] = btn_command

root.mainloop()


#*********************
'''


rubric = soup.find('a', class_='rubric').text
print(rubric)
f.write(rubric+'\n')


''''''
name = soup.find('a', class_='block_title').text
print(name)
f.write(name+'\n\n')

''''''
time = soup.find('div', class_='date_full').text
print(time)
f.write(time+'\n\n\n')

''''''
item = soup.find_all('div', class_='rubricNews_item')
for content in item:
    cont = content.find('a')
    print(cont.get('title'), '\n')
    f.write(cont.get('title')+'\n****\n')

''''''
tg = []
for tag in soup.find_all(True):
    if tag.name not in tg:
        tg.append(tag.name)
print(tg)
f.write("\nTags:\n")
for i in tg:
    f.write(i+'\n')

''''''
photo = soup.find_all('a', class_='rubricNews_item_img news_with_rubric_img')
f.write("\nPhoto links:\n")
for ph in photo:
    box = ph.find('img')
    print(box.get('src'), '\n')
    f.write(box.get('src')+'\n')



''''''
podpiski = soup.find('div', class_="invite_in_messagers").text
print(podpiski)
f.write('\n'+podpiski)
'''
