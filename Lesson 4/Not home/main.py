# Максимальный элемент в массиве

size = int(input('Enter the size: '))
arr = []
for i in range(size):
    value = int(input('Enter the member: '))
    arr.append(value)
print('arr:', arr)

max = arr[0]
for i in range(size):
    if max < arr[i]:
        max = arr[i]
print('Max =', max)

arr = arr[::-1]
print('arr:', arr)


# Количество элемента в списке (while)
import random

arr = []
member = ''

while member != '0':
    member = input('Enter the member or press \'0\' to finish: ')
    arr.append(member)
arr.pop()# удаляем стоп символ
print('Arr:', arr)

word = input('Enter word: ')
word_count = 0
for i in range(len(arr)):
    if(arr[i] == word):
        word_count += 1

if word_count == 0:
    print('\nNot found!')
else:
    print('\nWord:', word, '\nCount:', word_count)


# Вывести элементы списка меньше заданного
'''
size = int(input('Enter the size: '))
arr = [''] * size

for i in range(size):
    arr[i] = int(random.randint(0, 100))
print('Arr:', arr)

value = int(input('Enter value: '))
for i in range(len(arr)):
    if arr[i] < value:
        print(arr[i], end=' ')
'''

# Список из общих для 2 списков
'''
size1 = int(input('Enter size1: '))
size2 = int(input('Enter size2: '))

arr1 = [''] * size1
arr2 = [''] * size2

for i in range(size1):
    arr1[i] = random.randint(0, 10)
print('Arr1:\n', arr1)

for i in range(size2):
    arr2[i] = random.randint(0, 10)
print('Arr2:\n', arr2)

rez = []
for i in range(size1):
    for j in range(size2):
        if arr1[i] == arr2[j]:
            rez.append(arr1[i])
print('\nRez:\n', rez)

rez = set(rez)
print('\nRezzz:\n', rez)
'''
# Квадраты n первых целых чисел
'''
n = int(input('Enter n: '))
squares = [i*i for i in range(n)]
print('Squares: ', squares)
'''