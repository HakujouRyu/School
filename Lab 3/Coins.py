qIn = int(input("Please enter the # of quarters: "))
quarter = qIn * 25
dIn = int(input("Please enter the # of dimes: "))
dime = dIn * 10
nIn = int(input("Please enter the # of nickles: "))
nickle = nIn * 5
pIn = int(input("Please enter the # of pennies: "))
penny = pIn
dollar = int((quarter + dime + nickle + penny)/100)
cents = (quarter + dime + nickle + penny)%100
print("You have a total of $", dollar, ".", cents)
print("You have ", qIn, " Quarters. ")
print("You have ", dIn, " Dimes. ")
print("You have ", nIn, " Nickles. ")
print("You have ", pIn, "Pennies. ")
