x = int(input("Введите число:"))
print(x>0 or False)

print(abs(x)/10>=1 and abs(x)/100<1)



value = input("Введите число: ")
value = int(value)

if value % 2 == 0:
    print("Четное")
else:
    print("Нечетное")



sum = int(input("Введите сумму BYN: "))

print("400 - доллары, 401 - евро")
key = input("Введите код обмена: ")

if key == "400":
    print("Валюта: Доллары")
    print("Сумма к получению: ", round(sum/2.53, 2))
elif key == "401":
    print("Валюта: Евро")
    print("Сумма к получению: ", round(sum / 3, 2))
else:
    print("Ошибка")

x = int(input("Введите число x: "))
y = int(input("Введите число y: "))

if y != 0:
    print("Деление возможно", x/y)
else:
    print("Деление не возможно")

