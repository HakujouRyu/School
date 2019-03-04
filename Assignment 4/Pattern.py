num = 6
blank = 1
for line in range(6):
    for space in range(1, blank):
        print(" ", end='')
    blank += 1
    for column in range(1, num+1):
        print(" ", end='')
        print(column, end='')
    num -= 1
    print()
