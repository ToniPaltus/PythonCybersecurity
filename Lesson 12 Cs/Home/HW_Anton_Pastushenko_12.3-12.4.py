#12.3 Найти все простые числа от 0 до 100 (функция)
print('Simple:', [x for x in range(2, int(input('Max border: ')) + 1) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
#12.4 Посчитать первые 35 чисел Фибоначчи. функции Вывести только нечётные.
'''
def fib(n):
    if n == 1 or n == 0:
        return 1
    return fib(n - 1) + fib(n - 2)
n = int(input('Enter n: '))
for i in range(1, n + 1, 2):
    print(i, ')', fib(i), sep='')
'''