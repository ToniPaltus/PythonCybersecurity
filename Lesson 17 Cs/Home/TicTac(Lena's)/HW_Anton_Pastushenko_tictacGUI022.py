import tkinter
from tkinter import *
root = Tk()

def vin(li):
    victory ={1: ('1', '2', '3'), 2: ('3', '6', '9'), 3: ('1', '4', '7'), 4: ('7', '8', '9'), 5: ('1', '5', '9'), 6: ('2', '5', '8'), 7: ('3', '5', '7'), 8: ('4', '5', '6')}
    for i in victory.values():
        cnt1 = 0
        for j in li:
            if j in i:
                # print(i, ' good job')
                cnt1 += 1
            # else:
                # print('lox')
        if cnt1 == 3:
            if cnt %2 == 0:
                print('CROSSES VIN!')
            else:
                print('ZEROES WIN!')
            exit(990)
def com(btn):
    global cnt
    global listX, list0

    if btn['text'] in range(0, 10) or btn['text'] == 'X' or btn['text'] == '0':
        return
    elif cnt % 2 == 0:

        listX.append(btn['text'])
        btn['text'] = 'X'
        vin(listX)

    elif cnt % 2 == 1:
        list0.append(btn['text'])
        btn['text'] = '0'
        vin(list0)

    # print('lox')
    cnt += 1
    # print(cnt)
    # print('0: ', list0)
    # print('X: ', listX)

listX = []
list0 = []
cnt = 0
btn1 = Button(root, text='1')
btn1.place(relx=0, rely=0, relh=1 / 3, relw=1 / 3)
btn1['command'] = lambda: com(btn1)

btn2 = Button(root, text='2')
btn2.place(relx=1 / 3, rely=0, relh=1 / 3, relw=1 / 3)
btn2['command'] = lambda: com(btn2)

btn3 = Button(root, text='3')
btn3.place(relx=2 / 3, rely=0, relh=1 / 3, relw=1 / 3)
btn3['command'] = lambda: com(btn3)

btn4 = Button(root, text='4')
btn4.place(relx=0, rely=1 / 3, relh=1 / 3, relw=1 / 3)
btn4['command'] = lambda: com(btn4)

btn5 = Button(root, text='5')
btn5.place(relx=1 / 3, rely=1 / 3, relh=1 / 3, relw=1 / 3)
btn5['command'] = lambda: com(btn5)

btn6 = Button(root, text='6')
btn6.place(relx=2 / 3, rely=1 / 3, relh=1 / 3, relw=1 / 3)
btn6['command'] = lambda: com(btn6)

btn7 = Button(root, text='7')
btn7.place(relx=0, rely=2 / 3, relh=1 / 3, relw=1 / 3)
btn7['command'] = lambda: com(btn7)

btn8 = Button(root, text='8')
btn8.place(relx=1 / 3, rely=2 / 3, relh=1 / 3, relw=1 / 3)
btn8['command'] = lambda: com(btn8)

btn9 = Button(root, text='9')
btn9.place(relx=2 / 3, rely=2 / 3, relh=1 / 3, relw=1 / 3)
btn9['command'] = lambda: com(btn9)

root.mainloop()