#Кнопки которые меняются местами при нажатии на одну из них
import tkinter
from tkinter import *
root = Tk()
root.title('Прекол')
root['width'] = 250
root['height'] = 150

btn1 = Button(root, text='Привет', bg='green', fg='white')
btn2 = Button(root, text='Медвет', bg='blue', fg='white')
btn1.place(x=50, y=50)
btn2.place(x=150, y=50)

reserve = []
def foo_btn_1():
    reserve.append(btn1['text'])
    reserve.append(btn1['bg'])
    reserve.append(btn1['command'])

    btn1['text'] = btn2['text']
    btn1['bg'] = btn2['bg']
    btn1['command'] = btn2['command']

    btn2['text'] = reserve[0]
    btn2['bg'] = reserve[1]
    btn2['command'] = reserve[2]

    reserve.clear()
def foo_btn_2():
    reserve.append(btn2['text'])
    reserve.append(btn2['bg'])
    reserve.append(btn2['command'])

    btn2['text'] = btn1['text']
    btn2['bg'] = btn1['bg']
    btn2['command'] = btn1['command']

    btn1['text'] = reserve[0]
    btn1['bg'] = reserve[1]
    btn1['command'] = reserve[2]

    reserve.clear()

btn1['command'] = foo_btn_1
btn2['command'] = foo_btn_2

root.mainloop()














