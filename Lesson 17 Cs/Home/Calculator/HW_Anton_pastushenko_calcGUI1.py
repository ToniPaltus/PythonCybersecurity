# Калькулятор GUI
import re
from tkinter import *

def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return 'Division is not possible!'
def multiplication(a, b):
    return a * b
def ost_division(a, b):
    if b != 0:
        return a % b
    else:
       return 'Ost_division is not possible!'
def revers(a):
    return a**-1
def degree(a):
    return a**2

table = Tk()
table.title('Калькулятор')
table.geometry('415x550')
table['bg'] = 'lightgrey'

x1, x2, x3, x4 = 3, 106, 209, 312
y1, y2, y3, y4, y5 = 473, 400, 327, 254, 182

# Верхний ряд (декор)
btn_clear = Button(table, text='Очистить', height=2, width=10, font=('Arial Bold', 13), bg='pink')
btn_clear.place(x=3, y=3)
btn_type = Button(table, text='Обычный (c 2-мя числами)', width=25, height=2, font=('Arial Bold', 13), bg='pink')
def foo_clear():
    res_lbl['text'] = ''
btn_clear['command'] = foo_clear
btn_type.place(x=106, y=3)
btn__ = Button(table, text='--\n--', height=2, width=6, font=('Arial Bold', 13), bg='pink')
btn__.place(x=344, y=3)

# Окно
res_lbl = Label(table, width=31, height=3, font=('Arial Bold', 17), bg='lightblue', border=1)
res_lbl.place(x=3, y=63)

# 1 ряд
btn_persent = Button(table, text='%', width=10, height=3, font=('Arial Bold', 13))
btn_persent.place(x=x1, y=y5)
def foo_btn_persent():
    res_lbl['text'] += btn_persent['text']
btn_persent['command'] = foo_btn_persent

btn_revers = Button(table, text='^ = 1/x', width=10, height=3, font=('Arial Bold', 13))
btn_revers.place(x=x2, y=y5)
def foo_btn_revers():
    res_lbl['text'] += '^'
btn_revers['command'] = foo_btn_revers

btn_deg = Button(table, text='^^ = x^2', width=10, height=3, font=('Arial Bold', 13))
btn_deg.place(x=x3, y=y5)
def foo_btn_deg():
    res_lbl['text'] += '^^'
btn_deg['command'] = foo_btn_deg

btn_del = Button(table, text='/', width=10, height=3, font=('Arial Bold', 13))
btn_del.place(x=x4, y=y5)
def foo_btn_del():
    res_lbl['text'] += btn_del['text']
btn_del['command'] = foo_btn_del

# 2 ряд
btn_7 = Button(table, text='7', width=10, height=3, font=('Arial Bold', 13))
btn_7.place(x=x1, y=y4)
def foo_btn_7():
    res_lbl['text'] += btn_7['text']
btn_7['command'] = foo_btn_7

btn_8 = Button(table, text='8', width=10, height=3, font=('Arial Bold', 13))
btn_8.place(x=x2, y=y4)
def foo_btn_8():
    res_lbl['text'] += btn_8['text']
btn_8['command'] = foo_btn_8

btn_9 = Button(table, text='9', width=10, height=3, font=('Arial Bold', 13))
btn_9.place(x=x3, y=y4)
def foo_btn_9():
    res_lbl['text'] += btn_9['text']
btn_9['command'] = foo_btn_9

btn_mult = Button(table, text='*', width=10, height=3, font=('Arial Bold', 13))
btn_mult.place(x=x4, y=y4)
def foo_btn_mult():
    res_lbl['text'] += btn_mult['text']
btn_mult['command'] = foo_btn_mult

# 3 ряд
btn_4 = Button(table, text='4', width=10, height=3, font=('Arial Bold', 13))
btn_4.place(x=x1, y=y3)
def foo_btn_4():
    res_lbl['text'] += btn_4['text']
