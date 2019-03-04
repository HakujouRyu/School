travelDistance = int(input("Please enter the number of miles to be traveled: "))
mpg = int(input("Please enter your average MPG: "))
fuelCost = float(input("Please enter estimated $/gallon: "))
fuelUse = travelDistance / mpg
tripCost = fuelUse * fuelCost
print("The estimated cost of your travel distance is $", tripCost)