from tkinter import *
table = Tk()
table.geometry('250x250')
table.title('TicTac')

result = Tk()
result.geometry('230x30')
result.title('Result')

temp = Label(result, text='In process...', font='Arial 15')
temp.place(relx=0, rely=0, relh=1, relw=1)

def is_win(lst):
    for comb in win_comb:
        if comb[0] in lst and comb[1] in lst and comb[2] in lst:
            return True
    return False
def show_table(btn_s):
    k = 0
    i = 0
    while i < 10:
        for j in range(3):
            btn_s[i].place(relx=(i % 3) / 3, rely=k / 3, relh=1 / 3, relw=1 / 3)
            if i < 9:
                i += 1
        k += 1
        if i % 3 == 0 and i != 3 and i != 6:
            i += 1
def foo(btn):
    if btn['text'] == 'X' or btn['text'] == '0':
        return None

    global press_count
    global end

    if press_count % 2 == 0:
        x_pos.append(int(btn['text']))
        btn['text'] = 'X'
        print('X:', x_pos)
        if is_win(x_pos):
            if not end:
                temp['text'] = 'X win!'
                print('X win!')
                end = True
    else:
        null_pos.append(int(btn['text']))
        btn['text'] = '0'
        print('Null:', null_pos)
        if is_win(null_pos):
            if not end:
                temp['text'] = '0 win!'
                print('O win!')
                end = True

    press_count += 1
    print('press:', press_count)

   #if press_count == 9:
   #    exit(990)

    if not is_win(x_pos) and not is_win(null_pos) and press_count == 9:
        temp['text'] = 'Ничья'
        print('Ничья')
        end = True

win_comb = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
x_pos = []
null_pos = []
end = False

btn_s = [Button(table, text=str(btn+1)) for btn in range(10)]
press_count = 0
show_table(btn_s)

for btn in btn_s:
    btn['command'] = lambda btn = btn: foo(btn)

result.mainloop()
table.mainloop()