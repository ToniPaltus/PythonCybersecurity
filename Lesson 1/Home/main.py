# Задача №1
# Формула Герона

a = input("Введите сторону а: ")# input всегда выдает str
print("a =", a)
b = input("Введите сторону b: ")
print("b =", b)

c = input("Введите сторону c: ")
print("c =", c)

a = int(a)
b = int(b)
c = int(c)

p = (a+b+c)/2

print("p =", p)

from math import sqrt
S = sqrt(p*(p-a)*(p-b)*(p-c))
print("S =", S)


# Задача №2
# Логические операторы
value = input("Введите число: ")
print("d =", value)

value = int(value)
flag = False

if value > -15 and value <= 12 or value > 14 and value < 17 or value >= 19:
    flag = True
print("flag =", flag)

