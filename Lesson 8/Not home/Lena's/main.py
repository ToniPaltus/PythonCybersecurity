# 1

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

def func(x):
    if x == 0:
        return 1.0
    return math.sin(x)/x

# Data for plotting
# Интервал изменения переменной по оси X
xmin = -20.0
xmax = 20.0

# Шаг между точками
dx = 0.01

# !!! Создадим список координат по оси X на отрезке [xmin; xmax], включая концы
xlist = np.arange(xmin, xmax, dx)

# Вычислим значение функции в заданных точках
ylist = [func(x) for x in xlist]
fig, ax = plt.subplots()
ax.plot(xlist, ylist)
ax.set(xlabel='points', ylabel='values', title='About as simple as it gets, folks')
ax.grid()

# !!! Покажем окно с нарисованным графиком
fig.savefig("test.png")
plt.show()
'''
# 2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# Data for plotting
'''