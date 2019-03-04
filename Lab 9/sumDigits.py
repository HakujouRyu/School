def sumDigits(x):
    printsum = 0
    while x > 0:
        printsum += x % 10
        x = (x // 10)
    return printsum


while True:
    try:
        userIn = int(input("Please enter a positive integer:  "))
        break
    except ValueError:
        print("Please try again")
if userIn > 0:
    print("You entered: ", userIn, sep='')
    print("Sum of digits: ", sumDigits(userIn), sep='')
else:
        print("You didn't follow the rules! Try again")