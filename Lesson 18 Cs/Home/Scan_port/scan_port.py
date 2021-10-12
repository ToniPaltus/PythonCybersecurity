"""
К 22:00 воскресненье
Название: Сканер портов моего маршрутизатора
Доработать программы для GUI.
Используем TKINTER
Button, Label, Enter - туда пишем IP|из прошлого примера функция MyIP
192.168.1.10-->192.168.1. + 1 --> 192.168.1.1 ШЛЮЗ
Frame
Менеджеры
и всё чо вам нужно. Делаем красиво!!!
"""

import socket
from datetime import datetime

def scan_port(ip, port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(0.5)

  try:
     connect = sock.connect((ip,port)) #0 -- 999
     print('Port :',port,' its open.')
     sock.close()
  except:
    #заглушка/пустое/ничего не делать/
     pass

#Адрес нашего маршрутизатор --> cmd -- ipconfig -->шлюз по умолчанию
ip = '192.168.0.101'
start = datetime.now()
#0 -- 1000
for i in range(500):
    scan_port(ip, i) #0--999 включит

ends = datetime.now()
print("Time: start - ", start, "  end - ", ends)
print('Time : {}'.format(ends-start))

#Справитесь сами
#Дома доработаете чтобы работало быстрее!
#import threading

#for i in range(1000):
    #potoc = threading.Thread(target=scan_port, args=(ip,i))
   # potoc.start()
