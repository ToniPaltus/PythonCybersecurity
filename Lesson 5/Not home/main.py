import random
#1
'''
size = int(input('Enter size: '))
lst = [random.randint(0, 20) for i in range(size)]
print(lst[0], lst[-1])'''

#2 Вывести числа по порядку (2 - два раза, 3 - три раза..) до n
'''
n = int(input('Enter n: '))
count = 0
lst = []
for i in range(n):
    j = i
    while j and count != n:
        lst.append(i)
        j -= 1
        count += 1
print(lst)'''

# 3 Выводим индексы вхождений x
'''
size = int(input('Enter size: '))
lst = [random.randint(0, 20) for i in range(size)]
print('List:', lst)
x = int(input('Enter x: '))
indexes = []
for i in range(len(lst)):
    if lst[i] == x:
        indexes.append(i)
if not x in lst:
    print('Empty')
else:
    print('Indexes:', indexes)'''
# 4 Является ли число квадратом
'''
x = int(input('Enter x: '))
if x % x**0.5 == 0:
    print('Is a square of:', x**0.5)
else:
    print('Not a square')'''
# 5 Самовлюбленное число
'''
value = int(input('Enter value: '))
copy_value = value
razrady = []
while value:
    ost = value % 10
    value = int(value / 10)
    razrady.append(ost)
razrady.reverse()
print(razrady)
degree = len(razrady)
sum = 0
for item in razrady:
    sum += item**degree
if sum == copy_value:
    print(True)
else:
    print(False)
'''
'''
x = input('Введите число: ')
res = 0
for i in x:
    res += int(i) ** len(x)
print(True if res == int(x) else False)
'''
# 6 CamelCase
str = input('Enter str: ')
words = str.split()
result = ''
for item in words:
    app = item[0].upper()
    word = app + item[1:]
    result += word
print(result)


words = input('Enter str: ').split()
result = ''
for item in words:
    app = item[0].upper()
    word = app + item[1:]
    result += word
print(result)



x = input("Введите: ")
x = x.title()
print(x.replace(' ', ''))





