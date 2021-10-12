'''
ДЗ! Используя предыдущие функции,
 реализуйте еще одну функцию, которая будет выводить введенную
  сумму денег с плавающей точкой прописью (ввели «0,70» –
   функция возвращает «ноль рублей семьдесят копеек»).
'''

def point(Value):
    return len(Value) - Value.find('.') - 1
def number_to_string(Value, my_woman):
    #value = int(input('Введите свое число от 0 до 999: '))
    value = int(Value)
    hundreds = value // 100
    magic = value % 100
    dozens = int(value / 10 % 10)
    units = value % 10
    # print(hundreds, magic, dozens, units)

    result = ''
    # 0
    if int(value) == 0:
        result = 'ноль'
        print('Ваше число:', result)
        exit(990)

    # Сотни
    if hundreds:
        hundreds_list = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот',
                         'девятьсот']
        result += hundreds_list[hundreds - 1]

    # 10 - 19
    is_magic = False
    magic_list = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
                  'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    for i in range(len(magic_list)):
        if magic == i + 10:
            is_magic = True
            result += ' ' + magic_list[i]

    # Род
    woman = False
    if units == 1 or units == 2:
        #woman = bool(input('Ведите род числа (мужской - ничего, женский - что угодно): '))
        woman = my_woman

    # Десятки и единицы
    if not is_magic:
        if dozens:
            dozens_list = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
                           'девяносто']
            result += ' ' + dozens_list[dozens - 2]
        if units:
            if woman:
                units_list_wom = ['одна', 'две']
                result += ' ' + units_list_wom[units - 1]
            else:
                units_list = ['один', 'два', 'три', 'черыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
                result += ' ' + units_list[units - 1]
    return result
def rub_to_string(Value):
    #rub = int(input("Введите число рублей на ваш счет: "))
    rub = int(Value)
    ost_10 = rub % 10
    ost_100 = rub % 100
    s = "рублей"

    if ost_100 >= 11 and ost_100 <= 14:
        s = s
    elif ost_10 == 1:
        s = "рубль"
    elif ost_10 == 2 or ost_10 == 3 or ost_10 == 4:
        s = "рубля"
    return s
def kop_to_string(Value):
    #kop = int(input("Введите число копеек на ваш счет: "))
    kop = int(Value)
    ost_10 = kop % 10
    ost_100 = kop % 100
    s = "копеек"

    if ost_100 >= 11 and ost_100 <= 14:
        s = s
    elif ost_10 == 1:
        s = "копейка"
    elif ost_10 == 2 or ost_10 == 3 or ost_10 == 4:
        s = "копейки"
    return s
def value_to_string(Value):
    fractional_count = point(Value)
    #print('Fractional_count', fractional_count)

    #print('Whole_part:', (Value[:len(Value) - fractional_count - 1]), type(Value[:len(Value) - fractional_count - 1]))
    whole_part = number_to_string((Value[:len(Value) - fractional_count - 1]), False)
    rub = rub_to_string((Value[:len(Value) - fractional_count - 1]))

    #print('Fractional_part:', (Value[(len(Value) - fractional_count):]), type(Value[(len(Value) - fractional_count):]))
    fractional_part = number_to_string((Value[(len(Value) - fractional_count):]), True)
    kop = kop_to_string((Value[(len(Value) - fractional_count):]))

    return whole_part + ' ' + rub + ' ' + fractional_part + ' ' + kop

str = input('Enter value: ')
print('String:', value_to_string(str))