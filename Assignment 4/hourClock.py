tops = 10
topSpace = 0
while tops > 0:
    for space in range(0, topSpace):
        print(" ", end='')
    topSpace += 1
    for stars in range(1, tops):
            print("*", end='')
    print()
    tops -= 2
bottoms = 3
bottomSpace = 4
while bottoms < 11:
    for space in range(1, bottomSpace):
        print(" ", end='')
    bottomSpace -= 1
    for star in range(0, bottoms):
        print("*", end='')
    bottoms += 2
    print()