btn_4['command'] = foo_btn_4

btn_5 = Button(table, text='5', width=10, height=3, font=('Arial Bold', 13))
btn_5.place(x=x2, y=y3)
def foo_btn_5():
    res_lbl['text'] += btn_5['text']
btn_5['command'] = foo_btn_5

btn_6 = Button(table, text='6', width=10, height=3, font=('Arial Bold', 13))
btn_6.place(x=x3, y=y3)
def foo_btn_6():
    res_lbl['text'] += btn_6['text']
btn_6['command'] = foo_btn_6

btn_minus = Button(table, text='-', width=10, height=3, font=('Arial Bold', 13))
btn_minus.place(x=x4, y=y3)
def foo_btn_minus():
    res_lbl['text'] += btn_minus['text']
btn_minus['command'] = foo_btn_minus

# 4 ряд
btn_1 = Button(table, text='1', width=10, height=3, font=('Arial Bold', 13))
btn_1.place(x=x1, y=y2)
def foo_btn_1():
    res_lbl['text'] += btn_1['text']
btn_1['command'] = foo_btn_1

btn_2 = Button(table, text='2', width=10, height=3, font=('Arial Bold', 13))
btn_2.place(x=x2, y=y2)
def foo_btn_2():
    res_lbl['text'] += btn_2['text']
btn_2['command'] = foo_btn_2

btn_3 = Button(table, text='3', width=10, height=3, font=('Arial Bold', 13))
btn_3.place(x=x3, y=y2)
def foo_btn_3():
    res_lbl['text'] += btn_3['text']
btn_3['command'] = foo_btn_3

btn_plus = Button(table, text='+', width=10, height=3, font=('Arial Bold', 13))
btn_plus.place(x=x4, y=y2)
def foo_btn_plus():
    res_lbl['text'] += btn_plus['text']
btn_plus['command'] = foo_btn_plus

# 5 ряд
btn_znak = Button(table, text='+/-', width=10, height=3, font=('Arial Bold', 13))
btn_znak.place(x=x1, y=y1)
def foo_btn_znak():
    res_lbl['text'] += '-'
btn_znak['command'] = foo_btn_znak

btn_0 = Button(table, text='0', width=10, height=3, font=('Arial Bold', 13))
btn_0.place(x=x2, y=y1)
def foo_btn_0():
    res_lbl['text'] += btn_0['text']
btn_0['command'] = foo_btn_0

btn_tch = Button(table, text='.', width=10, height=3, font=('Arial Bold', 13))
btn_tch.place(x=x3, y=y1)
def foo_btn_tch():
    res_lbl['text'] += btn_tch['text']
btn_tch['command'] = foo_btn_tch

btn_equal = Button(table, text='=', width=10, height=3, font=('Arial Bold', 13), bg='purple')
btn_equal.place(x=x4, y=y1)
def foo_btn_equal():
    my_str = res_lbl['text']
    res = 0.0
    values = re.findall(r'\d*\.\d+|\d+', my_str)
    values = [float(i) for i in values]
    if my_str[0] == '-':
        values[0] *= -1
    print('Values:', values, type(values[0]))

    znak = re.findall(r'\W+', my_str)
    if '.' in znak:
        znak.remove('.')
    print('Znak:', znak[0], type(znak[0]))
    if znak[0] == '+':
        res = plus(values[0], values[1])
    elif znak[0] == '-':
        res = minus(values[0], values[1])
    elif znak[0] == '*':
        res = multiplication(values[0], values[1])
    elif znak[0] == '/':
        res = division(values[0], values[1])
    elif znak[0] == '%':
        res = ost_division(values[0], values[1])
    elif znak[0] == '^':
        res = revers(values[0])
    elif znak[0] == '^^':
        res = degree(values[0])
    print('Res:', res, type(res))
    res_lbl['text'] = str(res)
btn_equal['command'] = foo_btn_equal

table.mainloop()