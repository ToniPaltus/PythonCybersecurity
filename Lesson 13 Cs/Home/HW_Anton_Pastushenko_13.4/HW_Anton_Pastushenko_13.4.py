# 13.4
# Дан txt файл (Седержимое ниже, созайте файл ручками
# дома сами) со списком домашних телефонов в формате ***-**-**
# Достать из файла все номера телефонов начинающиеся
# с цифры 3 или 2, имеющие в качестве 3 цифры цифру ноль.
# В файле могут содержаться также битые номера. по этому проверяем формат.
# Все подходящие номера пишем в новый файл в
# формате: "Статус: OK; Номер :3*0-**-**;"
# Все неподходящие номера пишем в новый файл в формате:
# Статус: BAD; Номер :*в формате в котором он
import re

def write(file_name, status, ph):
    with open(file_name, 'a') as file_out:
        file_out.write('Status: ' + status + '; ' + 'Number: ' + str(ph) + '\n')
def read(file_name):
    with open(file_name, 'r') as file_in:
        print()
        for line in file_in:
            print(line, end='')
def clear(file_name):
    with open(file_name, 'w') as f:
        f.close()

file_name = 'phones.txt'
file_good = 'good.txt'
file_bed = 'bed.txt'

lst = []
with open(file_name, 'r') as file_in:
    for line in file_in:
        lst.append(line[:-1])
print(lst)

lst_good = []
for val in lst:
    if re.match(r'[2-3]{1}[0-9]{1}[0]{1}', val):
        lst_good.append(val)
print(lst_good)

lst_bed = []
for ph in lst:
    if ph not in lst_good:
        lst_bed.append(ph)
print(lst_bed)

for ph in lst_good:
    write(file_good, 'Good', ph)
for ph in lst_bed:
    write(file_bed, 'Bad', ph)
read(file_good)
read(file_bed)
#clear(file_good)
#clear(file_bed)