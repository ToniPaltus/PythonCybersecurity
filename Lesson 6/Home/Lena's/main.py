# 6.1 Factorial
'''
def calc_fact(value):
    if value == 0 or value == 1:
        return 1
    fact = 1
    for i in range(1, value + 1):
        fact *= i
    return fact
def calc_rec_fact(value):
    if value == 0 or value == 1:
        return 1
    return value * calc_rec_fact(value - 1)

value = int(input('Enter value: '))
fact = calc_rec_fact(value)
print('Fact {} ='.format(value), fact)
'''

# 6.2 Fibonnachi
'''
import random
def calc_fib(number):
    fib1 = 1
    fib2 = 1
    for i in range(number - 2):
        sum = fib1 + fib2
        fib1 = fib2
        fib2 = sum
    return fib2
def calc_rec_fib(number):
   if number <= 2:
       return 1
   return calc_rec_fib(number - 1) + calc_rec_fib(number - 2)

number = int(input('Enter number: '))
fib = calc_rec_fib(number)
print('{} fib ='.format(number), fib)
'''

# Крестики нолики
'''
Ваша задача написать простую программу, которая делает вид, что играет в тик
tac toe с пользователем. Чтобы вам было проще, мы решили
чтобы упростить игру. Вот наши предположения:
•
компьютер (то есть ваша программа) должен играть в игру, используя
'
•
пользователь (например, вы) должен играть в игру, используя «О»;
•
первый ход принадлежит компьютеру, который он всегда делает первым
'X' в середине
•
все квадраты пронумерованы строка за строкой, начиная с 1 (см.
пример сеанса ниже для справки)
•
пользователь вводит свой ход, вводя номер
квадрат они выбирают число должно быть правильным, т.е. оно должно быть
целое число, оно должно быть больше 0 и меньше 10, и оно
не может указывать на поле, которое уже занято;
•
программа проверяет, окончена ли игра, есть четыре возможных
приговоры: игра должна продолжаться, либо игра заканчивается
ничья, ваш выигрыш или выигрыш компьютера;
•
компьютер отвечает ходом, и чек
повторяется;
•
не применяйте искусственный интеллект в какой-либо форме случайным образом
выбор поля, сделанный компьютером, достаточно хорош для
игра.
Пример сеанса работы с программой может выглядеть следующим образом:
'''
'''
# HW 6.3
#TIC TAC TOE

# display_board()                  +
# enter_move()                     +
# enter_pc ()                      +
# make_list_of_free_fields         +
# victory_for                      +
# draw_move                        +
import random

def display_board():
    print("""
    +-------+-------+-------+
    |       |       |       |
    |   {}   |   {}   |   {}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {}   |   {}   |   {}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {}   |   {}   |   {}   |
    |       |       |       |
    +-------+-------+-------+""".format(cells[0], cells[1], cells[2], cells[3], cells[4], cells[5], cells[6],cells[7], cells[8]))
def enter_move ():
    print("There are free cells: ", can_add)
    n = input("\nEnter your move: ")                 # Ввод позиции 0
    while n not in can_add:
        print("This cell is busy. Try again!")
        n = input("Enter your move: ")
    else:
        print("Excellent! You made a move!!")
        can_add.remove(n)                           # Удаление из списка свободных ячеек
        n = int(n)
        cells[n - 1] = '0'
        cells_zeros.append(str(n))
        display_board()
        victory_for_zero()
def enter_pc ():
    n = random.randrange(0, len(can_add))
    box = can_add[n]
    print("PC made a move ", box)
    cells_crosses.append(box)
    del can_add[n]                      # Удаление из списка свободных ячеек
    n = str(n)
    for i in range(len(cells)):
        if cells[i] == box:
            cells[i] = 'x'
    display_board()
    victory_for_crosses()
def victory_for_crosses():
    for name in sorted(victory_crosses.keys()):
        flg = 0
        count = 0
        for score in victory_crosses[name]:
            count = count + 1
            for i in cells_crosses:
                  if i == score:
                    flg += 1
        if flg == count:
            display_board()
            print("CrOsSeS won!!")
            exit()
def victory_for_zero():
    for name in sorted(victory_zero.keys()):
        flg = 0
        for score in victory_zero[name]:
            for i in cells_zeros:
                if i == score:
                    flg += 1
        if flg == 3:
            display_board()
            print("Zeroes won!!")
            exit()
def frendship_won():
    if can_add == []:
        print("Peace")
        return False
    return True

cells = ['1', '2', '3', '4', 'x', '6', '7', '8', '9']                       # Информация о текущей заполняемости ячеек
can_add = ['1', '2', '3', '4', '6', '7', '8', '9']                          # Список свободных ячеек
cells_crosses = []
cells_zeros = []
victory_zero ={1: ('1', '2', '3'), 2: ('3', '6', '9'), 3: ('1', '4', '7'), 4: ('7', '8', '9')}  # Победа 0
victory_crosses = {5: ('1', '9'), 6: ('2', '8'), 7: ('3', '7'), 8: ('4', '6')}                  # Победа крестиков через середину
victory_crosses.update(victory_zero)                                        # Победа крестиков везде

display_board()
flg = True
while flg:
    enter_move()
    enter_pc()
    flg = frendship_won()
    #print("0: ",cells_zeros)
    #print("x: ",cells_crosses)


'''

