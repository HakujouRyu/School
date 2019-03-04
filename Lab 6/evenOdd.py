evenArray = []
oddArray = []
evenCounter = 50
oddCounter = 51
while evenCounter < 100:
    evenArray.append(str(evenCounter))
    evenCounter += 2
while oddCounter < 100:
    oddArray.append(str(oddCounter))
    oddCounter += 2
evenOut = ", " .join(evenArray)
oddOut = ", " .join(oddArray)
print("Even numbers between 50 and 100: ", evenOut)
print("Odd numbers between 50 and 100: ", oddOut)
