#2.1
print("Programming", "Essentials", "in", sep = '***', end = '...')
print("Python")

#2.2
print("    *\n   * *\n  *   *\n *     *\n* *   * *\n  *   *\n  *   *\n  *****\n"*2)

print(" "," "," "," ",'*',' ',' ',' ',' ',' ', sep = ' ')
print(" "," "," ","*",' ','*',' ',' ',' ',' ', sep = ' ')
print(" "," ","*"," ",' ',' ','*',' ',' ',' ', sep = ' ')
print(" ","*"," "," ",' ',' ',' ','*',' ',' ', sep = ' ')
print("*","*","*"," ",'',' ',' *','*','*',' ', sep = ' ')
print(" "," ","*"," ",' ',' ','*','',' ',' ', sep = ' ')
print(" "," ","*"," ",' ',' ','*',' ',' ',' ', sep = ' ')
print(" "," ","*","*",'*','*','*',' ',' ',' ', sep = ' ')

#2.3
print ("\n\"I\'m\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")


#2.4
John = int(input("Enter the number of John\'s apples "))
Mary = int(input("Enter the number of Mary\'s apples "))
Adam = int(input("Enter the number of Adam\'s apples "))
sum = Adam + Mary + John
sr = round(sum/3, 1)
max = max(John, Adam, Mary)
print("John has ", John, " apples\n", "Mary has ", Mary, " apples\n", "Adam has ", Adam, " apples\n", "Average number of apples is ", sr, "\nMax number of apples is ", max, sep='')


#2.5
km = float(input("kilometers = "))
ml = float(input("miles = "))
ml1 = round(km/1.61, 2)
km1 = round(ml*1.61, 2)
print(km, "kilometers is", ml1, "miles\n", ml, 'miles is', km1, 'kilometers')


#2.6
x = int(input("x = "))
#y = round((3*(x**3) - 2*(x**2) + 3*x - 1), 1)

y =(3*(x ** 3) - 2*(x ** 2) + 3*x - 1)
print("y =", y)


#2.7
#number of seconds in a number of hours
a = 2                  # number of hours
seconds = 3600         # number of seconds in 1 hour
print("Hours: ", a)
print("Seconds in Hours: ", a * seconds)


#2.8
x = int(input("Enter number: "))
znak = input("Enter sign: ")
y = int(input("Enter number: "))
if znak == '+':
    rez = x + y
elif znak == '-':
    rez = x - y
elif znak == '/':
    rez = x / y
elif znak == '*':
    rez = x * y
print(x, znak, y, '=', rez)

flg = int(input("Enter 1 to continue\nEnter  0 to end\n"))
while flg:
    rez1 = rez
    znak = input("Enter sign: ")
    y = int(input("Enter number: "))
    if znak == '+':
        rez += y
        print(rez1, znak, y, '=', rez)
    elif znak == '-':
        rez -= y
        print(rez1, znak, y, '=', rez)
    elif znak == '/':
        rez /= y
        print(rez1, znak, y, '=', rez)
    elif znak == '*':
        rez *= y
        print(rez1, znak, y, '=', rez)



#2.9
x = int(input("x = "))
y = round(1/(x + 1/(x + 1/(x + 1/x))), 1)
print("y = ", y)


#2.10
print("Hello, world!")


#2.11
a = 11111*1111111
print(a)


#2.12
a = 42/(4+2*(-1))
print(a)


#2.13
print(2021**21)


#2.14
days = int(input("Enter the number of days "))
print("In ", days, "days", days*60*60*24, "seconds")


#2.15
num = int(input("Enter the num "))
deg = int(input("Enter degree of number "))
rez = num**deg
print(num, "in degree", deg, "is", rez)
