#3.1

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))

max = a
if max < b:
    max = b
if max < c:
    max = c
if max < d:
    max = d
print("Max =", max, type(max))

#3.2
a, b, c, a1, b1, c1, a2, b2, c2, a3 = map(int, input("ENTER VALUE").split())
print(a, b, c, a1, b1, c1, a2, b2, c2, a3)
print('Max =', max(a, b, c, a1, b1, c1, a2, b2, c2, a3))
print('Min =', min(a, b, c, a1, b1, c1, a2, b2, c2, a3))

#3.3
str = input('enter: ')
if str == 'Spathiphyllum':
    print("Yes Spathiphyllum is the best plant ever!")
elif str == 'spathiphyllum':
    print("No, I want a big Spathiphyllum!")
else :
    print("Spathiphyllum! Not %str!"%(str))

#3.4
for i in range(0, 3):
    income = float(input('Enter your income: '))
    tax = round(0.15 * income, 5)
    print("Income: %s. Tax: %s"%(income, tax))

#3.5
year = int(input("Enter a year: "))
if year %400 == 0:
    print("common year")
elif year % 100 == 0:
    print("Not common year")
elif year % 4 == 0:
    print("common year")
else:
    print('it is a leep year')

#3.6
a = 0
b = -7586
count = 0
while(a != b):
    a = int(input("Enter a number: "))
    if a > b:
        print("your number is too large")
    else:
        print('your number is too small')
    count += 1
print("Well done! You are free now\nYour IQ is -"+str(count))

#3.7
import time

for i in range(1, 6):
    print(i, 'Mississippi')
    time.sleep(1)
print("Common!")

#3.8
while(True):
    str = input('Enter: ')
    if str == 'xadjikuliev':
        break
print('Out')

#3.9
str = input("Enter: ")
str = str.upper()
for i in range(len(str)):
    if str[i] == 'A' or str[i] == 'E' or str[i] == 'I' or str[i] == 'O' or str[i] == 'U' or str[i] == 'Y':
        continue
    print(str[i])

#3.10
str = input("Enter: ")
str = str.upper()
result = ''
for i in range(len(str)):
    if str[i] == 'A' or str[i] == 'E' or str[i] == 'I' or str[i] == 'O' or str[i] == 'U' or str[i] == 'Y':
        continue
    result = result + str[i]
    print("result:", result)
#print("result:", result)

#3.11
value = int(input('Enter: '))
iter = 1
while(value != 1):
    if(value % 2 == 0):
        value/=2
        print("Value:", value)
    else:
        value= value*3 + 1
        print("Value:", value)
    iter += 1
print(iter)

#3.12
x = int(input("Enter number: "))
znak = input("Enter sign: ")
y = int(input("Enter number: "))
if znak == '+':
    rez = x + y
elif znak == '-':
    rez = x - y
elif znak == '/':
    rez = round(x / y, 3)
elif znak == '*':
    rez = x * y
elif znak == '**':
    rez = x ** y
elif znak == '//':
    rez = x // y
elif znak == '%':
    rez = round(x % y, 3)

print(x, znak, y, '=', rez)

flg = True
while flg:
    rez1 = rez
    znak = input("Enter sign: ")
    y = int(input("Enter number: "))
    if znak == '+':
        rez += y
    elif znak == '-':
        rez -= y
    elif znak == '/':
        rez = round(rez / y, 3)
    elif znak == '*':
        rez *= y
    elif znak == '**':
        rez = rez ** y
    elif znak == '//':
        rez = rez // y
    elif znak == '%':
        rez = round(rez % y, 3)
    print(rez1, znak, y, '=', rez)
    flg = int(input("Enter 1 to continue\nEnter  0 to end "))

# Установка бита
value = int('00000100', 2)
print('Значение:', int(value), bin(value))

setBit = int('00000001', 2)
bit = int(input("Enter setbit: "))
setBit = setBit << bit

value = value | setBit
print(int(value), bin(value))

# Сброс бита
resetBit = int('00000001', 2)
bit = int(input("Enter resetbit: "))
resetBit = resetBit << bit

value = ~value
value = value | resetBit
value = ~value
print(int(value), bin(value))

# Инвертация бита
invBit = int('00000001', 2)
bit = int(input("Enter invbit: "))
invBit = invBit << bit

value = value ^ invBit
print(int(value), bin(value))

x = 5
print(~x)
