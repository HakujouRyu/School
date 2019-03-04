sentinel = True
userIn = 0
counter = 2
sum = 0
while sentinel is True:
    while userIn == 0:
        try:
            userIn = int(input("Please enter a number between 20 and 60: "))
        except ValueError:
            print("Please follow the rules!")
    if userIn < 20 or userIn > 60:
        print("Please follow the rules!")
        userIn = 0
    inclusion = userIn % 2
    if inclusion == 0:
        while counter <= (userIn):
            sum += counter
            counter += 2
    else:
        while counter < userIn:
            sum += counter
            counter += 2
    print(userIn)
    print(sum)
    userIn = 0
    sum = 0
    counter = 0