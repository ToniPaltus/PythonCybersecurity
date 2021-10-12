filename = 'messages.txt'
massages = list()

for i in range(4):
    massage = input('Enter string ' + str(i + 1) + ': ')
    massages.append(massage + '\n')

with open(filename, 'a') as file:
    for massage in massages:
        file.write(massage)
print('Считанные сообщения')
with open(filename, 'r') as file:
    for massage in file:
        print(massage, end='')