import random
def print_row(i):
    print('|', '|', '|', '|', sep=' ' * 7)
    print('|', table[i], '|', table[i + 1], '|', table[i + 2], '|', sep=' ' * 3)
    print('|', '|', '|', '|', sep=' ' * 7)
    print('+-------+-------+-------+')
def print_table():
   print('+-------+-------+-------+')
   for i in range(1, 8, 3):
       print_row(i)
def update_free(free):
    for key in free.keys():
        if free[key] == '0' or free[key] == 'X' or free[key] == False:
            free[key] = False
        else:
            free[key] = True

    return free
def is_winer():
    print('0:', pos_0)
    print('X:', pos_X)

    for i in range(len(win_combination)):
        if win_combination[i][0] in pos_X and win_combination[i][1] in pos_X and win_combination[i][2] in pos_X:
            print('X won!')
            return False
    for i in range(len(win_combination)):
        if win_combination[i][0] in pos_0 and win_combination[i][1] in pos_0 and win_combination[i][2] in pos_0:
            print('0 won!')
            return False
    return True

table = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9'
}
win_combination = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
win = True
pos_0 = []
pos_X = []
free = table.copy()
free = update_free(free)

iter = 0
while True in free.values() and win:
    iter += 1
    print('\nPart:', iter)
    print_table()

    free_0 = []
    for key in free.keys():
        if free[key] == True:
            free_0.append(key)
    print('Free:', free_0)
    if free_0:
        flg = True
        while flg:
            position_0 = input('Enter your position for 0: ')
            if position_0.replace(' ', '') <= '9' and position_0.replace(' ', '') >= '1' and len(position_0.replace(' ', '')) == 1:
                position_0 = position_0.replace(' ', '')
                if int(position_0) in free_0:
                    flg = False
                    position_0 = int(position_0)
                else:
                    print('This cell is filled. Please choice something from Free...')
            else:
                print('This cell is filled. Please choice something from Free...')

    table[position_0] = free[position_0] = '0'
    pos_0.append(position_0)
    free = update_free(free)
    print_table()
    win = is_winer()
    if not win:
        break

    free_X = []
    for key in free.keys():
        if free[key] == True:
            free_X.append(key)
    if free_X:
        position_X = random.choice(free_X)

    table[position_X] = free[position_X] = 'X'
    pos_X.append(position_X)
    free = update_free(free)
    print_table()
    win = is_winer()
if win:
    print_table()
    print('Draw!')

# 6.4* Files
'''
# время импорта
# формат: [сообщение] [дата и время]
# Введите то, что вы хотите сделать, пока ввод не
# равный "стоп"
# я хочу кушац
# я хочу играть
# и так далее
# останавливаться
# Функции:
# записать в файл
# читать из файла по разделителю или по строке
'''
'''
from datetime import datetime

def write_in_file(file_out):
    massage = ' '
    i = 0
    while massage != '':
        i += 1
        massage = input(f'{i}) Enter your massage: ')
        if massage != '':
            file_out.write('\n' + str(i) + ') ' + massage + '  ' + str(datetime.now()))
def read_file(file_in):
    for line in file_in:
        print(line, end='')

file = 'my_text_file'
with open(file, 'w') as file_out:
   write_in_file(file_out)

with open(file, 'r') as file_in:
   read_file(file_in)
'''