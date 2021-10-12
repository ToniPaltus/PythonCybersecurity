import numpy as np

def ahah(length=5, explosive=False, typos=0.05, exclamation=0, caps=False):
    s = []
    # Работаем отдельно с блоками столько раз, сколько length
    for i in range(length):
        block = ''.join(np.random.permutation(['a', 'x']))
        # Если ошибки, заменяем случайным образом
        if typos > 0:
            block = block.replace('a', 'n', np.random.binomial(n=1, p=typos, size = 1)[0]).replace('x', 'з', np.random.binomial(n = 1, p = typos, size = 1)[0])
        # Добавляем блок в список
        s.append(block)

    # Соединяем блоки вместе в единую строку
    s = ''.join(s)

    # Если взрывной, то начинается с 'пх'
    if explosive:
        s = 'пх' + s[2:]

    # Добавляем воскл. знаки
    s += ''.join(np.random.choice(['1', '!'], size = exclamation))

    # Возвращаем капсом или нет
    return s.upper() if caps else s

print(ahah(length=5, explosive=True, typos=0.5, exclamation=5, caps=True))