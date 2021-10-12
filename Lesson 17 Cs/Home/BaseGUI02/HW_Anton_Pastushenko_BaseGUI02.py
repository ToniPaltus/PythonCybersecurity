'''
02.
Спроектировать пользовательский интерфейс и написать
программу для перевода чисел в p ичную систему счисления. Число
и основание системы вводит пользователь.
16 16--10 16--8 16--2
10 10--2 10--8 10--16
8 8--10 8--2 8--16
2 2--10 2--8 2--16
поле для числа и 3 окошка с результатами + кнопка Вычислить1.. n"
'''
from tkinter import *
root = Tk()

root['width'] = 480
root['height'] = 120
root.title('Переводчик')

lbl1_enter = Label(root, text='Введите 16: 0x')
lbl1_enter.place(x=0, y=10)
lbl2_enter = Label(root, text='Введите 10: 0d')
lbl2_enter.place(x=0, y=35)
lbl3_enter = Label(root, text='Введите 8:  0o')
lbl3_enter.place(x=0, y=60)
lbl4_enter = Label(root, text='Введите 2:  0b')
lbl4_enter.place(x=0, y=85)

entry1 = Entry(root, width=15)
entry1.place(x=80, y=10)
entry2 = Entry(root, width=15)
entry2.place(x=80, y=35)
entry3 = Entry(root, width=15)
entry3.place(x=80, y=60)
entry4 = Entry(root, width=15)
entry4.place(x=80, y=85)

calc_butn1 = Button(root, text='Вычислить', fg='black')
calc_butn1.place(x=400, y=10)
def calc_1():
    lbl11['text'] = int('0x' + entry1.get(), 16)
    lbl12['text'] = oct(int('0x' + entry1.get(), 16))
    lbl13['text'] = bin(int('0x' + entry1.get(), 16))
calc_butn1['command'] = calc_1

calc_butn2 = Button(root, text='Вычислить', fg='black')
calc_butn2.place(x=400, y=35)
def calc_2():
    lbl21['text'] = bin(int(entry2.get()))
    lbl22['text'] = oct(int(entry2.get()))
    lbl23['text'] = hex(int(entry2.get()))
calc_butn2['command'] = calc_2

calc_butn3 = Button(root, text='Вычислить', fg='black')
calc_butn3.place(x=400, y=60)
def calc_3():
    lbl31['text'] = int('0o' + entry3.get(), 8)
    lbl32['text'] = bin(int('0o' + entry3.get(), 8))
    lbl33['text'] = hex(int('0o' + entry3.get(), 8))
calc_butn3['command'] = calc_3

calc_butn4 = Button(root, text='Вычислить', fg='black')
calc_butn4.place(x=400, y=85)
def calc_4():
    lbl41['text'] = int('0b' + entry4.get(), 2)
    lbl42['text'] = oct(int('0b' + entry4.get(), 2))
    lbl43['text'] = hex(int('0b' + entry4.get(), 2))
calc_butn4['command'] = calc_4

lbl11 = Label(root, text='---')
lbl11.place(x=200, y=10)
lbl21 = Label(root, text='---')
lbl21.place(x=200, y=35)
lbl31 = Label(root, text='---')
lbl31.place(x=200, y=60)
lbl41 = Label(root, text='---')
lbl41.place(x=200, y=85)

lbl12 = Label(root, text='---')
lbl12.place(x=250, y=10)
lbl22 = Label(root, text='---')
lbl22.place(x=250, y=35)
lbl32 = Label(root, text='---')
lbl32.place(x=250, y=60)
lbl42 = Label(root, text='---')
lbl42.place(x=250, y=85)

lbl13 = Label(root, text='---')
lbl13.place(x=300, y=10)
lbl23 = Label(root, text='---')
lbl23.place(x=300, y=35)
lbl33 = Label(root, text='---')
lbl33.place(x=300, y=60)
lbl43 = Label(root, text='---')
lbl43.place(x=300, y=85)

root.mainloop()