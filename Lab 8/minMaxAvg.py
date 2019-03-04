def my_max(x, y, z):
    maxList = [x, y, z]
    maxList.sort(reverse=True)
    result = maxList[0]
    return result


def my_min(x, y, z):
    minList = [x, y, z]
    minList.sort()
    result = minList[0]
    return result


def my_avg(x, y, z):
    result = ((x + y + z) / 3)
    return result


userIn1 = int(input("Please enter a number: "))
userIn2 = int(input("Please enter a second number: "))
userIn3 = int(input("Please enter a third number: "))
print("You entered: ", userIn1, ", ", userIn2, ", ", userIn3, sep='')
print("Max value of your three numbers is: ", my_max(userIn1, userIn2, userIn3))
print("Min value of your three numbers is: ", my_min(userIn1, userIn2, userIn3))
print("Average of the three numbers is: ", my_avg(userIn1, userIn2, userIn3))