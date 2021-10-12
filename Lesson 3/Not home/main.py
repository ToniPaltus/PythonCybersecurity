#Factorial

value = int(input("Enter the value: "))
copy_value = value
fact = 1
while value != 0:
    fact *= value
    value -= 1
print("Factorial of value:", copy_value, "=", fact)


#Полиндром

str = input("Enter string: ")
palindrom = True

length = len(str)
print("Length:", length)

for i in range(0, int(length/2)):
    if str[i] != str[length - i - 1]:
        palindrom = False
        break
print("String:", str, "\nPalindrom:", palindrom)

#Лучше
str = input("Enter string: ")
palindrom = str == str[::-1]
print("String:", str, "\nPalindrom:", palindrom)

str = input("Enter string: ")
if len(str) < 2:
    print('Пустая строка')
else:
    rez = str[:2] + str[-2:]
    print('Result:', rez)

















