acctNum = input("Please enter account Number: ")
acctType = input("Is account premium? Y/N: ")
if acctType == "n" or acctType == "n":
    totalMinutes = int(input("Please enter total minutes used: "))
    acctType = "Regular"
    regPrice = int(15)
    regExcess = float(0.50)
    excessMinutes = int(0)
    if totalMinutes > 50:
        excessMinutes = (totalMinutes - 50) * regExcess
    print("Account Number: ", acctNum)
    print("Account Type ", acctType)
    print("Amount Due: $", regPrice + excessMinutes)

elif acctType == "y" or acctType == "Y":
    acctType = "Premium"
    premPrice = int(25)
    premDay = float(0.20)
    premNight = float(0.10)
    dayExcess = int(0)
    nightExcess = int(0)
    dayMin = int(input("Please enter total daytime minutes: "))
    nightMin = int(input("Enter total nighttime minutes: "))
    if dayMin > 50:
        dayExcess = (dayMin - 50) * premDay
    if nightMin > 100:
        nightExcess = (nightMin - 100) * premNight
    print("Account Number: ", acctNum)
    print("Account Type ", acctType)
    print("Amount Due: $", (premPrice + dayExcess + nightExcess))
else:
    print("ERROR: invalid account type, please try again.")