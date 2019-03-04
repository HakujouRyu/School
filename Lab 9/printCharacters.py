def print_chars(x, y):
    start = ord(x)
    end = ord(y)
    i = start
    j = 0
    while i <= end:
        print(chr(i), end='')
        i += 1
        j += 1
        if j % 5 == 0:
            print()


while True:
    while True:
        try:
            userInA = input("Please enter start Character:  ")
            if len(userInA) == 1:
                try:
                    if int(userInA) >= 0 or int(userInA) < 0:
                        print("Please enter a letter!")
                    else:
                        break
                except ValueError:
                    break
            else:
                print("One letter please:")
        except ValueError:
            print("What did you even do to see this?")
    while True:
        try:
            userInB = input("Please enter end Character:  ")
            if len(userInB) == 1:
                try:
                    if int(userInB) >= 0 or int(userInB) < 0:
                        print("Please enter a letter!")
                    else:
                        break
                except ValueError:
                    break
            else:
                print("One letter please:")
        except ValueError:
            print("What did you even do to see this?")
    if ord(userInA) < ord(userInB):
        break
    else:
        print("put start letter first!")

print_chars(userInA, userInB)
