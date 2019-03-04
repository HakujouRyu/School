sum = int(0)
counter = 0
userIn = 105
while userIn <= 1 or userIn > 100:
    try:
        userIn = int(input("Please enter a number between 1 and 100: "))
        if userIn <= 0 or userIn > 100:
         print("Invalid input. Try again.")
    except:
        print("Invalid input. Try again.")
        userIn = 105

while counter <= userIn:
    sum += counter
    counter += 1
print("You entered", userIn)
print("Sum of values: ", sum)