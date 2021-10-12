from math import gcd

a = int(input('Enter a: '))
b = int(input('Enter b: '))
'''
min = min(a, b)
max = max(a, b)

current_max = max
current_min = min
prev_max = min
prev_q = 0

iter = 1
while current_min != 0:
    print(iter)
    if iter > 1:
        prev_q = current_q
    current_q = current_max // current_min
    print('q:', current_q)

    current_min = current_max % current_min
    print('min:', current_min)

    current_max = prev_max
    print('cur_max:', current_max)

    prev_max = current_min
    print('pr_max:', current_max)


   # x = prev2_x - prev_q * prev_x
   # y = prev2_y - prev_q * prev_y

    print('________________')
    iter += 1





# gcd = max * x + min * y //y = max % min //x = (gcd - min * (max % min))/(max)
print(gcd(a, b))
y = max % min
#x = (gcd(a, b) - min * (max % min)) / max
x = int((prev_max - min * (max % min)) / max)

print('x:', x)
print('y:', y)
print(gcd(a, b) == max*x + min*y)
#print(current_max == *x + b*y)
'''

'''
for i in range(-20, 20):
    for j in range(-20, 20):
        if gcd(a, b) == a*i + b * j:
            print(i)
            print(j)
'''


def bezout(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
    return (x, y, a)


x, y, a = bezout(a, b)
print('x:', x)
print('y:', y)
print('a:', a)
print('gcd:', gcd(a, b))
print(gcd(a, b) == (a * x + b * y))

