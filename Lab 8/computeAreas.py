def square_area(x):
    result = x ** 2
    return result


def rectangle_area(x, y):
    result = (y * x)
    return result


def circle_area(x):
    result = 3.14 * (x ** 2)
    return result


def triangle_area(x, y):
    result = (x * y) / 2
    return result


loop1 = True
#program Shell
loop2 = True
#Shape Shell
loop3 = True
#Dimensions Shell
while loop1 is True:
    while loop2 is True:
        shapeChoice = input("What is your shape? \n"
                    "1. square \n"
                    "2. rectangle\n"
                    "3. circle\n"
                    "4. triangle \n")
        try:
            shapeChoice =float(shapeChoice)
            loop2 = False
        except ValueError:
            print("Please try again!")
    if shapeChoice == 1:
        while loop3 is True:
            dimension = input("Please enter length of side: ")
            try:
                dimension = float(dimension)
                loop3 = False
            except ValueError:
                print("Please try again!")

        print("The area of the square is: ", square_area(dimension))
        loop2 = True
        loop3 = True
        del dimension

    if shapeChoice == 2:
        while loop3 is True:
            dimension1 = input("Please enter length: ")
            dimension2 = input("Please enter width: ")
            try:
                dimension1 = float(dimension1)
                dimension2 = float(dimension2)
                loop3 = False
            except ValueError:
                print("Please try again!")

        print("The area of the rectangle is: ", rectangle_area(dimension1, dimension2))
        loop2 = True
        loop3 = True
        del dimension1
        del dimension2

    if shapeChoice == 3:
        while loop3 is True:
            dimension = input("Please enter length of radius: ")
            try:
                dimension = float(dimension)
                loop3 = False
            except ValueError:
                print("Please try again!")

        print("The area of the circle is: ", circle_area(dimension))
        loop2 = True
        loop3 = True
        del dimension

    if shapeChoice == 4:
        while loop3 is True:
            dimension1 = input("Please enter length of base: ")
            dimension2 = input("Please enter height: ")
            try:
                dimension1 = float(dimension1)
                dimension2 = float(dimension2)
                loop3 = False
            except ValueError:
                print("Please try again!")

        print("The area of the trangle is: ", triangle_area(dimension1, dimension2))
        loop2 = True
        loop3 = True
        del dimension1
        del dimension2

