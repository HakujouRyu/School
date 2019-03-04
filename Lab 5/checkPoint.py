xValue = int(input("Please enter 'x' value: "))
yValue = int(input("Please enter 'y' value: "))
if xValue == 0 and yValue == 0:
    print("(", xValue, ", ", yValue, ") is in the Origin Plane.", sep= '')
if xValue == 0 and yValue != 0:
    print("(", xValue, ", ", yValue, ") is on the X-Axis.", sep= '')
if xValue != 0 and yValue == 0:
    print("(", xValue, ", ", yValue, ") is on the Y-Axis.", sep= '')
if xValue > 0 and yValue > 0:
    print("(", xValue, ", ", yValue, ") is in the First Quadrant.", sep='')
if xValue < 0 and yValue > 0:
    print("(", xValue, ", ", yValue, ") is in the Second Quadrant.", sep='')
if xValue < 0 and yValue < 0:
    print("(", xValue, ", ", yValue, ") is in the Third Quadrant.", sep='')
if xValue > 0 and yValue < 0:
    print("(", xValue, ", ", yValue, ") is in the Fourth Quadrant.", sep='')
