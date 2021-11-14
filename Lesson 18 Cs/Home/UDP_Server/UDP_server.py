"""
К 18:30 20.08.2021
Название: UDP чат - SERVER
Доработать программы для GUI.
Используем TKINTER
Button, Label
Frame
Менеджеры
и всё чо вам нужно. Делаем красиво!!!
"""
import socket

# IPv4         UDP датаграммы
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#            Ваш IP адрес     ПОРТ
sock.bind(('192.168.0.192', 8080))
# В чате может быть много людей, и их никнеймы нужно хранить
client = []# Список где храним адреса клиентов/ники людей
print('Start Server')

#консолька - while True | while 3221231:
while 1:
    data, addres = sock.recvfrom(1024)
    print('Data:', data, '\tAddress:', addres[0], addres[1])
    if addres not in client:
        client.append(addres)# Если такого клиента нету , то добавить

    for clients in client:
        if clients == addres:
            continue# Не отправлять данные клиенту, который их прислал
        sock.sendto(data, clients)
