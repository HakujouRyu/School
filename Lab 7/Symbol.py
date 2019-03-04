width = 0
length = 0
loop1 = True
loop2 = True
sentinel =  True
while sentinel is True:
    while loop1 is True:
        try:
            userIn = int(input("Please enter a number: "))
        except ValueError:
            print("Try again.")
        else:
            loop1 = False
    while loop2 is True:
        try:
            userChar = input("Please enter a symbol: ")
        except ValueError:
            "Try again!"
        else:
            loop2 = False
    for i in range(userIn):
        for x in range(userIn):
            print(userChar, end='')
        print()
    width = 0
    height = 0
    loop1 = True
    loop2 = True