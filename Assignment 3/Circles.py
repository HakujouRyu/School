import math
x1 = int(input("Please enter the X value of the first center: "))
y1 = int(input("Please enter the Y value of the first center: "))
rad1 = int(input("Please enter the radius of the first circle: "))
x2 = int(input("Please enter the X value of the second center: "))
y2 = int(input("Please enter the Y value of the first center: "))
rad2 = int(input("Please enter the radius of the second circle: "))
distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
if rad1 > (distance + rad2):
    print("Completely inside")
elif rad1 < distance:
        if distance < (rad1 + rad2):
            print("Overlapped")
        elif distance > (rad1 + rad2):
            print("Completely outside")
elif distance == (rad1 + rad2):
    print("Circles touch")
