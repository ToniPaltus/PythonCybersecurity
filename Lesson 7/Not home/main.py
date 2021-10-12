'''def trace(func):
    def inner(*args, **kwargs):
        print(func, __name__, args, kwargs)
        return func(*args, **kwargs)
    return inner
@trace
def foo(x):
    return x
@trace
def boo(x, y):
    return x + y


print(foo(15))
print(boo(15, 5))'''


import time

def timer(func):
    def inner(*args, **kwargs):
        print('Начало таймера')
        start = time.time()
        func(*args, **kwargs)
        stop = time.time() - start
        print('Конец таймера, функция выполнилась за:', stop)
        return inner

@timer
def f():
    print('Function F is running')
    time.sleep(5)
    print('Function F did run')

@timer
def fun():
    print('aaa')
fun()




