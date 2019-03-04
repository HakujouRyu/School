userBank = []
reDo = True
print("Lets play maths.")
while reDo == True:
    try:
        userIn = int(input("Please enter a whole number (0 to quit): "))
        if userIn == 0:
            reDo = False
        if userIn > 0:
            userBank.append(userIn)
    except ValueError:
        print('Please enter whole numbers!')
userBank.sort(reverse=True)
n = len(userBank)
occurrenceCount = 0
y = userBank[0]
for x in range(n):
    if y == userBank[x]:
        occurrenceCount += 1
print()
print('The largest number you entered was: ', userBank[0], sep='')
print('You entered ', y, ', ', occurrenceCount, ' times.', sep='')