#3.1
import random
size = int(input('Enter the size: '))
lst =[]

for i in range(size):
    lst.append(random.randint(0, 20))
print('List1:\n', lst)

length = len(lst)
print('Length:', length)

value = int(input('Enter the value for insert to middle: '))
lst[int((length-1)/2)] = value
print('List2:\n', lst)

lst.pop()
print('List3:\n', lst)

length = len(lst)
print('Length:', length)


#3.2

beatles = []
print('Step 1')
print('Beatles:', beatles)

print('Step 2\n')
names = ['Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон']
for i in range(len(names)):
    beatles.append(names[i])
print('Beatles:', beatles)

print('\nStep 3')
names2 = ['Стю Сатклифф', 'Пит Лучший']
for i in range(len(names2)):
    flg = bool(input('Would you like to invite ' + str(names2[i]) + '?: '))
    if flg:
        beatles.append(names2[i])
print('Beatles:', beatles)

print('\nStep 4')
for i in range(len(names2)):
    flg = bool(input('Would you like to delete ' + str(names2[i]) + '?: '))
    if flg:
        for j in range(len(beatles)):
            if beatles[j] == names2[i]:
                del(beatles[j])
print('Beatles:', beatles)

print('\nStep 5')
names3 = ['Ринго Старра']
for i in range(len(names3)):
    flg = bool(input('Would you like to insert ' + str(names3[i]) + '?: '))
    if flg:
        beatles.insert(0, names3[i])
print('Beatles:', beatles)


#3.3
import random
size = int(input('Enter the size: '))
arr = ['']*size

for i in range(size):
    arr[i] = random.randint(0, 20)
print('Arr: \n', arr)

#Bubble sort
Sort = True
while Sort:
    Sort = False
    for i in range(size - 1):
        if arr[i] > arr[i + 1]:
            Sort = True
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
print('Bubble Arr: \n', arr)

arr.sort()
print('Bubble Arr: \n', arr)

arr.reverse()
print('Bubble Arr: \n', arr)