#3.4 Удалить повторяшки
import random

size = int(input('Enter the size: '))
lst = [random.randint(0, 20) for i in range(size)]
lst.sort()
print('List:', lst)

for item in lst:
    while lst.count(item) >= 2:
        if lst.count(item) >= 2:
            del lst[lst.index(item)]
print('List:', lst)

#3.5 Написать строку чисел, перевести их в инт и найти сумму
'''
numbers = input('Enter your numbers: ')
numbers_list = numbers.split()
print('Numbers_list:', numbers_list)
numbers_list = [int(numbers_list[i]) for i in range(len(numbers_list))]
my_sum = sum(numbers_list)
print('Numbers_list:', numbers_list, '\nSum:', my_sum)
'''
#3.6 Составить список из элементов другого списка, которые повторяются в нем более 1 раза
'''
size = int(input('Enter the size: '))
lst = [random.randint(0, 20) for i in range(size)]
lst.sort()
print('List:', lst)

result = []
for item in lst:
    if lst.count(item) > 1:
        if not item in result:
            result.append(lst[lst.index(item)])
print('Result:', result)
'''
#3.7 Найти среднее арифметическое чисел в листе
'''
size = int(input('Enter the size: '))
lst = [random.randint(0, 20) for i in range(size)]
print('List:', lst)
avarage = sum(lst)/len(lst)
print('Avarage:', avarage)
'''
#3.8 Найти среднее арифметическое чисел в диапазоне от а до b кратных 3
'''
a = int(input('Enter a: '))
b = int(input('Enter b: '))

lst = [i for i in range(a, b + 1) if i % 3 == 0]
print('List:', lst)
avarage = sum(lst)/len(lst)
print('Avarage:', avarage)
'''