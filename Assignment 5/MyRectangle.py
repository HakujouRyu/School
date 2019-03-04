def isValid(width, height):
    if (width + height) > 30:
        return True
    else:
        return False


def my_area(width, height):
    if isValid(width, height) is True:
        area = width * height
        return area
    else:
        return False


def my_perimeter(width, height):
    if isValid(width, height) is True:
        perimeter = (width * 2) + (height * 2)
        return perimeter
    else:
        return False


try:
    width = int(input("Please enter width of rectangle: "))
    height = int(input("Please enter height of rectangle:  "))
except ValueError:
    print("Please try again!")

print("Entered width: ", width, sep='')
print("Entered height: ", height, sep='')

if isValid(width, height) is False:
    print("This is an invalid rectangle. Try again")
if isValid(width, height):
    print("Area: ", my_area(width, height), sep='')
    print("Perimeter: ", my_perimeter(width, height), sep="")

