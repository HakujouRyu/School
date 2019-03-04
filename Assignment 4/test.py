num = 7
space = 0
while num > 0:
    for x in range(0, space):
        print(" ", end='')
    space += 1
    for x in range(1, num):
        print(" ", end='')
        print(x, end='')
    num -= 1
    print()