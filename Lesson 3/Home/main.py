import random
level = int(input("Enter level of your tree: "))

length = 1
for i in range(1, level):
    length += 2
#print('Length:', length)
center = int(length / 2 + 1)
#print('Center:', center)

fon = input('Enter the fon: ')
agg = input('Enter the aggregate: ')
toy = input('Enter the toy: ')

aggregate = 1
for i in range(1, level + 1):
    if i % 2 == 1:
        print(fon * (center - i), agg * aggregate, fon * (length - aggregate - center + i), sep='')
    else:
        toy_poz = int(random.uniform(1, aggregate))
        #print('Random:', toy)
        #print('aggregate:', aggregate)
        print(fon * (center - i), agg * toy_poz, toy, agg * (aggregate - toy_poz - 1), fon * (length - aggregate - center + i), sep='')
    aggregate += 2