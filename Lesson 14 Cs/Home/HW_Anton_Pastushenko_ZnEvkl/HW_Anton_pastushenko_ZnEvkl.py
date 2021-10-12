# Расширенный алгоритм Евклида
'''
from math import gcd

def findModInversw(a, n):
    if gcd(a, n) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, n
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q*v1), (u2 - q*v2), (u3 - q*v3), v1, v2, v3
    return u1 % n
c = findModInversw(2, 13)
print(c, (c * 2) % 13)
'''
# кольцо Zn
'''
a = -3
n = 5
print(a % n)
print((a + n) % n)
print(3.5 % 5, -3.5 % 5)

n = 1
if n % 1 == 0:
    print('Целое')
else:
    print('Не целое')
'''
