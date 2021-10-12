# 5.1 Calculator

def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def division(a, b):
    if b != 0:
        return a / b
    else:
        print('Division is not possible!')
def multiplication(a, b):
    return a * b
def ost_division(a, b):
    if b != 0:
        return a % b
    else:
       print('Ost_division is not possible!')
def whole_division(a, b):
    if b != 0:
        return a // b
    else:
        print('Whole_division is not possible!')
def degree(a, b):
    return a**b
def is_odd(a):
    if ost_division(a, 2) != 0:
        return True
    else:
        return False
def is_even(a):
    return not(is_odd(a))
def get_type(a):
    return type(a)
def get_max(a, b):
    return a if a > b else b
def get_min(a, b):
    return a if a < b else b
def get_avg(a, b):
    return plus(a, b) / 2
def set_type(var):
    if var.isdigit():
        flg = True
        while flg:
            chose = int(input('Choose the type of variable {} (int - 1, float - 2): '.format(var)))
            if chose == 1 or chose == 2:
                flg = False
                if chose == 1:
                    var = int(var)
                else:
                    var = float(var)
            else:
                print('Uncorrect input. Try again...')
        return var
    else:
        print('Not a number')
        exit(990)
def my_replace(var):
    return var.replace(' ', '')

a = my_replace(input('Enter a: '))
operat = my_replace(input('Enter operator: '))
b = my_replace(input('Enter b: '))

a = set_type(a)
b = set_type(b)
rez = ' '

if operat == '+':
    rez = plus(a, b)
elif operat == '-':
    rez = minus(a, b)
elif operat == '/':
    rez = division(a, b)
elif operat == '*':
    rez = multiplication(a, b)
elif operat == '%':
    rez = ost_division(a, b)
elif operat == '//':
    rez = whole_division(a, b)
elif operat == '**':
    rez = degree(a, b)
elif operat == 'odd':
    rez = [is_odd(a), is_odd(b)]
elif operat == 'even':
    rez = [is_even(a), is_even(b)]
elif operat == 'type':
    rez = [get_type(a), get_type(b)]
elif operat == 'max':
    rez = get_max(a, b)
elif operat == 'min':
    rez = get_min(a, b)
elif operat == 'avg':
    rez = get_avg(a, b)
else:
    print('Uncorrect input. Sorry. Try again next time...')
if rez != ' ':
    print(f'{a} {operat} {b} =', rez)


# 5.2 Leap Year
'''
def is_year_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    year = test_data[i]
    print(year, '->', end='')
    result = is_year_leap(year)
    if result == test_results[i]:
        print('Ok')
    else:
        print('Failed')
'''

# 5.3 leap year remastered
'''
def is_year_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
def days_in_month(year, month):
    if month > 12 or month < 1:
        return None
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    thurty = [4, 6, 9, 11]
    thurty_one = [1, 3, 5, 7, 8, 10, 12]

    if month in thurty:
        return 30
    else:
        return 31

test_years = [1900, 2000, 2016, 1987]
test_month = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    year = test_years[i]
    month = test_month[i]
    print(year, month, '->', end='')
    result = days_in_month(year, month)
    if result == test_results[i]:
        print('Ok')
    else:
        print('Failed')
'''

# 5.4 Count of days in the year
'''
def is_year_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
def days_in_month(year, month):
    if month > 12 or month < 1:
        return None
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    thurty = [4, 6, 9, 11]
    thurty_one = [1, 3, 5, 7, 8, 10, 12]

    if month in thurty:
        return 30
    else:
        return 31
def day_of_year(year, month, day):
    sum = day
    for i in range(1, month):
        if days_in_month(year, i) != None:
            sum += days_in_month(year, i)
        else:
            return 'Error'
    return sum

print(day_of_year(2000, 12, 31))
print(day_of_year(2007, 11, 12))
print(day_of_year(20013, 5, 6))
'''

# 5.5 Prime number
'''
def is_prime(number):
    prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            prime = False
            break
    return prime

number = int(input('Enter number: '))
for i in range(1, number):
    if is_prime(i + 1):
        print(i + 1, end=' ')
'''

# 5.6 мили на галон -> литры/100 км
'''
def liters_100km_to_miles_gallon(liters):
    return(100 * 3.785)/(liters * 1.609)
def miles_gallon_to_liters_100km(miles):
    return(100 * 3.785)/(miles * 1.609)

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
'''