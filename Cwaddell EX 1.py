import random

def SortArray(x):
    swap = 0
    while True:
        for i in range(1, len(x)):
            if x[i-1] > x[i]:
                temp = x[i]
                x[i] = x[i - 1]
                x[i-1] = temp
                swap += 1
        if swap == 0:
            break
        swap = 0

def printout(x):
    for i in range(len(x)):
        print('The value at [', i, '] is: ', x[i], end='')
        print()


listRand = []
for i in range(10):
    listRand.append(random.randint(0, 100))
print('Before sort')
printout(listRand)
# listA = [11, 4, 44, 14, 5]
# print(listRand)
# print(listA)
SortArray(listRand)
# SortArray(listA)
# print(listRand)
# print(listA)
print('After Sort')
printout(listRand)
