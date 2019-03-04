stars = 1
spaceCounter = 8
while stars < 16:
    for space in range(1, spaceCounter):
        print(" ", end='')
    spaceCounter -= 1
    for column in range(0, stars):
        print("*", end='')
    stars += 2
    print()
