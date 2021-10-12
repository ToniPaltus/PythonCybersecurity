# Шифрование картинки по Цезарю

from PIL import Image

for key in range(0, 255, 25):
    im = Image.open(r'Картинка по цезарю\tiger.png')
    img = im.load()

    w, h = im.size
    for x in range(0, w):
        for y in range(0, h):
            (r, g, b) = img[x, y]
            r, g, b = (r + key) % 255, (g + key) % 255, (b + key) % 255
            img[x, y] = (r, g, b)
    im.save(r'Зашифрованные картинки по цезарю\tiger' + str(key) + '.png')

# Шифрование картинки по Вижинеру
from PIL import Image
from random import randint

im = Image.open(r'Картинка по винижеру\tiger.png')
img = im.load()

w, h = im.size

keys = [[randint(0, 255) for i in range(10)],
        [randint(0, 255) for i in range(100)],
        [randint(0, 255) for i in range(1000)],
        [randint(0, 255) for i in range(h * w)]]

for ik in range(0, len(keys)):
    im = Image.open(r'Картинка по винижеру\tiger.png')
    img = im.load()

    w, h = im.size
    key = keys[ik]
    k = key * (w * h // len(key) + 1) * 3
    i = 0
    for x in range(0, w):
        for y in range(0, h):
            (a, b, c) = img[x, y]
            a, b, c = (a + k[i]) % 255, (b + k[i+1]) % 255, (c + k[i+2]) % 255
            img[x, y] = (a, b, c)
            i += 3
        im.save(r'Зашифрованные картинки по вижинеру\V_tiger-' + str(ik) + '.png')


'''
#### Шифруем картинку по Вижинеру

from PIL import Image
from random import randint

im = Image.open(r'D:\IBA CyberSec\Lecture 7 Python Crypto\Картинку по винижеру\tiger.png')
img = im.load()

w, h = im.size

keys = [[randint(0,255) for i in range(10)], 
        [randint(0,255) for i in range(100)], 
        [randint(0,255) for i in range(1000)], 
        [randint(0,255) for i in range(w*h)]]
'''
'''
for ik in range(0, len(keys)):
    im = Image.open(r'D:\IBA CyberSec\Lecture 7 Python Crypto\Картинку по винижеру\tiger.png')
    img = im.load()

    w, h = im.size
    key = keys[ik]
    k = key*(w*h // len(key) + 1)*3
    i = 0
    for x in range(0,w):
         for y in range(0,h):
            (a,b,c) = img[x,y]
            a, b, c = (a + k[i]) % 255, (b + k[i+1]) % 255, (c + k[i+2]) % 255 
            img[x,y] = (a,b,c)
            i += 3
         im.save(r'D:\IBA CyberSec\Lecture 7 Python Crypto\Картинку по винижеру\V_tiger-'+str(ik)+'.png')

'''