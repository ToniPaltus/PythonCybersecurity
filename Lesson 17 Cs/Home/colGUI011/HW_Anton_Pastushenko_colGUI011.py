'''
Расположить в окне три кнопки с надписями "Красный", "Зеленый",
"Синий". При нажатии на кнопку окно должно окрашиваться в
соответствующий цвет.
'''

from tkinter import *
root = Tk()
root['bg'] = 'gray'

# Мой
red_btn = Button(root, text='Red', bg='red', fg='white')
red_btn.place(relx=0.1, rely=0.1)
def red():
    root['bg'] = 'red'
    root.title(red_btn['text'])
red_btn['command'] = red

green_btn = Button(root, text='Green', bg='green', fg='white')
green_btn.place(relx=0.3, rely=0.1)
def green():
    root['bg'] = 'green'
    root.title(green_btn['text'])
green_btn['command'] = green

blue_btn = Button(root, text='Blue', bg='blue', fg='white')
blue_btn.place(relx=0.55, rely=0.1)
def blue():
    root['bg'] = 'blue'
    root.title(blue_btn['text'])
blue_btn['command'] = blue

# Вариант - 1
'''
def paintRed(): root.config(bg='red')
def paintGreen(): root.config(bg='green')
def paintBlue(): root.config(bg='blue')

red_btn = Button(root, text='Red', command=paintRed)
red_btn.pack(side=LEFT)

green_btn = Button(root, text='Green', command=paintGreen)
green_btn.pack(side=LEFT)

blue_btn = Button(root, text='Blue', command=paintBlue)
blue_btn.pack(side=LEFT)
'''
# Вариант - 2
'''
def paint(color): root.config(bg=color)
buttons = [
    Button(root, text='Red', command=lambda: paint('red')),
    Button(root, text='Green', command=lambda: paint('green')),
    Button(root, text='Blue', command=lambda: paint('blue'))
]

for btn in buttons:
    btn.pack(side=RIGHT)
'''
# Вариант - 3
'''
def click(e):
    root.config(bg=e.widget.color)
for color in ['Red', 'Green', 'Blue']:
    btn = Button(root, text=color)
    btn.bind('<Button-1>', click)
    btn.color = color
    btn.pack(side=LEFT)
'''
root.mainloop()