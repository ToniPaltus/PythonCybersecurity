import traceback
from tkinter import *
root = Tk()

# Окно с кнопкой + Задание свойств виджета
'''
btn1 = Button(root)
btn1['text'] = 'Превед'
btn1['bg'] = 'blue'
btn1['fg'] = 'white'
btn1.place(x=100, y=50)

btn2 = Button(root, text='Медвед', bg='green', fg='white')
btn2.place(x=200, y=50)

btn3 = Button(root)
btn3.config(text='Медвед2', bg='blue', fg='white')
btn3.place(x=300, y=50)

root.mainloop()
'''
# Связывание действий
'''
btn1 = Button(root, text='Привет', bg='blue', fg='white')
btn2 = Button(root, text='Медвед', bg='blue', fg='white')
btn1.place(x=100, y=50)
btn2.place(x=200, y=50)

def foo1():
    root.title(btn1['text'])
def foo2():
    root.title(btn2['text'])

btn1['command'] = foo1#Здесь можно присвоить функцию только без параметров
btn2['command'] = foo2

#def foo(button, root):
    #root.title(button['text'])
#btn1['command'] = lambda: foo(btn1, root)
#btn2['command'] = lambda: foo(btn2, root)

root.mainloop()
'''
# Калькулятор
'''
def sum(str):
    lst = str.split('+')
    summa = 0
    for x in lst:
        if x.isdigit():
            summa += int(x)
    return summa

root['width'] = 400
root['height'] = 200

entry = Entry(root, width=25)#Ввод
entry.place(x=20, y=20)

btn = Button(root, text='Вычислить')
btn.place(x=20, y=50)

lbl = Label(root)
lbl.place(x=200, y=20)

def btn_command():
    res = sum(entry.get())
    lbl['text'] = '= ' + str(res)

btn['command'] = btn_command
root.mainloop()
'''
# Метки
'''
label1 = Label(root, text='Это метка!\nИз двух строк.', font='Arial 18')
label1.place(x=0, y=0)

entry = Entry(root, width=20, bd=3)
entry.place(x=70, y=70)

text = Text(root, width=30, height=5, font='Verdana 12', wrap=WORD)
text.place(x=100, y=100)

root.mainloop()
'''
# Переменные + радиокнопки + флажки + списки
'''
v = StringVar()
v.set('Hello!')
ent = Entry(root, width=20, bd=3, textvariable=v)
ent.place(x=0, y=0)
# _______________________________
var1 = IntVar()
var1.set(1)

var2 = IntVar()
var2.set(0)

# Эти кнопки объединяет в группу переменная var1
r1 = Radiobutton(root, text='Первая', variable=var1, value=0)
r2 = Radiobutton(root, text='Вторая', variable=var1, value=1)

r1.place(x=0, y=25)
r2.place(x=0, y=50)
#Эти кнопки объединяют в группу переменная var2
r3 = Radiobutton(root, text='Третья', variable=var2, value=0)
r4 = Radiobutton(root, text='Четвертая', variable=var2, value=1)
r3.place(x=80, y=25)
r4.place(x=80, y=50)
# _______________________________

v1 = IntVar()
v2 = IntVar()

check1 = Checkbutton(root, text='Первый флажок', variable=v1, onvalue=1, offvalue=0)
check2 = Checkbutton(root, text='Второй флажок', variable=v2, onvalue=5, offvalue=0)
check1.place(x=160, y=25)
check2.place(x=160, y=50)
# _______________________________

words = ['Linux', 'Python', 'Tk', 'Tkinter']
listbox = Listbox(root, selectmode=SINGLE, height=4)
#Заполнение списка пунктами
for i in words:
    listbox.insert(END, i)
listbox.place(x=0, y=75)

root.mainloop()
'''
# Мессенджеры расположения
'''
# place
entry = Entry(root, width=25)
entry.place(x=20, y=20)

lbl = Label(root, text='=1000')
lbl.place(x=200, y=20)

btn = Button(root, text='Вычислить')
btn.place(x=20, y=50)

# pack
entry = Entry(root, width=25)
entry.pack()

lbl = Label(root, text='=1000')
lbl.pack()

btn = Button(root, text='Вычислить')
btn.pack()

root.mainloop()
'''
# Pack
'''
entry = Entry(root, width=25)
S = TOP
entry.pack(side=S)

lbl = Label(root, text='=1000', bg='gray')
lbl.pack(side=S)

btn = Button(root, text='Вычислить')
btn.pack(side=S)

root.mainloop()
'''
# Pack + Frame
'''
frame1 = Frame(root, bg='gray', bd=5)
frame2 = Frame(root, bg='gray', bd=5)
frame1.pack()
frame2.pack()

entry = Entry(frame1, width=25)
entry.pack(side=LEFT)

lbl = Label(frame1, text='1000', bg='blue')
lbl.pack(side=LEFT)

btn = Button(frame2, text='Вычислить')
btn.pack()

root.mainloop()
'''
# grid(табличка)
'''
entry = Entry(root, width=25)
entry.grid(row=0, column=0, padx=5, pady=5)

lbl = Label(root, text='=1000', bg='gray')
lbl.grid(row=0, column=1, padx=5, pady=5)

btn = Button(root, text='Вычислить')
btn.grid(row=1, column=0, columnspan=2)

root.mainloop()
'''
# place(резиновые координаты)
'''
entry = Entry(root, width=25)
entry.place(relx=0.1, rely=0.1)

lbl = Label(root, text='=1000', bg='gray')
lbl.place(relx=0.7, rely=0.1)

btn = Button(root, text='Вычислить')
btn.place(relx=0.4, rely=0.5)

root.mainloop()
'''
# Событие метод bind()
'''
Метод bind() принимает три аргумента:
1)название события
2)функцию, которая будет вызвана при наступлении события
3)третий аргумент необязательный строка "+" означает, что эта
привязка добавляется к уже существующим.
'''
frame = Frame(root, width=400, height=400, bg='pink')
frame.pack()

def my(e):
    btn = Button(frame, text='XYЙ')
    btn.place(x=e.x, y=e.y)
frame.bind('<Button-1>', my)

def show(ev):
    '''выводит координаты мыши в заголовок окна'''
    str = 'x = {0} y = {1}'.format(ev.x, ev.y)
    root = ev.widget.master
    root.title(str)
frame.bind('<Motion>', show)

root.mainloop()

#Рисование на холсте
'''
root['width'] = 520
root['height'] = 520
canvas = Canvas(root, width=500, height=500, bg='lightblue', cursor='pencil')
canvas.place(x=10, y=10)

canvas.create_line(200, 50, 300, 50, width=3, fill='blue')
canvas.create_line(0, 0, 100, 100, width=2, arrow=LAST)

x = 75
y = 110
canvas.create_rectangle(x, y, x + 80, y + 50, fill='white', outline='blue')
canvas.create_polygon([250, 100], [200, 150], [300, 150], fill='yellow')
canvas.create_polygon([300, 80], [400, 80], [450, 75], [450, 200], [300, 180], [330, 160], outline='white', smooth=1, fill='green')
canvas.create_oval([20, 200], [150, 300], fill='gray50')

root.mainloop()
'''
