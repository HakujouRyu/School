import math
xOne = int(input("Please enter \'x\' value of your first point: "))
yOne = int(input("Please enter \'y\' value of your first point: "))
xTwo = int(input("Please enter \'x\' value of your second point: "))
yTwo = int(input("Please enter \'y\' value of your second point: "))
distance = math.sqrt((xTwo - xOne)**2 + (yTwo - yOne)**2)
print("Distance = ", distance)