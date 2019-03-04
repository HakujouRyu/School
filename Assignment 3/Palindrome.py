userInput = 0
while userInput > 99999 or userInput < 11111:
    try:
        userInput = int(input("Please enter a number between 11111 and 99999: "))
    except:
        print("Error: Follow the rules!")
        userInput = -1
onesDigit = int(userInput % 10)
userInput = int(userInput / 10)
tensDigit = int(userInput % 10)
userInput = int(userInput / 10)
hundDigit = int(userInput % 10)
userInput = int(userInput / 10)
thouDigit = int(userInput % 10)
userInput = int(userInput / 10)
tenkDigit = int(userInput)
print(onesDigit, tensDigit, hundDigit, thouDigit, tenkDigit)

while onesDigit != tenkDigit or tensDigit != thouDigit:
    while userInput > 99999 or userInput < 11111:
        try:
            userInput = int(input("Sorry, try again! Please enter a number between 11111 and 99999: "))
        except:
            print("Error: Follow the rules!")
            userInput = 0
    onesDigit = int(userInput % 10)
    userInput = int(userInput / 10)
    tensDigit = int(userInput % 10)
    userInput = int(userInput / 10)
    hundDigit = int(userInput % 10)
    userInput = int(userInput / 10)
    thouDigit = int(userInput % 10)
    userInput = int(userInput / 10)
    tenkDigit = int(userInput)
    print(onesDigit, tensDigit, hundDigit, thouDigit, tenkDigit)
else:
    print("Congratulations!! That’s a palindrome!")