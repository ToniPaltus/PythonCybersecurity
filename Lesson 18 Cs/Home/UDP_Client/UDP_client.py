"""
20.08.2021 18:00

Название: UDP чат - CLIENT
Доработать программы для GUI.
Используем TKINTER
Button, Label
Frame
Менеджеры
и всё чо вам нужно. Делаем красиво!!!
"""

import socket
import threading

# читаем сообщения которе data пересылает от других сервер
def read_soct():
    while 1:
        data = sor.recv(1024)
        print(data)

#  адрес сервера
server = '192.168.0.192', 8080  # Данные сервера

sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#name = input("Псевдоним:")  # Вводим наш псевдоним

# адрес конкретного компа на котором вы это запускаете
sor.bind(('192.168.0.192', 81))  # Задаем сокет как клиент
#sor.sendto((name + ' Connect to server').encode('utf-8'), server)
# Уведомляем сервер о подключении

potok = threading.Thread(target=read_soct)
potok.start()
client = []

# Наши сообщения
while True:
    name = input("Псевдоним:")  # Вводим наш псевдоним
    if name not in client:
        client.append(name)
        sor.sendto((name + ' Connect to server').encode('utf-8'), server)
    message = input('Enter massage: ')
    sor.sendto(('[' + name + '] sayd: ' + message).encode('utf-8'), server)
