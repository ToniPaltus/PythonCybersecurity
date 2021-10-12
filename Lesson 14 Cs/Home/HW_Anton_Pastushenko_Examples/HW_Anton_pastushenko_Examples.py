# 1
'''
a1 = int(input("Enter: "))
print('Yes' if a1 in range(0, 5) else 'No')
'''
# 2
'''
a = int(input('Enter: '))
print([2**x for x in range(0, 21)])
print('YEs' if a in [2**x for x in range(0, 21)] else 'No')
'''
# 3
'''
a = int(input('Enter: '))
st = 'Yes' if a == 1 else 'No'
print(st, type(st))

b = int(input('Enter: '))

bol = True if b == 1 else False
print(bol, type(bol))
'''
# 4
'''
a, b, c = list(map(float, input('Enter: ').split()))
print(a, type(a))
print(b, type(b))
print(c, type(c))

a1, b1, c1 = map(float, input('Enter: ').split())
print(a1, type(a1))
print(b1, type(b1))
print(c1, type(c1))

res = int(a + b) if (a + b) % 1 == 0 else a + b
print(res, type(res))
'''
# 5
'''
li = [x for x in range(1, 4)]
print(li)

lii = li*2
print(lii)
'''
# 6
'''
a, b = list(map(int, input('Enter: ').split()))
print('a =', a, 'b =', b)
print()

print('logic of c:')
print('a + 1 =', a + 1)
for x in range(1, a + 1):
    print('x =', x)

c = [x for x in range(1, a + 1)]*2
print('c =', c)
n = b % a
print('n =', n)
print(*c[a - n: len(c) - n])

print(c[1:2])#element
print(*c[1:2])#value
'''
# 7
'''
#s = input('Enter: ').split()
s = '2 2 7 3 3 5 1 0'.split()
res = ''
while s != ['0']:
    n = int(s[0])
    x = ''.join(s[1: n + 1])
    res += str(n) + '' + x + ' '
    print(n, x)
    s = s[n + 1:]
print(res[:-1])
'''
# 8
'''
n = int(input('Enter: '))
s = [list(map(int, input('Enter: '))) for i in range(0, n)]
while True:
    print(s)
    if len(s) == 1:
        res = s[0][1] - s[0][0]
        break
    mn = max(s[0][0], s[1][0])
    mx = min(s[0][1], s[1][1])
    print(mx, mn)
    if mx < mn:
        res = 0
        break
    s = s[2:]
    s.append([mn, mx])
print(res)
'''
# 9 Лямбда
'''
f = lambda x: x * x
print(type(f))
print(f(5))

f = lambda x, y: x * y
print(f(5, 2))

f = lambda: True
print(f())
'''
# 10 enumerate
'''
seq = list('qwerty')
print(seq)
for i, val in enumerate(seq, start=1):
    print(f'№ {i} -> {val}')
'''
# 11 enumerate
'''
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(seasons, type(seasons)) #['Spring', 'Summer', 'Fall', 'Winter'] <class 'list'>
print(list(enumerate(seasons, start=1))) #[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
'''
# 12 enumerate
'''
grocery = ['bread', 'milk', 'butter']
for item in enumerate(grocery):
    print(item)
print()

for count, item in enumerate(grocery):
    print(count, item)
print()
'''
# 13 enumerate + lambda
'''
n = input('Enter: ')
s0 = list(map(int, input('Enter: ').split()))
print(s0)
s = s0[:]
print(s)
s = list(enumerate(s))
s.sort(key = lambda item: item[1])

sp1 = [s[-1], s[-2], s[-3]]
sp1.sort(key=lambda item: item[0])
sp2 = [s[0], s[1], s[-1]]
sp2.sort(key=lambda item: item[0])

p1 = sp1[-1][1] * sp1[-2][1] * sp1[-3][1]
p2 = sp2[0][1] * sp2[1][1] * sp2[-1][1]

res = str(sp2[0][1])+'' + str(sp2[1][1] + '' + str(sp2[2][1]))
if p1 > p2:
    res = str(sp1[0][1])+' '+str(sp1[1][1])+' '+str(sp1[2][1])
print(res)
'''
# 14
'''
def summa(a):
    x = list(str(a))
    print(sum(map(int, x)))
    return sum(map(int, x))
print(summa(56))
'''
# 15 ord() chr()
'''
print(ord('A'))
print(chr(65))
'''
# 16 Системы счисления
'''
n = 1
print(n, hex(n), oct(n), bin(n))
n1 = int('1')
print(n1, hex(n1), oct(n1), bin(n1))
a = 0x1
print(a)
b = 0x12
print(b)
'''
# 17 Перевод целого числа p -> 10
'''
p = 16
print(int('0xAA', p))
p = 8
print(int('0o1', p))

a = ord('A')
print(a, chr(a))
dictionary = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print(dictionary)
'''
# 18 Перевод целого числа 10 -> q
'''
digits = '0123456789'+''.join([chr(i) for i in range(ord('A'), ord('Z') + 1)])
print(digits)

def dec2k(num, k):
    if num < k:
        return digits[num]
    return dec2k(num//k, k) + digits[num % k]
print(dec2k(16**10-1, 33))
'''
# 19 Символы и коды
'''
s = 'Phython is the best programming language'
print([c for c in s])
print()

print([ord(c) for c in s])
print()

print([hex(ord(c)) for c in s])
print()

print({i: chr(i) for i in range(0, 128)})

print(''.join([hex(ord(c))[2:] for c in s]))
p = ''.join([hex(ord(c))[2:] for c in s])
p1 = [int(p[i:i+2], 16) for i in range(0, len(p), 2)]
print(p1)
p2 = [chr(int(p[i:i+2], 16)) for i in range(0, len(p), 2)]
print(p2)
p3 = ''.join(p2)
print(p3)


s = 'Питон - лучший язык программирования'
print([c for c in s], '\n', [ord(c) for c in s], '\n', [hex(ord(c)) for c in s])
'''
# 20 Строки и байты
'''
s = '╨Т╤Б╨╡╨╝ ╨╖╨┤╨░╤А╨╛╨▓╨░! ╨Я╤А╨╡╨┤╤Б╤В╨░╨▓╨╗╤П╨╡╨╝ ╨╜╨░╤И ╨╜╨╛╨▓╤Л╨╣ ╨д╨╗╨░╨│: ╤В╤А╨╕ ╤И╨╡╤Б╤В╤М ╤И╨╡╤Б╤В╤М ╤Б╨╡╨╝╤М ╨╜╨╛╨╗╤М ╨┤╨▓╨░ ╨▓╨╛╤Б╨╡╨╝╤М'
print(s.encode('cp866').decode())

s = 'Python is the best programming language'
print(s.encode())
s.encode()

s = 'Всем здарова! Представляем наш новый Флаг: шесть семьдесят восемь сорок тридцать семь'
s.encode()
print(s.encode())
'''
# 21 Евклид Нод
'''
def gcd1(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)
def gcd2(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        if a > b:
            return gcd2(a - b, b)
        else:
            return gcd2(a, b - a)
def gcd3(a, b):
    if b == 0:
        return a
    else:
        return gcd3(b, a % b)
def gcd4(a, b):
    while b:
        a, b = b, a % b
    return a
def gcd5(a, b):
    return gcd5(b, a % b) if b else a

gcd1(42, 12)
print(gcd2(42, 12))
print(gcd3(42, 12))
print(gcd4(42, 12))
print(gcd5(42, 12))
'''
# 22 Simple numbers
'''
def IsPrime1(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n
def IsPrime2(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
def IsPrime3(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n
print(IsPrime1(13))
print(IsPrime2(12))
print(IsPrime3(66))
'''
# 23 Факторизация
'''
def factorize1(n):
    divisor = 2
    while divisor ** 2 <= n:
        if n % divisor == 0:
            n //= divisor
            print(divisor)
        else:
            divisor += 1
    if n != 1:
        print(n)
def factorize2(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n //= i
        i += 1
    if n > 1:
        primfac.append(n)
    return primfac

n = int(input('Enter: '))
factorize1(n)
print(factorize2(n))
'''
# 24 Каноническое разложение числа n
'''
def Factor(n):
    Ans = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            Ans.append(d)
            n//=d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans
print(Factor(33))
'''