# Шифр Цезаря
'''
alef = [(i - ord('A'), chr(i)) for i in range(ord('A'), ord('Z') + 1)]
print(alef)
CN = {x[1]: x[0] for x in alef}
NC = {x[0]: x[1] for x in alef}
print(CN)
print(NC)

Massage = input('Enter: ').upper()
k = int(input('Enter: '))
Encode = [NC[(CN[m] + k) % len(alef)] for m in Massage]
print(Encode)
'''
# Шифр Цезаря 2
'''
alef = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
CN = {c: ord(c) - ord('A') for c in alef}
NC = {ord(c) - ord('A'): c for c in alef}

for i in range(0, 3):
    k = int(input('Enter: '))
    Massage = input('Enter: ').upper()
    print(''.join(NC[(CN[m] + k) % 26] if m in alef else m for m in Massage))
'''
# Шифр Цезаря 3
'''
def ECeasar(massage, k):
    alef = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    CN = {c: ord(c) - ord('A') for c in alef}
    NC = {ord(c) - ord('A'): c for c in alef}

    return ''.join([NC[(CN[m] + k) % 26] if m in alef else m for m in massage])
k = int(input('Enter k: '))
massage = input('Enter massage: ').upper()
print(ECeasar(massage, k))
'''
# Афинный шифр Цезаря

alef = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print('Alef:', alef)
NC = {ord(c) - ord('A'): c for c in alef}
CN = {c: ord(c) - ord('A') for c in alef}
print('NC:', NC)
print('CN:', CN)

k1, k2 = list(map(int, input('Enter keys: ').split()))
massage = input('Enter massage: ').upper()
encode = ''.join([NC[(CN[m] + k1) * k2 % 26] if m in alef else m for m in massage])
print(encode)

# Дешифрование
'''
# ci = (mi / k2 - k1) % 26 = (mi * k2^(-1) + k1) % 26
# k2 = 1 3 5 7 9 11 13 15 17 19 21 23 25
def findModInvese(a, n):
    from math import gcd

    if gcd(a, n) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, n

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % n

alef = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
CN = {c: ord(c) - ord('A') for c in alef}
NC = {ord(c) - ord('A'): c for c in alef}

k1, k2 = list(map(int, input('Enter keys: ').split()))
C = input('Enter encode: ').upper()
k2_1 = findModInvese(k2, 26)
massage = ''.join([NC[((CN[c] * k2_1) - k1) % 26] if c in alef else c for c in C])
print(massage)
'''
# Шифр Вижинера
'''
alef = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print(alef)

CN = {c: ord(c) - ord('A') for c in alef}
NC = {ord(c) - ord('A'): c for c in alef}
print('NC:', NC)
print('CN:', CN)

M = 'REGULAR EXPRESSIONS (REGEX / REGEXP)'
key = 'ONETWO'
print('Фраза:', M, 'Ключ:', key, len(key))

key = key * (len(M) // len(key) + 1)
print('Фраза:', M, 'Ключ:', key, len(key))
# C = "".join([NC[(alef.index(m)+alef.index(k)) % 26] if m in alef else m for (m, k) in zip(M,key)])
C = ''.join([NC[(CN[m] + CN[k]) % 26] if m in alef else m for(m, k) in zip(M, key)])
print('Encode:', C)
'''