"""
К 22:00 воскресненье
Название: Cканер устройств в сети
Доработать программы для GUI.
Используем TKINTER
Button, Label
Frame
Менеджеры
и всё чо вам нужно. Делаем красиво!!!
"""

# Погуглить
# позволяют получать инфо об ОС и платформе, процыке и тд
import os
import platform

# для многопоточности
import threading
import socket

from datetime import datetime

def getMyIp():
    # Создаем сокет (UDP)
    # socket.AF_INET  - сокет для IPv4
    # SOCK_DGRAM - UDP сокет
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Настраиваем сокет на BROADCAST вещание.
    # SOCK_DGRAM - широковещательная рассылочка
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    s.connect(('<broadcast>', 0))
    # s.getsockname() - вернет ваш IP адрес
    return s.getsockname()[0]
def scan_Ip(ip):  # comm ---> 0-254
    # addr = "192.168.100." + 0-254
    addr = net + str(ip)
    # comm = "ping -n 1 "+"192.168.100.X" |+ X=0-254
    comm = ping_com + addr
    response = os.popen(comm)  # запусть ping в Операционке
    data = response.readlines()  # ответ ping'а сохрани
    # print()
    # записывать в файл и потом изучить чтобы понять логику этихх вещей
    for line in data:
        if 'TTL' in line:
            print(addr, "--> Ping Ok")
            break

net = getMyIp()  # 192.168.100.10
print('You IP :', net)

# net mask [255 255 255 0] 0 255 для мобилок ПК телика и тд
# ip addse [192 168 100 10]
net_split = net.split('.')  # ["192"  168 100 10]
a = '.'
net = net_split[0] + a + net_split[1] + a + net_split[2] + a  # string  "192.168.100."

start_point = int(input("Enter the Starting Number: "))  # 0
end_point = int(input("Enter the Last Number: "))  # 254

oc = platform.system()
if (oc == "Windows"):  # Linux MAC OS
    ping_com = "ping -n 1 "
else:
    ping_com = "ping -c 1 "
#############################################
t1 = datetime.now()  # засечь время
print("\nScanning in Progress:")

for ip in range(start_point, end_point):
    if ip == int(net_split[3]):
        continue
    potoc = threading.Thread(target=scan_Ip, args=[ip])
    potoc.start()

potoc.join()
t2 = datetime.now()
total = t2 - t1  # фактическое время

print("Scanning completed in: ", total)
