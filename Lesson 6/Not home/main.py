# 1
'''
def research_min(a, b):
    return a if a < b else b

a = int(input('Enter value: '))
b = int(input('Enter value: '))

c = research_min(a, b)
print(c)
'''

# 2
'''
def research_mim(*args):
    return min(args)
c = research_mim(1 , 3, 4, 8, -7, 5)
print(c)
'''
# 3 min in range

def min_in_range(first = 'Empty string', *args, my_min = float('-inf'), my_max = float('inf')):
    min_value = my_max
    for item in (first, ) + args:
        if item < min_value and my_min < item < my_max:
            min_value = item
    return max(min_value, my_min)

c = min_in_range(1, 5, 2, 8, 7, -8, my_min=1, my_max=10)
print(c)
