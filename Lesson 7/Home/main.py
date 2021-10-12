# 1.
# Учитывая массив целых чисел, удалите наименьшее значение. Не изменяйте исходный массив / список.
# Если есть несколько элементов с одинаковым значением, удалите тот, у которого индекс ниже.
# Если вы получили пустой массив / список, верните пустой массив / список.
# remove_smallest ([1,2,3,4,5]) = [2,3,4,5]
# remove_smallest ([5,3,2,1,4]) = [5,3,2,4]
# remove_smallest ([2,2,1,2,1]) = [2,2,2,1]

'''
import random
def remove_smallest(lst):
    if lst != []:
        print('min element:', lst[lst.index(min(lst))], 'index:', lst.index(min(lst)))
        lst.remove(lst[lst.index(min(lst))])
    return lst

size = int(input('Enter size: '))
lst = [random.randint(0, 10) for i in range(size)]
print('Lst:', lst)
lst = remove_smallest(lst)
print('Lst:', lst)
'''

# 2
# Реализуйте функцию unique_in_order, которая принимает в качестве аргумента последовательность и возвращает список элементов.
# без каких-либо элементов с одинаковым значением рядом друг с другом и с сохранением исходного порядка элементов.
# unique_in_order ('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order ('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order ([1,2,2,3,3]) == [1,2,3]
import random

'''
def unique_in_order(lst):
    i = 0
    while i < (len(lst) - 1):
        while lst[i] == lst[i + 1]:
            del lst[i]
            i -= 1
        i += 1
    return lst

lst = list(input('Enter string: ').split(' '))
print(lst)
lst = unique_in_order(lst)
print(lst)
'''

# 3
# Напишите алгоритм, который берет массив и перемещает все нули в конец,
# сохраняя порядок остальных элементов.
# move_zeros ([false, 1,0,1,2,0,1,3, «a»]) # возвращает [false, 1,1,2,1,3, «a», 0,0]


def move_zeros(lst):
    for i in range(len(lst)):
        if str(lst[i]) == '0':
            lst.append(0)
            lst.remove(0)
    return lst
def show(lst):
    print(lst)
    print('0:', lst.count(0))

size = int(input('Enter size: '))
lst = [random.randint(0, 3) for i in range(size)]
show(lst)
lst = move_zeros(lst)
show(lst)



# 4
# Напишите функцию cakes (), которая принимает рецепт (объект) и доступные ингредиенты (также объект) и
# возвращает максимальное количество пирожных, которое Пит может испечь (целое число). Для простоты нет единиц измерения сумм.
# (например, 1 фунт муки или 200 г сахара - это просто 1 или 200). Ингредиенты, которых нет в предметах,
# можно рассматривать как 0.
# торты ({мука: 500, сахар: 200, яйца: 1}, {мука: 1200, сахар: 1200, яйца: 5, молоко: 200}) -> 2

'''
def cakes():
    lst = []
    for key in ingredients.keys():
        lst.append(int(ingredients[key] / resept_for_one[key]))
    return min(lst)


resept_for_one = {
    'flour': 200,
    'sugar': 50,
    'egg': 1,
    'milk': 30
}
print('For one cake you need:')
for key, value in resept_for_one.items():
    print(f'{value} of {key}')
ingredients = {
    'flour': 0,
    'sugar': 0,
    'egg': 0,
    'milk': 0
}

for key in ingredients.keys():
    ingredients[key] = int(input(f'Enter count of {key}: '))
print('Your ingredients:', ingredients)
cake = cakes()
print('Cakes:', cake)
'''