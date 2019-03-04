hiGrade = int(0)
loGrade = int(0)
try:
    grade1 = int(input("Please enter your first grade (0 - 100): "))
except:
    grade1 = 105
while grade1 < 0 or grade1 > 100:
    try:
        print("ERROR: Please enter valid grade value")
        grade1 = int(input("Please reenter your first grade (0 - 100): "))
    except:
        grade1 = 105

hiGrade = grade1
loGrade = grade1
try:
    grade2 = int(input("Please enter your second grade (0 - 100): "))
except:
    grade2 = 105
while grade2 < 0 or grade2 > 100:
    try:
        print("ERROR: Please enter valid grade value")
        grade2 = int(input("Please reenter your second grade (0 - 100): "))
    except:
        grade2 = 105
if grade2 > hiGrade:
    hiGrade = grade2
if grade2 < loGrade:
    loGrade = grade2
try:
    grade3 = int(input("Please enter your third grade (0 - 100): "))
except:
    grade3 = 105
while grade3 < 0 or grade3 > 100:
    try:
        print("ERROR: Please enter valid grade value")
        grade3 = int(input("Please reenter your third grade (0 - 100): "))
    except:
        grade3 = 105
if grade3 > hiGrade:
    hiGrade = grade3
if grade3 < loGrade:
    loGrade = grade3
try:
    grade4 = int(input("Please enter your last grade (0 - 100): "))
except:
    grade4 = 105
while grade4 < 0 or grade4 > 100:
    try:
        print("ERROR: Please enter valid grade value")
        grade4 = int(input("Please reenter your last grade (0 - 100): "))
    except:
        grade4 = 105
if grade4 > hiGrade:
    hiGrade = grade4
if grade4 < loGrade:
    loGrade = grade4
avgGrade = ((grade4 + grade3 + grade2 + grade1) / 4)
print("you entered: ", grade1, ", ", grade2, ", ", grade3, ", ", grade4, sep='')
print("Highest Grade: ", hiGrade)
print("Lowest Grade: ", loGrade)
print("Average Grade: ", avgGrade)